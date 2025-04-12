from toffee import Bundle, Signal, Signals

class EnqTagSuffix(Bundle):
    tage_enable, sc_enable = Signals(2)
    

class controlBundle(Bundle):
    signals = ["reset","clock","canAccept","isEmpty",]
# io_enq_req_i(0-5)_
class EnqBundle(Bundle):
    def __init__(self,dut):
        super().__init__()
        self.tag = EnqTagSuffix.from_prefix("io_enq_")
        self.req_0 = Bundle.new_class_from_xport(dut.io_enq_req_0).from_prefix("io_enq_req_0_")
        self.req_1 = Bundle.new_class_from_xport(dut.io_enq_req_1).from_prefix("io_enq_req_1_")
        self.req_2 = Bundle.new_class_from_xport(dut.io_enq_req_2).from_prefix("io_enq_req_2_")
        self.req_3 = Bundle.new_class_from_xport(dut.io_enq_req_3).from_prefix("io_enq_req_3_")
        self.req_4 = Bundle.new_class_from_xport(dut.io_enq_req_4).from_prefix("io_enq_req_4_")
        self.req_5 = Bundle.new_class_from_xport(dut.io_enq_req_5).from_prefix("io_enq_req_5_")

class ExceptionTagSuffix(Bundle):
    signals = [
        "valid",
        "bits_commitType",
        "bits_instr",
        "bits_singleStep",
        "bits_vls",
        "bits_isInterrupt",
        "bits_singleStep",
        "bits_crossPageIPFFix",
    ]


class ExceptionBundle(Bundle):
    def __init__(self,dut):
        super().__init__()
        self.tag = ExceptionTagSuffix.from_prefix("io_exception_")
        self.exceptionVec = Bundle.new_class_from_xport(dut.io_exception_bits_exceptionVec).from_prefix("io_exception_bits_exceptionVec_")
        self.frontendCanFire = Bundle.new_class_from_xport(dut.io_exception_bits_trigger_frontendCanFire).from_prefix("io_exception_bits_trigger_frontendCanFire_")
        self.backendCanFire = Bundle.new_class_from_xport(dut.io_exception_bits_trigger_backendCanFire).from_prefix("io_exception_bits_trigger_backendCanFire_")


class WriteBackSuffix(Bundle):
    signals = [
        "19_valid",
        "19_bits_robIdx_value",
        "18_valid",
        "18_bits_robIdx_value"
    ]


class CommitSuffix(Bundle):
    signals = [
        "isCommit",
        "isWalk",
    ]
class CommitBundle(Bundle):
    def __init__(self,dut):
        super().__init__()
        self.tag = CommitSuffix.from_prefix("io_commits_")
        self.commitvalid = Bundle.new_class_from_xport(dut.io_commits_commitValid).from_prefix("io_commits_commitValid_")
        self.walkValid = Bundle.new_class_from_xport(dut.io_commits_walkValid).from_prefix("io_commits_walkValid_")
        self.io_Commits_info = Bundle.new_class_from_xport(dut.io_commits_info).from_prefix("io_commits_info_")
        self.io_Commits_robIdx = Bundle.new_class_from_xport(dut.io_commits_robIdx).from_prefix("io_commits_robIdx_")

class RabCommitSuffix(Bundle):
    signals = [
        "isCommit",
        "isWalk",
    ]
class EnqPtrGen(Bundle):
    def __init__(self,dut):
        super().__init__()
        self.ptr = Bundle.new_class_from_xport(dut.bosc_Rob_enqPtrGenModule_enqPtrVec_0).from_prefix("bosc_Rob_enqPtrGenModule_enqPtrVec_0_")

class rabCommitBundle(Bundle):
    def __init__(self,dut):
        super().__init__()
        self.tag = RabCommitSuffix.from_prefix("io_rabCommits_")
        self.commitvalid = Bundle.new_class_from_xport(dut.io_rabCommits_commitValid).from_prefix("io_rabCommits_commitValid_")
        self.walkValid = Bundle.new_class_from_xport(dut.io_rabCommits_walkValid).from_prefix("io_rabCommits_walkValid_")
        self.Commits_info = Bundle.new_class_from_xport(dut.io_rabCommits_info).from_prefix("io_rabCommits_info_")
        

class SingleTagSuffix(Bundle):
    signals = [
        "robFull",
        "headNotReady",
        "wfi_enable",
        "debugHeadLsIssue",
        "debugRobHead_debug_fuType",
        "readGPAMemData",
        "hartId"
    ]

class debugEnqLsqSuffix(Bundle):
    signals = [
        "canAccept"   
    ]
