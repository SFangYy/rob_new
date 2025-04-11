import random 

from ..rob_wrapper import *
from toffee import Executor
import toffee 
from gen.gen_base import GenBase

class gen_enq():
    def __init__(self,env = None):
        self.rob_idx = 0
        self.gen = gen_base(env)
        self.env = env

    async def wait_cycle(self,cycle=0):
        await self.env.enq_agent.bundle.step(cycle)

    async def gen_invalid_instr(self,invalid="",exception = ""):
        invalid_type = ["not_first","invalid"]
        for i in range(16):
            for j in range(0,i):
                await self.gen.gen_enq_inst_list(j)
                invalid_num = random.randint(0,5)
                instr_list = []
                for i in range(invalid_num):
                    instr = self.gen.gen_instr("")
                    instr_list.append(instr)
                instr = self.gen.gen_instr("",random.choice(invalid_type))
                instr_list.append(instr)
                await self.gen.enq_inst_list(instr_list)
                await self.gen.gen_enq_inst_list(i)
                await self.wait_cycle(1)
                assert(i+j+invalid_num == self.env.internal.bundle.enq_ptr.value.value)
                await self.wait_cycle(10)
                self.env.enq_agent.bundle.set_all(0)
                await self.env.enq_agent.init_dut()

    async def gen_rob_not_enough(self):
        
        await self.gen.gen_enq_inst_list(156)
        enq_num = random.randint(1,10)
        await self.gen.gen_enq_inst_list(enq_num)
        await self.wait_cycle(3)
        assert(156 == self.env.internal.bundle.enq_ptr.value.value)

        await self.wait_cycle(10)
        self.env.enq_agent.bundle.set_all(0)
        await self.env.enq_agent.init_dut()