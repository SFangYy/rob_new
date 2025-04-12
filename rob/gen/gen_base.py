import random

from env.rob_wrapper import *
from toffee import Executor
import toffee

class GenBase():
    def __init__(self,env):
        self.env = env
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

    def gen_inst(self,itype = "",invalid = "",exception = -1):
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
    async def random_enq_inst(self, size):

        send_list = []
        for i in range(size):
            inst = self.gen_inst()[0]

            send_list.append(inst)
            self.add_robidx()

        sub_lists = [send_list[i:i+6] for i in range(0, len(send_list), 6)]
        for sub_list in sub_lists:
            await self.env.enq_agent.enq_list(sub_list)

        #self.inst_list = []

    # 根据指令流入对指令
    async def enq_inst(self, inst_list):
        
        send_list
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
        #real_nums = getattr(self.env.internal.bundle.entry,f"index{rob_idx}").uopNum.value

        # if nums == -1 or real_nums == 0 or (real_nums - nums < 0):
        #     nums = real_nums
        fuOptype = 16
        writeback = Rob_Writeback()
        writeback.writeback_instr(0,rob_idx,fuOptype,nums,hasexception,0)
        return writeback

    async def wb_inst(self,wb_list,wait = 0,nums = 0):
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
                writeback = self.gen_writeback_info(i,nums,0)
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

    # async def gen_enq_inst_list(self,entry_size,snapshot = 0,exception = 0,type = 0):
    #     origin_num = snapshot

    #     snapshot_list = []
    #     if snapshot < entry_size and snapshot !=0 :
    #         snapshot_list = random_numbers = random.sample(range(1, entry_size), snapshot)
    #     exception_list = []
    #     if exception != 0:
    #         exception_list = random.sample(range(self.enq_ptr + 1, self.enq_ptr + entry_size), exception)

    #     async def send_enq(size,snapshot):
    #         count = 0
    #         inst_list = []
    #         for _ in range(size):
    #             if self.rob_idx in exception_list:
    #                 self.gen_instr("","",random.choice(self.enq_exception_list))
    #             else:
    #                 self.gen_instr()

    #         # if len(self.inst_list) != 0:
    #         #     await self.enq_inst_list(self.inst_list)

    #     await send_enq(entry_size,0)

    #     inst_list = self.inst_list
    #     self.inst_list = []
    #     return inst_list

    # def gen_instr(self,itype = "",invalid = "",exception = ""):
    #     instr = Rob_Instr()
    #     if(itype == ""):
    #         instr.enq_instr()
    #     elif(itype == "ldu" or itype == "stu" or itype == "move"):
    #         instr.enq_instr(0,itype)
    #     if(invalid == "not_first"):
    #         instr.firstUop = 0
    #     elif(invalid == "invalid"):
    #         instr.valid = 0
    #     if(exception == 0):
    #         instr.gen_exception(0)
    #     return instr

    # async def enq_inst_list(self, inst_list):
    #     send_list = []

    #     if type (inst_list) == type(""):
    #         inst = Rob_Instr()
    #         inst.enq_instr(2,inst_list)
    #         inst.robIdx_value = self.rob_idx
    #         self.add_robidx()
    #         send_list.append(inst)
    #     elif type (inst_list) == type(0):
    #         for i in range(inst_list):
    #             inst = Rob_Instr()
    #             inst.enq_instr(2)
    #             inst.robIdx_value = self.rob_idx
    #             send_list.append(inst)
    #             check_full()
    #             self.add_robidx()
    #     elif type(inst_list[0]) == type(""):
    #         for item in inst_list:
    #             inst = Rob_Instr()
    #             if(item == ""):
    #                 inst.enq_instr(2)
    #             else:
    #                 inst.enq_instr(2,item)
    #             send_list.append(inst)
    #             inst.robIdx_value = self.rob_idx
    #             check_full()
    #             self.add_robidx()
    #     else:
    #         for item in inst_list:
    #             if item.valid == 1 and item.firstUop == 1:
    #                 item.robIdx_value = self.rob_idx
    #                 self.add_robidx()
    #                 self.add_enqptr()

    #     async with Executor(exit = "none") as exec:
    #         exec(self.env.enq_agent.enq_list(inst_list), sche_order="dut_first")
    #     await self.env.enq_agent.bundle.step(1)

    #     send_list = []

#     async def gen_enq_inst_list(self,entry_num,snapshot = 0):
#         origin_num = snapshot
#         snapshot_list = []
#         if snapshot < entry_num and snapshot !=0 :
#             snapshot_list = random_numbers = random.sample(range(1, entry_num), snapshot)
#         async def send_enq(count,snapshot,snapshot_list = []):
#             i = 0
#             while i <= count - 1:
#                 enq_num = random.randint(0,6)
#                 enq_index = random.sample(range(0,6),enq_num)
#                 inst_list = []
#                 if snapshot != 0 and snapshot_list:
#                     if i + enq_num >= snapshot_list[origin_num - snapshot]:
#                         await self.gen_snapshot()
#                         i += 1
#                         snapshot -= 1
#                         continue
#                 for j in range(6):
#                     if (i <= count -1):
#                         inst = Rob_Instr()
#                         if j in enq_index:
#                             inst.enq_instr(2)
#                             inst_list.append(inst)
#                             i += 1
#                         else:
#                             inst_list.append(inst)
#                     else:
#                         i += 1
#                         break
#                 if len(inst_list) != 0:
#                     await self.enq_inst_list(inst_list)

