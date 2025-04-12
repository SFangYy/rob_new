from toffee import *

class EnqTagSuffix(Bundle):
    tage_enable, sc_enable = Signals(2)

class ControlBundle(Bundle):
    reset, clock, canAccept, isEmpty = Signals(4)

class RedirectBundle(Bundle):
    bits_level, bits_robIdx_flag, bits_robIdx_value, valid = Signals(4)

class SnptBundle(Bundle):
    flushVec_0, flushVec_1, flushVec_2, flushVec_3, snptDeq, snptSelect, useSnpt = Signals(7)

class EnqReqBundle(Bundle):
    bits_blockBackward, bits_commitType, bits_crossPageIPFFix, bits_dirtyFs, bits_dirtyVs, bits_eliminatedMove, \
    bits_exceptionVec_0, bits_exceptionVec_1, bits_exceptionVec_12, bits_exceptionVec_2, bits_exceptionVec_20, \
    bits_exceptionVec_22, bits_firstUop, bits_flushPipe, bits_fpWen, bits_ftqOffset, bits_ftqPtr_flag, \
    bits_ftqPtr_value, bits_fuOpType, bits_fuType, bits_hasException, bits_instr, bits_instrSize, bits_isMove, \
    bits_isVset, bits_isXSTrap, bits_lastUop, bits_ldest, bits_loadWaitBit, bits_numWB, bits_pc, bits_pdest, \
    bits_preDecodeInfo_isRVC, bits_rfWen, bits_robIdx_flag, bits_robIdx_value, bits_singleStep, bits_snapshot, \
    bits_trigger_frontendCanFire_0, bits_trigger_frontendCanFire_1, bits_trigger_frontendCanFire_2, \
    bits_trigger_frontendCanFire_3, bits_trigger_frontendHit_0, bits_trigger_frontendHit_1, \
    bits_trigger_frontendHit_2, bits_trigger_frontendHit_3, bits_v0Wen, bits_vecWen, bits_vlWen, bits_vlsInstr, \
    bits_vpu_specVill, bits_vpu_specVlmul, bits_vpu_specVma, bits_vpu_specVsew, bits_vpu_specVta, bits_vpu_vill, \
    bits_vpu_vlmul, bits_vpu_vma, bits_vpu_vsew, bits_vpu_vta, bits_waitForward, bits_wfflags, valid = Signals(63)

class EnqBundle(Bundle):
    def __init__(self):
        super().__init__()
        self.tag = EnqTagSuffix.from_prefix("io_enq_")
        self.req = BundleList(EnqReqBundle, "io_enq_req_#_", 6)

