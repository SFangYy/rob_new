import random
from env.rob_wrapper import *

class GenBase():
    def __init__(self,env):
        self.env = env
        self.enqptr = 0
        self.deqptr = 0
        self.can_wb = [-1] *160
        self.wb_channel = [0] *28
        self._deq_ptr = 0
        self._rob_idx = 0
        self._enq_ptr = 0
        self.enq_ptr_flag = 0
        self.deq_ptr_flag = 0
        self.count = 0
        #self.snapshot =  deque(maxlen=4)
        self.enq_exception_list = [0,1,2,12,20,22]
        self.inst_list = []


    @property
    def rob_idx(self):
        return self._rob_idx

    @property
    def enq_ptr(self):
        return self._enq_ptr
    @property
    def deq_ptr(self):
        return self._deq_ptr

    @enq_ptr.setter
    def enq_ptr(self, new_value):

        self._enq_ptr = self._update_value(new_value,"enq_ptr_flag")
    @deq_ptr.setter
    def deq_ptr(self, new_value):
        self.count -= 1
        self._deq_ptr = self._update_value(new_value,"deq_ptr_flag")

    @rob_idx.setter
    def rob_idx(self, new_value):
        self.count += 1
        self._rob_idx = self._update_value(new_value)

    def _update_value(self, new_value,type = ""):
        if new_value == 160:

            if type != "":
                setattr(self,type,1 if getattr(self,type) == 0 else 0)
                print(self.enq_ptr_flag)
            return 0
        return new_value

    def add_robidx(self):
        self.rob_idx = self._rob_idx + 1

    def add_enqptr(self,numWB = -1):
        self.can_wb[self.enq_ptr] = numWB
        self.enq_ptr = self._enq_ptr + 1
    def add_deqptr(self):
        self.deq_ptr = self._deq_ptr + 1

    async def wait_cycle(self,cycle=0):
        await self.env.enq_agent.bundle.step(cycle)

    def init_dut(self):
        self.env.enq_agent.init_dut()
    def gen_fu(self,size,exception = -1):
        inst_list = []
        for i in range(size):
            inst = Rob_Instr()
            inst.enq_instr()

            inst.robIdx_value = self.rob_idx
            if i == 0:
                inst.firstUop = 1
                inst.exception = exception
                self.add_enqptr(inst.numWB)
            elif i == size -1:
                inst.firstUop = 0
                inst.lastUop = 1
            else:
                inst.firstUop = 0
                inst.lastUop = 0
            self.inst_list.append(inst)

        return inst_list

    def gen_inst(self,itype = "",invalid = "",exception = 0):
        inst_list = []
        if(itype == ""):
            #isfu = random.choices([0,1], [0.9,0.1])[0]
            isfu = 0
            if isfu:
                fu_size = random.randint(2,16)
                inst_list = self.gen_fu(fu_size)
            else:
                inst = Rob_Instr()
                inst.enq_inst("")
                inst.robIdx_value = self.rob_idx
                #gen_snapshot(inst)
                inst_list.append(inst)
        elif(itype == "ldu" or itype == "stu" or itype == "move"):
            instr.enq_instr(itype)
            self.add_robidx

        elif(invalid == "invalid"):
            instr = Rob_Instr()
            instr.enq_instr("")
            instr.valid = 0
            instr.robIdx_value = self.rob_idx
            self.inst_list.append(instr)
        else:
            instr = Rob_Instr()
            inst.enq_inst("csr")

        if inst_list:
            return inst_list

    async def enq_single_instr(self,env,instr):
        instr.robIdx_value = self.rob_idx
        await env.enq_agent.enqueue_instr(0,instr)
        self.rob_idx  += 1

    # 随机入队size条指令
    async def random_enq_inst(self, size, hasexception = 0):

        send_list = []
        exception_inst = random.randint(0,size)
        for i in range(size):
            if hasexception and i == exception_inst:
                inst = self.gen_inst()[0]
            else:
                inst = self.gen_inst()[0]

            send_list.append(inst)
            self.add_robidx()

        sub_lists = [send_list[i:i+6] for i in range(0, len(send_list), 6)]
        for sub_list in sub_lists:
            await self.env.enq_agent.enq_list(sub_list)

        #self.inst_list = []

    # 根据指令流入对指令
    async def enq_inst(self, inst_list):

        send_list = []
        if type (inst_list) == type(""):
            inst = Rob_Instr()
            inst.enq_inst()
            inst.robIdx_value = self.rob_idx
            send_list.append(inst)
            self.add_robidx()
        elif type(inst_list[0]) == type(""):
            for item in inst_list:
                if item == "invalid":
                    inst = self.gen_inst("","invalid")[0]
                else:
                    inst = self.gen_inst(item,"")[0]
                send_list.append(inst)

        else:
            for item in self.inst_list:
                #print("this is enq",item.robIdx_value,item.exception)
                if item.valid == 1 and item.firstUop == 1:
                    self.add_enqptr(item.numWB)

        await self.env.enq_agent.enq_list(send_list)



    def gen_writeback_info(self,env,rob_idx,nums = -1,hasexception = 0):
        #futype = getattr(self.env.internal.bundle.entry,f"index{rob_idx}").debug_fuType

        fuOptype = 16
        writeback = Rob_Writeback()
        if nums == 0:
            # nums = real_nums = getattr(self.env.internal.bundle.entry,f"index{rob_idx}").uopNum.value
            nums = 2
        writeback.writeback_instr(0,rob_idx,fuOptype,nums,hasexception,0)
        return writeback

    async def wb_inst(self,wb_list,wait = 0,nums = 0, hasexception  = 1):
        """writeback inst stream
        args:
            wb_list: size or inst_stream like 5 or [1,3,4]
            wait: wait some cycle then writeback
            nums: inst uopNum
        """
        writeback_list = []
        #await self.env.wb_agent.bundle.step(wait)
        if type(wb_list) == type(0):
            for i in range(wb_list):
                writeback = self.gen_writeback_info(i,nums,hasexception)
                writeback_list.append(writeback)
        else:
            if type(wb_list[0]) == type(0):
                for item in wb_list:
                    writeback = self.gen_writeback_info(item,nums,0)
                    writeback_list.append(writeback)
                    self.add_deqptr()
            else:
                writeback_list = wb_list
                for _ in range(len(writeback_list)):
                    self.add_deqptr()

        await self.env.wb_agent.writeback_list(writeback_list)
        #await self.env.enq_agent.bundle.step(1)

        writeback_list = []

# #======================================= redirect ====================================================
    async def redirect(self,cycle = 0,rtype=0, rob_idx = 0,useSnpt=0):
        await self.wait_cycle(cycle)
        if rob_idx == 0:
            rob_idx = random.randint(0,self.env.internal.bundle.enq_ptr.value.value)
        await self.env.enq_agent.rob_redirect(1,1,rob_idx,rtype,useSnpt)

        await self.wait_cycle(1)
