import random

from env.rob_wrapper import *
from toffee import *
from .gen_base import GenBase

class GenWalk():
    def __init__(self,gen = None):
        self.gen = gen

    async def gen_isflush_self(self,isflush):


        enq_size = random.randint(2,160)
        await self.gen.random_enq_inst(enq_size)
        deq_size = random.randint(1,enq_size - 1)
        await self.gen.wb_inst(enq_size)

        redirectid = random.randint(deq_size,enq_size)
        if isflush == 0:
            await self.gen.redirect(0,0,redirectid,0)
        else:
            await self.gen.redirect(0,1,redirectid,0)

    async def gen_redirect(self,isenqdeq,hassnap,usesnap):
        
        if isenqdeq :
            enq_size = random.randint(2,160)
            await self.gen.random_enq_inst(enq_size)
            deq_size = random.randint(1,enq_size - 1)
            await self.gen.wb_inst(enq_size)
        else: 
            enq_size = random.randint(2,160)
            await self.gen.random_enq_inst(enq_size)
            deq_size = random.randint(1,enq_size - 1)
            await self.gen.wb_inst(enq_size)

        redirectid = random.randint(deq_size,enq_size)
        await self.gen.redirect(0,0,redirectid,usesnap)



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

    async def gen_canot_commit(self):

        enq_size = random.randint(1,10)
        await self.gen.random_enq_inst(enq_size)
        await self.gen.wb_inst(enq_size)

    async def gen_line_isall_commit(self,type):

        enq_size = random.randint(1,10)
        await self.gen.random_enq_inst(enq_size)
        await self.gen.wb_inst(enq_size)