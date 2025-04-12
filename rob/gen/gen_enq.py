import random

from env.rob_wrapper import *
from toffee import *
from .gen_base import GenBase

class GenEnq():
    def __init__(self,gen = None):
        self.rob_idx = 0
        self.gen = gen
        #self.env = env


    async def gen_invalid(self,type = ""):
        invalid_type = ["not_first","invalid"]

        enq_inst_size = random.randint(1,159)
        await self.gen.random_enq_inst(enq_inst_size)

        invalid_size = random.randint(0,5)
        inst_list = []

        for i in range(invalid_size):
            inst = self.gen.gen_inst("",random.choice(invalid_type))
            inst_list.append(inst)
            await self.gen.enq_inst_list(inst_list)
            await self.gen.wait_cycle(1)
            #assert(i+j+invalid_num == self.env.internal.bundle.enq_ptr.value.value)


    async def gen_rob_not_enough(self):

        #await self.gen.wb_inst([1,2,3],2,0)
        await self.gen.random_enq_inst(156)
        for i in range(4):
            await self.gen.random_enq_inst(1)
            
        #enq_num = random.randint(1,10)
        #await self.gen.gen_enq_inst_list(enq_num)
        #await self.gen.wait_cycle(3)

    async def gen_rab_not_enough(self):

        #await self.gen.wb_inst([1,2,3],2,0)
        await self.gen.random_enq_inst(156)
        for i in range(4):
            await self.gen.random_enq_inst(1)

    async def gen_enq_inst(self):

        enq_size = random.randint(1,10)
        await self.gen.random_enq_inst(enq_size)
        await self.gen.wb_inst(enq_size)


    async def gen_special_inst(self):

        enq_size = random.randint(1,10)
        await self.gen.random_enq_inst(enq_size)
        await self.gen.wb_inst(enq_size)

    async def gen_enqflag_reverse(self):
        #enq_size = random.randint(1,10)
        await self.gen.random_enq_inst(156)
        await self.gen.wb_inst(20)
        await self.gen.random_enq_inst(4)
        await self.gen.random_enq_inst(156)
        await self.gen.random_enq_inst(4)

    async def gen_rob_empty(self):

        enq_size = random.randint(1,10)
        await self.gen.random_enq_inst(enq_size)
        await self.gen.wb_inst(enq_size)

    async def gen_enq_with_exception(self):

        enq_size = random.randint(1,10)
        await self.gen.random_enq_inst(enq_size,1)
        await self.gen.wb_inst(enq_size)