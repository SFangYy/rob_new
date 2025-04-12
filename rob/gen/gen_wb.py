import random

from env.rob_wrapper import *
from toffee import *
from .gen_base import GenBase

class GenWb():
    def __init__(self,gen = None):
        self.gen = gen

    async def gen_wb_incycle(self,incycle):

        enq_size = random.randint(1,10)
        await self.gen.random_enq_inst(enq_size)
        if incycle == 1:
            await self.gen.wb_inst(enq_size,1,0)
        else:
            await self.gen.wb_inst(enq_size,1,1)


    async def gen_wb_special_inst(self):

        enq_size = random.randint(1,10)
        await self.gen.random_enq_inst(enq_size)
        await self.gen.wb_inst(enq_size)

    async def gen_wb_not_old_inst(self):
        #enq_size = random.randint(1,10)
        enq_size = random.randint(1,10)

        await self.gen.random_enq_inst(enq_size)
        self.gen.enqptr += enq_size
        wb_inst = random.randint(self.gen.deqptr + 1,self.gen.enqptr)
        await self.gen.wb_inst([wb_inst])
        self.gen.deqptr + 1

    async def gen_canot_commit(self):
        
        enq_size = random.choice([num for num in range(1,160) if num %8 !=0 ])
        await self.gen.random_enq_inst(enq_size)
        await self.gen.wb_inst(enq_size)

    async def gen_line_isall_commit(self,isall):
        
        if isall == 0:
            enq_size = random.choice([num for num in range(1,160) if num %8 !=0 ])
        else:
            enq_size = random.choice([num for num in range(1,160) if num %8 ==0 ])
        await self.gen.random_enq_inst(enq_size)
        await self.gen.wb_inst(enq_size)

    async def gen_wb_with_exception(self):

        enq_size = random.randint(1,10)
        await self.gen.random_enq_inst(enq_size)
        await self.gen.wb_inst(enq_size,1)