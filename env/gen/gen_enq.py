import random 

from ..rob_wrapper import *
from toffee import Executor
import toffee 
from .gen_base import GenBase

class GenEnq():
    def __init__(self,gen = None):
        self.rob_idx = 0
        self.gen = gen
        #self.env = env


    async def gen_invalid_instr(self,invalid="",exception = ""):
        invalid_type = ["not_first","invalid"]

        enq_inst_size = random.randint(1,159)
        await self.gen.random_enq_inst(enq_inst_size)

        invalid_size = random.randint(0,5)
        inst_list = []

        for i in range(invalid_size):
            inst = self.gen.gen_inst("",random.choice(invalid_type))
            inst_list.append(instr)
            await self.gen.enq_inst_list(inst_list)
            await self.gen.enq_inst_list(i)
            await self.gen.wait_cycle(1)
            #assert(i+j+invalid_num == self.env.internal.bundle.enq_ptr.value.value)


    async def gen_rob_not_enough(self):
        
        await self.gen.wb_inst([1,2,3],2,0)
        await self.gen.random_enq_inst(156)
        enq_num = random.randint(1,10)
        #await self.gen.gen_enq_inst_list(enq_num)
        #await self.gen.wait_cycle(3)
        #assert(156 == self.env.internal.bundle.enq_ptr.value.value)
