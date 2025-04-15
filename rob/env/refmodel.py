from toffee import *
from env.rob_wrapper import *
class Snapshot:
    def __init__(self, value: int, flag: int):
        self.value = value
        self.flag = flag

class RobModel(Model):
    def __init__(self):
        super().__init__()
        self.queue = [Rob_Instr() for _ in range(160)]
        self.enq_ptr = 0
        self.deq_ptr = 0
        self.enq_flag = 0
        self.deq_flag = 0
        self.rob_size = 160
        self.line_size = 8
        self.all_commit = 0
        self.line_total = 20
        self.redirect = 0
        self.snapshots = [Snapshot(0,0) for _ in range(4)]
        self.snapshots_id = 0
        self.snapshots_size = 4

    def _check_enq(self):
        self.inst_size = abs(self.enq_ptr - self.deq_ptr)

        if self.redirect or self.inst_size > 154:
            return False
        return True

    def update_snapshot(self):
        snap = Snapshot(self.enq_ptr, self.enq_flag)
        self.snapshots[self.snapshots_id] = snap
        self.snapshots_id = (self.snapshots_id + 1) % self.snapshots_size

    def update_ptr(self,ptrtype):
        """update ptr and flag"""
        if ptrtype :
            self.enq_ptr = (self.enq_ptr + 1) % self.rob_size
            if self.enq_ptr == 0:
                self.enq_flag = 1 - self.enq_flag
        else:
            self.deq_ptr = (self.deq_ptr + 1) % self.rob_size
            if self.deq_ptr == 0:
                self.deq_flag = 1 - self.deq_flag

    @driver_hook(agent_name="enq_agent")
    def enq_list(self, instr_list):
        if self._check_enq():
            for inst in instr_list:
                print(inst)
                self.queue[self.enq_ptr] = inst
                if inst.snapshot:
                    self.update_snapshot()
                self.update_ptr(1)

    def flush(self,idx_flag,idx_value,level,use_snpt):
        walk_end = None
        if level:
            walk_end = idx_value
        else:
            walk_end = idx_value + 1

        same_flag_candidates = []
        diff_flag_candidates = []

        for snap in self.snapshots:
            if not (0 <= snap.value < 160 and snap.flag in (0,1)):
                continue

            if snap.flag == self.deq_flag:
                if snap.value > self.deq_ptr:
                    same_flag_candidates.append(snap)
            else:
                diff_flag_candidates.append(snap)

        walk_start = None
        if same_flag_candidates:
            walk_start = min(same_flag_candidates, key = lambda x: x.value)
        elif diff_flag_candidates:
            walk_start = min(diff_flag_candidates, key = lambda x: x.value)
        if walk_start or use_snpt == 0:
            walk_start = self.deq_ptr

        inst = Rob_Instr()
        if self.enq_flag == self.deq_flag:
            for idx in range(walk_end, self.enq_ptr):
                self.queue[idx] = inst
            self.enq_ptr = walk_end
        else:
            for idx in range(self.walk_end, self.rob_size):
                self.queue[idx] = inst
            for idx in range(0, self.enq_ptr):
                self.queue[idx] = inst
            self.enq_ptr = walk_end
            self.enq_flag = self.deq_flag


    @driver_hook(agent_name="enq_agent")
    def rob_redirect(self, valid, idx_flag, idx_value, level, use_snpt=0):
        self.redirect = valid

        if self.redirect:
            self.flush(idx_flag,idx_value,level,use_snpt)

    def update_entry(self, id, uopnums):
        if not 0 <= id <= 159:
            raise ValueError("writeback inst id must in 0-159")
        self.queue[id].numWB = max(0,self.queue[id].numWB - uopnums)

    def _check_commit(self):
        current_block = self.deq_ptr // self.line_size
        end = min(current_block * self.line_size + self.line_size, self.enq_ptr)

        for idx in range(self.deq_ptr, end):
            if self.queue[idx].numWB != 0:
                self.commit(idx)
            elif idx == end:
                self.all_commit = 1
                self.commit(idx)

    def commit(self,new_deq_ptr,end = 0):
        inst = Rob_Instr()
        for idx in range(self.deq_ptr,new_deq_ptr):
            self.queue[idx] = inst

        old_flag_state = self.deq_flag
        if self.all_commit:
            self.deq_ptr = end + 1
        else:
            self.deq_ptr = new_deq_ptr

        if (old_flag_state == 0 and self.deq_ptr == 0) or \
           (old_flag_state == 1 and self.deq_ptr == 160//self.line_size):
            self.deq_flag = 1 - self.deq_flag

    @driver_hook(agent_name="wb_agent")
    def writeback_list(self, writeback_list):
        for wbinfo in writeback_list:
            self.update_entry(wbinfo.robIdx_value,wbinfo.nums)
        self._check_commit()



