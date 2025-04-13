from toffee import *
from env.rob_wrapper import *

class RobModel(Model):
    def __init__(self):
        super().__init__()
        self.queue = [Rob_Instr() for _ in range(160)]
        self.enq_ptr = 0
        self.deq_ptr = 0
        self.enq_flag = 0
        self.deq_flag = 0
        self.line_size = 8
        self.all_commit = 0
        self.line_total = 20
        

    def update_ptr(self,ptrtype):
        """update ptr and flag"""
        if ptrtype :
            self.enq_ptr = (self.enq_ptr + 1) % 160
            if self.enq_ptr == 0:
                self.enq_flag = 1 - self.enq_flag
        else:
            self.deq_ptr = (self.deq_ptr + 1) % 160
            if self.deq_ptr == 0:
                self.deq_flag = 1 - self.deq_flag

    @driver_hook(agent_name="enq_agent")
    def enq_list(self, instr_list):
        for instr in instr_list:
            print(instr)
            self.queue.append(instr)
            self.update_ptr(1)
        print("[RobModel] Enqueueing instructions:")
        print("update enq_ptr: ",self.enq_ptr)

    @driver_hook(agent_name="enq_agent")
    def rob_redirect(self, valid, idx_flag, idx_value, level, useSnpt=0):
        print("[RobModel] Rob redirecting:")
        print(f"valid: {valid}, idx_flag: {idx_flag}, idx_value: {idx_value}, level: {level}, useSnpt: {useSnpt}")

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
        print("[RobModel] Writeback channel:")
        print(f"writeback_instr: {writeback_list}")