class WriteBackBundle(Bundle):
    bits_data_0, bits_data_1, bits_debugInfo_dispatchTime, bits_debugInfo_eliminatedMove, bits_debugInfo_enqRsTime, \
    bits_debugInfo_issueTime, bits_debugInfo_renameTime, bits_debugInfo_runahead_checkpoint_id, \
    bits_debugInfo_selectTime, bits_debugInfo_tlbFirstReqTime, bits_debugInfo_tlbRespTime, \
    bits_debugInfo_writebackTime, bits_debug_isPerfCnt, bits_exceptionVec_10, bits_exceptionVec_11, \
    bits_exceptionVec_2, bits_exceptionVec_22, bits_exceptionVec_3, bits_exceptionVec_8, bits_exceptionVec_9, \
    bits_flushPipe, bits_intWen, bits_pdest, bits_predecodeInfo_brType, bits_predecodeInfo_isCall, \
    bits_predecodeInfo_isRVC, bits_predecodeInfo_isRet, bits_predecodeInfo_valid, \
    bits_redirect_bits_cfiUpdate_NOS_flag, bits_redirect_bits_cfiUpdate_NOS_value, \
    bits_redirect_bits_cfiUpdate_TOSR_flag, bits_redirect_bits_cfiUpdate_TOSR_value, \
    bits_redirect_bits_cfiUpdate_TOSW_flag, bits_redirect_bits_cfiUpdate_TOSW_value, \
    bits_redirect_bits_cfiUpdate_addIntoHist, bits_redirect_bits_cfiUpdate_afhob_afhob_0_bits_0, \
    bits_redirect_bits_cfiUpdate_afhob_afhob_0_bits_1, bits_redirect_bits_cfiUpdate_afhob_afhob_0_bits_2, \
    bits_redirect_bits_cfiUpdate_afhob_afhob_0_bits_3, bits_redirect_bits_cfiUpdate_afhob_afhob_1_bits_0, \
    bits_redirect_bits_cfiUpdate_afhob_afhob_1_bits_1, bits_redirect_bits_cfiUpdate_afhob_afhob_1_bits_2, \
    bits_redirect_bits_cfiUpdate_afhob_afhob_1_bits_3, bits_redirect_bits_cfiUpdate_afhob_afhob_2_bits_0, \
    bits_redirect_bits_cfiUpdate_afhob_afhob_2_bits_1, bits_redirect_bits_cfiUpdate_afhob_afhob_2_bits_2, \
    bits_redirect_bits_cfiUpdate_afhob_afhob_2_bits_3, bits_redirect_bits_cfiUpdate_afhob_afhob_3_bits_0, \
    bits_redirect_bits_cfiUpdate_afhob_afhob_3_bits_1, bits_redirect_bits_cfiUpdate_afhob_afhob_3_bits_2, \
    bits_redirect_bits_cfiUpdate_afhob_afhob_3_bits_3, bits_redirect_bits_cfiUpdate_afhob_afhob_4_bits_0, \
    bits_redirect_bits_cfiUpdate_afhob_afhob_4_bits_1, bits_redirect_bits_cfiUpdate_afhob_afhob_4_bits_2, \
    bits_redirect_bits_cfiUpdate_afhob_afhob_4_bits_3, bits_redirect_bits_cfiUpdate_afhob_afhob_5_bits_0, \
    bits_redirect_bits_cfiUpdate_afhob_afhob_5_bits_1, bits_redirect_bits_cfiUpdate_afhob_afhob_5_bits_2, \
    bits_redirect_bits_cfiUpdate_afhob_afhob_5_bits_3, bits_redirect_bits_cfiUpdate_br_hit, \
    bits_redirect_bits_cfiUpdate_folded_hist_hist_0_folded_hist, \
    bits_redirect_bits_cfiUpdate_folded_hist_hist_10_folded_hist, \
    bits_redirect_bits_cfiUpdate_folded_hist_hist_11_folded_hist, \
    bits_redirect_bits_cfiUpdate_folded_hist_hist_12_folded_hist, \
    bits_redirect_bits_cfiUpdate_folded_hist_hist_13_folded_hist, \
    bits_redirect_bits_cfiUpdate_folded_hist_hist_14_folded_hist, \
    bits_redirect_bits_cfiUpdate_folded_hist_hist_15_folded_hist, \
    bits_redirect_bits_cfiUpdate_folded_hist_hist_16_folded_hist, \
    bits_redirect_bits_cfiUpdate_folded_hist_hist_17_folded_hist, \
    bits_redirect_bits_cfiUpdate_folded_hist_hist_1_folded_hist, \
    bits_redirect_bits_cfiUpdate_folded_hist_hist_2_folded_hist, \
    bits_redirect_bits_cfiUpdate_folded_hist_hist_3_folded_hist, \
    bits_redirect_bits_cfiUpdate_folded_hist_hist_4_folded_hist, \
    bits_redirect_bits_cfiUpdate_folded_hist_hist_5_folded_hist, \
    bits_redirect_bits_cfiUpdate_folded_hist_hist_6_folded_hist, \
    bits_redirect_bits_cfiUpdate_folded_hist_hist_7_folded_hist, \
    bits_redirect_bits_cfiUpdate_folded_hist_hist_8_folded_hist, \
    bits_redirect_bits_cfiUpdate_folded_hist_hist_9_folded_hist, bits_redirect_bits_cfiUpdate_ghr, \
    bits_redirect_bits_cfiUpdate_histPtr_flag, bits_redirect_bits_cfiUpdate_histPtr_value, \
    bits_redirect_bits_cfiUpdate_isMisPred, bits_redirect_bits_cfiUpdate_jr_hit, \
    bits_redirect_bits_cfiUpdate_lastBrNumOH, bits_redirect_bits_cfiUpdate_pc, bits_redirect_bits_cfiUpdate_pd_brType, \
    bits_redirect_bits_cfiUpdate_pd_isCall, bits_redirect_bits_cfiUpdate_pd_isRVC, \
    bits_redirect_bits_cfiUpdate_pd_isRet, bits_redirect_bits_cfiUpdate_pd_valid, \
    bits_redirect_bits_cfiUpdate_predTaken, bits_redirect_bits_cfiUpdate_sc_hit, bits_redirect_bits_cfiUpdate_sctr, \
    bits_redirect_bits_cfiUpdate_shift, bits_redirect_bits_cfiUpdate_specCnt_0, \
    bits_redirect_bits_cfiUpdate_specCnt_1, bits_redirect_bits_cfiUpdate_ssp, bits_redirect_bits_cfiUpdate_taken, \
    bits_redirect_bits_cfiUpdate_target, bits_redirect_bits_cfiUpdate_topAddr, bits_redirect_bits_debugIsCtrl, \
    bits_redirect_bits_debugIsMemVio, bits_redirect_bits_debug_runahead_checkpoint_id, bits_redirect_bits_ftqIdx_flag, \
    bits_redirect_bits_ftqIdx_value, bits_redirect_bits_ftqOffset, bits_redirect_bits_interrupt, \
    bits_redirect_bits_isRVC, bits_redirect_bits_level, bits_redirect_bits_robIdx_flag, \
    bits_redirect_bits_robIdx_value, bits_redirect_bits_stFtqIdx_flag, bits_redirect_bits_stFtqIdx_value, \
    bits_redirect_bits_stFtqOffset, bits_redirect_valid, bits_robIdx_flag, bits_robIdx_value, valid = Signals(118)