class debugEnqLsqBundle(Bundle):
    def __init__(self,dut):
        super().__init__()
        self.needAlloc = Bundle.new_class_from_xport(dut.io_debugEnqLsq_needAlloc)
        self.req = Bundle.new_class_from_xport(dut.io_debugEnqLsq_req)

class Entry(Bundle):
    def __init__(self,dut):
        super().__init__()
        for name in [*[f"bosc_Rob_robEntries_{i}" for i in range(160)]]:
                    origin_name = name
                    bundle_name = origin_name.split("_")
                    bundle_name_str = "index" + bundle_name[3]
        
                    setattr(self,bundle_name_str,Bundle.new_class_from_xport(getattr(dut,name)).from_prefix(name+"_"))

class DeqGroup(Bundle):
    def __init__(self,dut):
        super().__init__()
        for name in [*[f"bosc_Rob_robDeqGroup_{i}" for i in range(8)]]:
                    origin_name = name
                    bundle_name = origin_name.split("_")
                    bundle_name_str = "index" + bundle_name[3]
                    setattr(self,bundle_name_str,Bundle.new_class_from_xport(getattr(dut,name)).from_prefix(name+"_"))

class HasCommit(Bundle):
    def __init__(self,dut):
        super().__init__()
        for name in [*[f"bosc_Rob_hasCommitted_{i}" for i in range(8)]]:
                    origin_name = name
                    bundle_name = origin_name.split("_")
                    bundle_name_str = "index" + bundle_name[3]
                    setattr(self,bundle_name_str,Bundle.new_class_from_xport(getattr(dut,name)).from_prefix(name+"_"))
class LineBundle(Bundle):
    signals = [
        "robIdxThisLine_0",
        "allCommited",
        "robBanksRaddrThisLine",
        "lastWalkPtr_value",
        "walkSizeSum",
        *[f"hasCommitted_{i}" for i in range(8)]
    ]
class Internal_Bundle(Bundle):
    def __init__(self, dut):
        super().__init__()
        self.dut = dut 

        #self.enq_ptr = EnqPtrGen(dut)
        #self.enq_ptr = Bundle.from_prefix("bosc_Rob_enqPtrGenModule_enqPtrVec_0_")
        self.enq_ptr = Bundle.new_class_from_xport(dut.bosc_Rob_enqPtrGenModule_enqPtrVec_0).from_prefix("bosc_Rob_enqPtrGenModule_enqPtrVec_0_")
        self.deq_ptr = Bundle.new_class_from_xport(dut.bosc_Rob_deqPtrGenModule_deqPtrVec_0).from_prefix("bosc_Rob_deqPtrGenModule_deqPtrVec_0_")
        self.walk_ptr = Bundle.new_class_from_xport(dut.bosc_Rob_walkPtrVec_0).from_prefix("bosc_Rob_walkPtrVec_0_")
        self.entry = Entry(dut)
        self.deqgroup = DeqGroup(dut)
        #self.hascommit = HasCommit(dut)
        self.thisline = LineBundle.from_prefix("bosc_Rob_")
        


"""
dut
dut.io_enq_req_0_bits_trigger_frontendHit_0.value = 0

bundle = RobBundle(dut)
bundle.req_0.frontendHit.value = 0

"""
class RobBundle(Bundle):
    def __init__(self, dut):
        super().__init__()
        self.dut = dut
        self.wb_channel = list(range(1, 8, 2)) + list(range(14, 25))
        
        # connect Bundle
        self.control = controlBundle()
        self.redirect = Bundle.new_class_from_xport(dut.io_redirect).from_prefix("io_redirect_")
        # enq Bundle
        self.enq = EnqBundle(dut)

        # writeback & writebackNums
        # writeback port:1,3,5,7,14-25
        # writeback port : 0-25
        for name in [*[f"io_writeback_{i}" for i in self.wb_channel]]:
            setattr(self,name,Bundle.new_class_from_xport(getattr(dut,name)).from_prefix(name+"_"))
        for name in [*[f"io_writebackNums_{i}" for i in range(26)]]:
           setattr(self,name,Bundle.new_class_from_xport(getattr(dut,name)).from_prefix(name+"_"))
        self.snpt = Bundle.new_class_from_xport(dut.io_snpt).from_prefix("io_snpt_")
        #self.enq_ptr = Bundle.new_class_from_xport(dut.Rob_enqPtrGenModule_enqPtrVec_0).from_prefix("Rob_enqPtrGenModule_enqPtrVec_0_")
        #self.line = Bundle.new_class_from_xport(dut.bosc_Rob).from_prefix("bosc_Rob_")
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