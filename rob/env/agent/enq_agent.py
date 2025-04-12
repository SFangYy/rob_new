from toffee.agent import Agent
from ..bundle import EnqTagSuffix #,RobBundle
#from env.rob_wrapper import *
class EnqAgent(Agent):
    def __init__(self, bundle):
        super().__init__(bundle)
        self.bundle = bundle



    # #@driver_method()
    # async def init_dut(self):
    #     self.bundle.control.reset.value = 1
    #     await self.bundle.step(2)
    #     self.bundle.set_all(0)
    #     self.bundle.control.reset.value = 0
    #     await self.bundle.step(1)


    """ new enq port
    input          io_enq_req_0_valid,
    input  [31:0]  io_enq_req_0_bits_instr,
    input  [40:0]  io_enq_req_0_bits_pc,
    input          io_enq_req_0_bits_exceptionVec_0,
    input          io_enq_req_0_bits_exceptionVec_1,
    input          io_enq_req_0_bits_exceptionVec_2,
    input          io_enq_req_0_bits_exceptionVec_12,
    input          io_enq_req_0_bits_exceptionVec_20,
    input          io_enq_req_0_bits_exceptionVec_22,
    input          io_enq_req_0_bits_hasException,
    input          io_enq_req_0_bits_trigger_frontendCanFire_0,
    input          io_enq_req_0_bits_trigger_frontendCanFire_1,
    input          io_enq_req_0_bits_trigger_frontendCanFire_2,
    input          io_enq_req_0_bits_trigger_frontendCanFire_3,
    input          io_enq_req_0_bits_preDecodeInfo_isRVC,
    input          io_enq_req_0_bits_crossPageIPFFix,
    input          io_enq_req_0_bits_ftqPtr_flag,
    input  [5:0]   io_enq_req_0_bits_ftqPtr_value,
    input  [3:0]   io_enq_req_0_bits_ftqOffset,
    input  [5:0]   io_enq_req_0_bits_ldest,
    input  [34:0]  io_enq_req_0_bits_fuType,
    input  [8:0]   io_enq_req_0_bits_fuOpType,
    input          io_enq_req_0_bits_rfWen,
    input          io_enq_req_0_bits_fpWen,
    input          io_enq_req_0_bits_vecWen,
    input          io_enq_req_0_bits_v0Wen,
    input          io_enq_req_0_bits_vlWen,
    input          io_enq_req_0_bits_isXSTrap,
    input          io_enq_req_0_bits_waitForward,
    input          io_enq_req_0_bits_blockBackward,
    input          io_enq_req_0_bits_flushPipe,
    input          io_enq_req_0_bits_vpu_vill,
    input          io_enq_req_0_bits_vpu_vma,
    input          io_enq_req_0_bits_vpu_vta,
    input  [1:0]   io_enq_req_0_bits_vpu_vsew,
    input  [2:0]   io_enq_req_0_bits_vpu_vlmul,
    input          io_enq_req_0_bits_vpu_specVill,
    input          io_enq_req_0_bits_vpu_specVma,
    input          io_enq_req_0_bits_vpu_specVta,
    input  [1:0]   io_enq_req_0_bits_vpu_specVsew,
    input  [2:0]   io_enq_req_0_bits_vpu_specVlmul,
    input          io_enq_req_0_bits_vlsInstr,
    input          io_enq_req_0_bits_wfflags,
    input          io_enq_req_0_bits_isMove,
    input          io_enq_req_0_bits_isVset,
    input          io_enq_req_0_bits_firstUop,
    input          io_enq_req_0_bits_lastUop,
    input  [6:0]   io_enq_req_0_bits_numWB,
    input  [2:0]   io_enq_req_0_bits_commitType,
    input  [7:0]   io_enq_req_0_bits_pdest,
    input          io_enq_req_0_bits_robIdx_flag,
    input  [7:0]   io_enq_req_0_bits_robIdx_value,
    input  [2:0]   io_enq_req_0_bits_instrSize,
    input          io_enq_req_0_bits_dirtyFs,
    input          io_enq_req_0_bits_dirtyVs,
    input          io_enq_req_0_bits_eliminatedMove,
    input          io_enq_req_0_bits_snapshot,
    input          io_enq_req_0_bits_loadWaitBit,
    input          io_enq_req_0_bits_singleStep,

    """
    async def enqueue_instr(self,req_idx,instr):
        def select_req(i):
            func_map = {
                0:self.bundle.enq.req_0,
                1:self.bundle.enq.req_1,
                2:self.bundle.enq.req_2,
                3:self.bundle.enq.req_3,
                4:self.bundle.enq.req_4,
                5:self.bundle.enq.req_5,
            }
            if i in func_map:
                return func_map[i]
            else:
                print(f"No req function associated with {i}")
                return None
        result = select_req(req_idx)
        if instr.exception != 0:
            exception = getattr(result,f"exceptionVec_{instr.exception}")
            exception.value = 1
        result.valid.value = instr.valid
        #result.bits_instr.value = instr.instr
        #result.bits_pc.value = instr.pc
        #result.bits_trigger_frontendCanFire_0.value = instr.frontendCanFire
        #result.bits_trigger_frontendHit_0.value = instr.frontendHit
        result.bits_isMove.value = instr.isMove
        result.bits_ftqPtr_flag.value = instr.ftqPtr_flag
        result.bits_ftqPtr_value.value = instr.ftqPtr_value
        result.bits_ftqOffset.value = instr.ftqOffset
        result.bits_ldest.value = instr.ldest
        result.bits_exceptionVec_0.value =0
        result.bits_fuType.value = instr.fuType
        result.bits_fuOpType.value = instr.fuOpType
        result.bits_waitForward.value = instr.waitForward
        result.bits_blockBackward.value = instr.blockBackward
        result.bits_firstUop.value = instr.firstUop
        result.bits_lastUop.value = instr.lastUop
        result.bits_robIdx_flag.value = instr.robIdx_flag
        result.bits_robIdx_value.value = instr.robIdx_value
        result.bits_fpWen.value = instr.fpWen
        result.bits_rfWen.value = instr.rfWen
        result.bits_vecWen.value = instr.vecWen
        result.bits_v0Wen.value = instr.v0Wen
        result.bits_vlWen.value = instr.vlWen
        result.bits_isXSTrap.value = instr.isXSTrap
        result.bits_flushPipe.value = instr.flushPipe
        result.bits_vpu_vill.value = instr.vpu_vill
        result.bits_vpu_vma.value = instr.vpu_vma
        result.bits_vpu_vta.value = instr.vpu_vta
        result.bits_preDecodeInfo_isRVC = instr.isRVC
        result.bits_vpu_vsew.value = instr.vpu_vsew
        result.bits_vpu_vlmul.value = instr.vpu_vlmul
        result.bits_vlsInstr.value = instr.vlsInstr
        result.bits_wfflags.value = instr.wfflags
        result.bits_isMove.value = instr.isMove
        result.bits_isVset.value = instr.isVset
        result.bits_numWB.value = instr.numWB
        result.bits_commitType.value = instr.commitType
        result.bits_pdest.value = instr.pdest
        result.bits_instrSize.value = instr.instrSize
        result.bits_dirtyVs.value = instr.dirtyVs
        result.bits_dirtyFs.value = instr.dirtyFs
        #result.bits_eliminatedMove.value = instr.eliminatedMove
        #result.bits_snapshot.value = 0
        result.bits_loadWaitBit.value = instr.loadWaitBit
        #result.bits_singleStep.value = instr.singleStep
        #result.bits_debug_fuType.value = instr.debug_fuType
        result.bits_numWB.value = instr.numWB
        result.bits_pdest.value = instr.pdest
        if(req_idx == 0 and instr.snapshot == 1):
            result.bits_snapshot.value = 1

        elif req_idx == 0 and instr.snapshot == 0:
            result.bits_snapshot.value = 0

        if(instr.flushpipe == 1):
            result.bits_flushPipe.value = 1
            result.valid.value = 0


    # @driver_method()
    async def enq_list(self,instr_list):
        idx_1 = 0
        for instr in instr_list:
            await self.enqueue_instr(idx_1,instr)
            idx_1 = idx_1+1

        #await self.bundle.step(1)


    async def reset_enq(self):
        instr = Rob_Instr()
        instr.valid = 0
        instr.robIdx_value = 0
        for i in range(6):
            await self.enqueue_instr(i,instr)
        #await self.bundle.step(1)
        #return self.bundle.enq_ptr.ptrVec.value.value
        #print("dut is ",self.bundle.enq_ptr.ptrVec.value.value)

    # @driver_method()
    async def rob_redirect(self,valid,idx_flag,idx_value,level,useSnpt=0):
        self.bundle.redirect.valid.value = valid
        self.bundle.redirect.bits_robIdx_flag.value = 0
        self.bundle.redirect.bits_robIdx_value.value = idx_value
        self.bundle.redirect.bits_level.value = level
        self.bundle.snpt.useSnpt.value = useSnpt

    # async def enq_debug(self,channel,debug_info):
    #     self.bundle.debugEnqLsq.canAccept.value = 1
    #     getattr(self.bundle.debugEnqLsq,f"needAlloc_{channel}").value = 1
    #     getattr(self.bundle.debugEnqLsq, f"req_{channel}_bits_robIdx_value").value = debug_info.robIdx

    #     getattr(self.bundle.debugEnqLsq, f"req_{channel}_valid").value = debug_info.valid

    #     getattr(self.bundle.debugEnqLsq, f"req_{channel}_bits_lqIdx_value").value = debug_info.lqIdx
    #     await self.bundle.step(1)

    # async def enq_lsDown(self,channel,robIdx):
    #     #self.bundle.debugEnqLsq.canAccept.value = 1
    #     getattr(self.bundle.lsTopDownInfo,f"{channel}_s1_robIdx").value = robIdx
    #     getattr(self.bundle.lsTopDownInfo,f"{channel}_s1_vaddr_valid").value = 1
    #     getattr(self.bundle.lsTopDownInfo,f"{channel}_s1_vaddr_bits").value = robIdx

    #     getattr(self.bundle.lsTopDownInfo,f"{channel}_s2_robIdx").value = robIdx
    #     getattr(self.bundle.lsTopDownInfo,f"{channel}_s2_paddr_valid").value = 1
    #     getattr(self.bundle.lsTopDownInfo,f"{channel}_s2_paddr_bits").value = robIdx
    #     await self.bundle.step(1)