class WriteBackNumsBundle(Bundle):
    bits = Signals(1)

"""
dut
dut.io_enq_req_0_bits_trigger_frontendHit_0.value = 0

bundle = RobBundle(dut)
bundle.req_0.frontendHit.value = 0
"""

class RobBundle(Bundle):
    def __init__(self):
        super().__init__()

        # connect Bundle
        self.control = ControlBundle()
        self.redirect = RedirectBundle.from_prefix("io_redirect_")

        # enq Bundle
        self.enq = EnqBundle()

        # writeback & writebackNums
        # writeback port:1,3,5,7,14-25
        # writeback port : 0-25
        self.wb_channel = list(range(1, 8, 2)) + list(range(14, 25))
        self.writeback = BundleList(WriteBackBundle, "io_writeback_#_", 25)
        self.writeback_nums = BundleList(WriteBackNumsBundle, "io_writebackNums_#_", 25)
        self.snpt = SnptBundle.from_prefix("io_snpt_")





        # self.enq_ptr = Bundle.new_class_from_xport(dut.Rob_enqPtrGenModule_enqPtrVec_0).from_prefix("Rob_enqPtrGenModule_enqPtrVec_0_")
        # self.line = Bundle.new_class_from_xport(dut.bosc_Rob).from_prefix("bosc_Rob_")
        # self.exception = ExceptionBundle(dut)
        # self.commit = CommitBundle(dut)
        # self.rabcommit = rabCommitBundle(dut)
        # #self.diffCommit = diffCommitBundle(dut)
        # self.writebackNums = Bundle.new_class_from_xport(dut.io_writebackNums_15).from_prefix("io_writebackNums_15_")

        # self.robDeqPtr = Bundle.new_class_from_xport(dut.io_robDeqPtr).from_prefix("io_robDeqPtr_")


        # self.fromDecode = Bundle.new_class_from_xport(dut.io_fromDecode).from_prefix("io_fromDecode_")
        # self.singleSignals = SingleTagSuffix.from_prefix("io_")
        # self.difftest = Bundle.new_class_from_xport(dut.io_readGPAMemAddr).from_prefix("io_readGPAMemAddr_")
        # self.io_toDecode = Bundle.new_class_from_xport(dut.io_toDecode).from_prefix("io_toDecode_")
        # self.debugEnqLsq = Bundle.new_class_from_xport(dut.io_debugEnqLsq).from_prefix("io_debugEnqLsq_")
        # self.lsTopDownInfo = Bundle.new_class_from_xport(dut.io_lsTopdownInfo).from_prefix("io_lsTopdownInfo_")
        # self.io_debugTopDown = Bundle.new_class_from_xport(dut.io_debugTopDown).from_prefix("io_debugTopDown_")
        # self.io_perf = Bundle.new_class_from_xport(dut.io_perf).from_prefix("io_perf_")

        # sub model
        #self.internal_bundle = Internal_Bundle(dut)


