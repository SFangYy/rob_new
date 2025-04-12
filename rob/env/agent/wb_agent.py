
from ..rob_wrapper import *
from queue import Queue
from toffee import *
class WritebackAgent(Agent):
    def __init__(self,bundle):
        super().__init__(bundle)
        self.bundle = bundle
        self.line = 0

    def commit_assert(self,line):
        def deqgroup_assert():
            if getattr(self.bundle.entry,f"index{0}").ftqIdx_value.value == self.bundle.deqgroup.ftqIdx_value.value:
                return True
            else:
                return True
        if line == self.bundle.line.robIdxThisLine_0.value:
            #print(getattr(self.bundle.entry,f"index{0}").ftqIdx_value.value,self.bundle.deqgroup.ftqIdx_value.value)
            if(self.line == 0 and self.line != self.bundle.line.robIdxThisLine_0.value):
                if deqgroup_assert():
                    return True
                else:
                    return False
                #print(getattr(self.bundle.entry,f"index{0}").ftqIdx_value.value,self.bundle.deqgroup.ftqIdx_value.value)
                self.line = self.bundle.line.robIdxThisLine_0.value

            return True
        else:
            return False
    async def enqueue_control(self,redirect_valid):
        self.bundle.redirect.valid.value = redirect_valid

    async def redirect_instr(self,valid, robIdx_value, level):
        self.bundle.redirect.valid.value = valid
        self.bundle.redirect.bits_robIdx_flag.value = 1
        self.bundle.redirect.bits_robIdx_value.value = robIdx_value
        self.bundle.redirect.bits_level.value = level

    @driver_method()
    async def writeback(self,channel,writeback_instr):

        if channel != None:
            result = self.bundle.writeback[channel]
            if (19 <= channel and channel <=25):
                result.valid.value = writeback_instr.valid
            result.bits_robIdx_value.value = writeback_instr.robIdx_value
            if channel in [5,14,15,19,20,21,22,23,24,25]:
                if(writeback_instr.exception != -1):
                    exception_channel = getattr(result,f"bits_exceptionVec_{writeback_instr.exception}")
                    exception_channel.value = 1
            if(0 <= channel and channel <=25):
                result_num = self.bundle.writeback_nums[channel]
                result_num.bits.value = writeback_instr.nums

            if(channel<=25 and channel >=14):
                #result.bits_data_0.value = writeback_instr.data
                result.bits_robIdx_flag.value = writeback_instr.robIdx_flag
            if(channel<=25 and channel >=21):
                result.bits_flushPipe.value = writeback_instr.flushPipe

    #@driver_method()
    async def writeback_list(self,writeback_list):
        for wb_info in writeback_list:
            await self.writeback(wb_info.channel,wb_info)
        # await self.bundle.step(1)
        # for inst in writeback_list:
        #     await self.reset_writeback(inst.channel,instr)


    async def reset_writeback(self,channel,writeback_instr):
        if channel != None:
            result = self.bundle.writeback[channel]
            result.bits_robIdx_value.value = 0
            result.valid.value = 0
            if(0 <= channel and channel <=25):
                result_num = self.bundle.writeback_nums[channel]
                result_num.bits.value = 0
            if channel in [5,14,15,19,20,21,22,23,24,25]:
                if(writeback_instr.exception != -1):
                    exception_channel = getattr(result,f"bits_exceptionVec_{writeback_instr.exception}")
                    exception_channel.value = 0


    async def control_commit(self,isCommit,iswalk,commitvalid,walkValid):
        def get_valid_i(self, idx, valid):
            if(idx&valid):
                return 1
            else:
                return 0
        def valid_i(valid):
            for i in range(len(valid)):
                self.bundle.commits.commitValid_i = get_valid_i(bin(i), valid)
        valid_i(commitvalid)
        valid_i(walkValid)
        self.bundle.commits.isWalk = iswalk
        self.bundle.commits.isCommit = isCommit