#         if(entry_num <= 150):
#             await send_enq(entry_num,snapshot,snapshot_list)

#         else:
#             await send_enq(150,snapshot,snapshot_list)
#             inst_list = []
#             for i in range(entry_num - 150):
#                 inst = Rob_Instr()
#                 inst.robIdx_value = i+150
#                 inst.enq_instr(2)
#                 inst_list.append(inst)
#             await self.enq_inst_list(inst_list)
#         return snapshot_list

#     async def gen_enq_with_wait(self,entry_num,snapshot = 0):
#         """
#         random enq inst
#         """
#         async def send_enq():
#             i = 0
#             while (i <= 2000):
#                 enq_num = random.randint(0,6)
#                 enq_index = random.sample(range(0,6),enq_num)
#                 inst_list = []
#                 for j in range(6):
#                     if (abs(self.enq_ptr - self.deq_ptr) + enq_num <= 156):
#                         inst = Rob_Instr()
#                         if j in enq_index:
#                             inst.enq_instr(2)
#                             inst_list.append(inst)
#                             i += 1
#                         else:
#                             inst_list.append(inst)
#                     else:
#                         while(1):
#                             await self.wait_cycle(5)
#                             deq_ptr = self.env.internal.bundle.deq_ptr.value.value
#                             i += 1
#                             if (abs(self.enq_ptr - deq_ptr) +enq_num <= 156 or i > 100):
#                                 break

#                 if len(inst_list) != 0:
#                     await self.enq_inst_list(inst_list)

#         await send_enq()

#     async def gen_snapshot(self):
#         instr = Rob_Instr()
#         instr.enq_instr(2)
#         instr.snapshot = 1
#         enq_list = []
#         enq_list.append(instr)
#         await self.enq_inst_list(enq_list)
# #==================================== wb_list =====================================================



#     async def random_writeback(self,end_ptr,wb_nums = -1):
#         i = 0
#         wb_list = []

#         while(self.env.internal.bundle.deq_ptr.value.value < end_ptr):
#             if(i > 100):
#                 break
#             i += 1
#             await self.env.wb_agent.bundle.step(3)
#             for item in wb_list:
#                 if getattr(self.env.internal.bundle.entry,f"index{item}").uopNum.value == 0:
#                     self.can_wb[item] = False

#             start_ptr = self.env.internal.bundle.deq_ptr.value.value
#             available_indices = [i for i in range(len(self.can_wb)) if self.can_wb[i]]

#             wb_count =random.randint(1,10)

#             available_indices = [i for i in available_indices if 0 <= i <= end_ptr]
#             if len(available_indices) <= wb_count:
#                 wb_list = available_indices
#             else:
#                 wb_list = random.sample(available_indices,wb_count)
#             #print(wb_list)
#             if wb_list:
#                 await self.wb_list(wb_list,2,wb_nums)
#         self.deq_ptr = end_ptr

#     async def random_writeback_wait(self,end_ptr,wb_nums = -1):
#         i = 0
#         wb_list = []
#         await self.wait_cycle(20)
#         def check_empty():
#             if self.enq_ptr_flag == self.deq_ptr_flag and self.deq_ptr == self.enq_ptr:
#                 return False
#             else:
#                 return True
#         while(True):
#             if(i > 500):
#                 break
#             if(not check_empty()):
#                 await self.wait_cycle(10)
#             i += 1
#             await self.env.wb_agent.bundle.step(3)
#             for item in wb_list:
#                 if getattr(self.env.internal.bundle.entry,f"index{item}").uopNum.value == 0:
#                     self.can_wb[item] = False

#             start_ptr = self.env.internal.bundle.deq_ptr.value.value
#             available_indices = [i for i in range(len(self.can_wb)) if self.can_wb[i]]
#             wb_count =random.randint(1,10)
#             end_ptr = self.enq_ptr if self.enq_ptr_flag == self.deq_ptr_flag else 159
#             available_indices = [i for i in available_indices if 0 <= i <= end_ptr]

#             if len(available_indices) <= wb_count:
#                 wb_list = available_indices
#             else:
#                 wb_list = random.sample(available_indices,wb_count)
#             if wb_list:
#                 await self.wb_list(wb_list,2,wb_nums)


# #======================================= redirect ====================================================
#     async def redirect(self,cycle = 0,rtype=0, rob_idx = 0,useSnpt=0):
#         await self.wait_cycle(cycle)
#         if rob_idx == 0:
#             rob_idx = random.randint(0,self.env.internal.bundle.enq_ptr.value.value)
#         await self.env.enq_agent.rob_redirect(1,1,rob_idx,rtype,useSnpt)

#         await self.wait_cycle(1)

#         async with Executor() as exec:
#             exec(self.env.enq_agent.rob_redirect(0,1,rob_idx,rtype,useSnpt))
#             #exec(self.assert_redirect(rob_idx,rtype,0))


#     async def gen_redirect(self,env,rtype):
#         async with Executor() as exec:
#             exec(self.enq_gen.full_enq_instr(self.env))
#             exec(self.redirect(env,10,rtype))