# class ExceptionTagSuffix(Bundle):
#     valid, bits_commitType, bits_instr, bits_singleStep, bits_vls, bits_isInterrupt, bits_singleStep, bits_crossPageIPFFix = Signals(8)

# class ExceptionBundle(Bundle):
#     def __init__(self,dut):
#         super().__init__()
#         self.tag = ExceptionTagSuffix.from_prefix("io_exception_")
#         self.exceptionVec = Bundle.new_class_from_xport(dut.io_exception_bits_exceptionVec).from_prefix("io_exception_bits_exceptionVec_")
#         self.frontendCanFire = Bundle.new_class_from_xport(dut.io_exception_bits_trigger_frontendCanFire).from_prefix("io_exception_bits_trigger_frontendCanFire_")
#         self.backendCanFire = Bundle.new_class_from_xport(dut.io_exception_bits_trigger_backendCanFire).from_prefix("io_exception_bits_trigger_backendCanFire_")


# class WriteBackSuffix(Bundle):
#     signals = [
#         "19_valid",
#         "19_bits_robIdx_value",
#         "18_valid",
#         "18_bits_robIdx_value"
#     ]


# class CommitSuffix(Bundle):
#     isCommit, isWalk = Signals(2)

# class CommitBundle(Bundle):
#     def __init__(self,dut):
#         super().__init__()
#         self.tag = CommitSuffix.from_prefix("io_commits_")
#         self.commitvalid = Bundle.new_class_from_xport(dut.io_commits_commitValid).from_prefix("io_commits_commitValid_")
#         self.walkValid = Bundle.new_class_from_xport(dut.io_commits_walkValid).from_prefix("io_commits_walkValid_")
#         self.io_Commits_info = Bundle.new_class_from_xport(dut.io_commits_info).from_prefix("io_commits_info_")
#         self.io_Commits_robIdx = Bundle.new_class_from_xport(dut.io_commits_robIdx).from_prefix("io_commits_robIdx_")

# class Internal_Bundle(Bundle):
#     def __init__(self, dut):
#         super().__init__()
#         self.dut = dut

#         #self.enq_ptr = EnqPtrGen(dut)
#         #self.enq_ptr = Bundle.from_prefix("bosc_Rob_enqPtrGenModule_enqPtrVec_0_")
#         self.enq_ptr = Bundle.new_class_from_xport(dut.bosc_Rob_enqPtrGenModule_enqPtrVec_0).from_prefix("bosc_Rob_enqPtrGenModule_enqPtrVec_0_")
#         self.deq_ptr = Bundle.new_class_from_xport(dut.bosc_Rob_deqPtrGenModule_deqPtrVec_0).from_prefix("bosc_Rob_deqPtrGenModule_deqPtrVec_0_")
#         self.walk_ptr = Bundle.new_class_from_xport(dut.bosc_Rob_walkPtrVec_0).from_prefix("bosc_Rob_walkPtrVec_0_")
#         self.entry = Entry(dut)
#         self.deqgroup = DeqGroup(dut)
#         #self.hascommit = HasCommit(dut)
#         self.thisline = LineBundle.from_prefix("bosc_Rob_")

# class EnqPtrGen(Bundle):
#     def __init__(self,dut):
#         super().__init__()
#         self.ptr = Bundle.new_class_from_xport(dut.bosc_Rob_enqPtrGenModule_enqPtrVec_0).from_prefix("bosc_Rob_enqPtrGenModule_enqPtrVec_0_")

# class rabCommitBundle(Bundle):
#     def __init__(self,dut):
#         super().__init__()
#         self.tag = RabCommitSuffix.from_prefix("io_rabCommits_")
#         self.commitvalid = Bundle.new_class_from_xport(dut.io_rabCommits_commitValid).from_prefix("io_rabCommits_commitValid_")
#         self.walkValid = Bundle.new_class_from_xport(dut.io_rabCommits_walkValid).from_prefix("io_rabCommits_walkValid_")
#         self.Commits_info = Bundle.new_class_from_xport(dut.io_rabCommits_info).from_prefix("io_rabCommits_info_")

# class SingleTagSuffix(Bundle):
#     robFull, headNotReady, wfi_enable, debugHeadLsIssue, debugRobHead_debug_fuType, readGPAMemData, hartId = Signals(7)

# class HasCommit(Bundle):
#     def __init__(self,dut):
#         super().__init__()
#         for name in [*[f"bosc_Rob_hasCommitted_{i}" for i in range(8)]]:
#             origin_name = name
#             bundle_name = origin_name.split("_")
#             bundle_name_str = "index" + bundle_name[3]
#             setattr(self,bundle_name_str,Bundle.new_class_from_xport(getattr(dut,name)).from_prefix(name+"_"))

# class RabCommitSuffix(Bundle):
#     isCommit, isWalk = Signals(2)

# class LineBundle(Bundle):
#     robIdxThisLine, allCommited, robBanksRaddrThisLine, lastWalkPtr_value, walkSizeSum = Signals(5)
#     hasCommitted_0, hasCommitted_1, hasCommitted_2, hasCommitted_3, hasCommitted_4, hasCommitted_5, hasCommitted_6, hasCommitted_7 = Signals(8)

# class DeqGroup(Bundle):
#     def __init__(self,dut):
#         super().__init__()
#         for name in [*[f"bosc_Rob_robDeqGroup_{i}" for i in range(8)]]:
#             origin_name = name
#             bundle_name = origin_name.split("_")
#             bundle_name_str = "index" + bundle_name[3]
            # setattr(self,bundle_name_str,Bundle.new_class_from_xport(getattr(dut,name)).from_prefix(name+"_"))


# class debugEnqLsqSuffix(Bundle):
#     canAccept = Signals(1)

# class debugEnqLsqBundle(Bundle):
#     def __init__(self,dut):
#         super().__init__()
#         self.needAlloc = Bundle.new_class_from_xport(dut.io_debugEnqLsq_needAlloc)
#         self.req = Bundle.new_class_from_xport(dut.io_debugEnqLsq_req)

# class Entry(Bundle):
#     def __init__(self,dut):
#         super().__init__()
#         for name in [*[f"bosc_Rob_robEntries_{i}" for i in range(160)]]:
#             origin_name = name
#             bundle_name = origin_name.split("_")
#             bundle_name_str = "index" + bundle_name[3]

#             setattr(self,bundle_name_str,Bundle.new_class_from_xport(getattr(dut,name)).from_prefix(name+"_"))
