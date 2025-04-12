from toffee.funcov import CovGroup
import toffee.funcov as fc
#from comm import UT_FCOV
def is_enq_ptr(bundle,i):
    if getattr(bundle.enq,"req_{enq_channel}_bits_exceptionVec_{i}").value == 1:
        return True
    else:
        return False 

def is_enq_exception(bundle, enq_channel):
    exception_list = [0,1,2,12,20,22]
    signal = False
    for i in range(exception_list):
        if getattr(bundle.enq,"req_{enq_channel}_bits_exceptionVec_{i}").value == 1:
            signal = True
    return signal

def is_special_inst(bundle,itype):
    signal = False
    def to_op_type(itype):
        if itype == "stu":
            return 1
        elif itype == "ldu":
            return 1
        elif itype == "csr":
            return 1

    for i in range(6):
        if getattr(bundle.enq,"req_{enq_channel}_fuOpType").value == to_op_type(itype):
            signal = True
    return signal

def get_coverage_group_of_sc_predict(bundle:Bundle) -> CovGroup:

    group = CovGroup("enq inst", True)

    group.add_watch_point(bundle, {
        f"enq_ptr_value equal{w}": bundle.internal_bundle.enq_ptr.value.value = w for w in range(159)
    }, name="enqptr_value")

    group.add_watch_point(bundle.internal_bundle.enq_ptr.flag, {
        "enq_ptr_flag 0": fc.Eq(0),
        "enq_ptr_flag 1": fc.Eq(1),
    }, name="enq full")

    group.add_watch_point(bundle,{
        f"enq_special_inst_stu":is_special_inst(bundle,"stu"),
        f"enq_special_inst_ldu":is_special_inst(bundle,"ldu"),
        f"enq_special_inst_csr":is_special_inst(bundle,"csr"),
    })

    group.add_watch_point(bundle,{
        f"enq_exception_{i}":is_enq_exception(bundle, w) for w in range(6) 
    })
    return group

def check_DeqGroup(bundle:Bundle) -> CovGroup:
    group = CovGroup("wb inst", True)

    group.add_watch_point(bundle, {
        f"deq_ptr_value equal{w}": bundle.internal_bundle.deq_ptr.value.value == w for w in range(159)
    }, name="enqptr_value")

    group.add_watch_point(bundle.internal_bundle.deq_ptr.flag.value, {
        "deq_ptr_flag 0": fc.Eq(0),
        "deq_ptr_flag 1": fc.Eq(1),
    }, name="enq full")

    group.add_watch_point(bundle, {
        f"DeqGroup_{i}": is_DeqGroup(i) for i in range(7)
    }, name="line entry ")

    group.add_watch_point(bundle, {
        f"allcommited_{i}": bundle.internal_bundle.thisline.allcommited.value == i for i in range(2)
    }, name="line is commited")

    group.add_watch_point(bundle, {
        f"hascommited_{i}": bundle.internal_bundle.thisline.hascommited.value == i for i in range(7)
    }, name="line entry ")

    group.add_watch_point(bundle.isEmpty, {
        f"rob_empty": fc.Eq(1)
    }, name="rob empty")

def check_walk(bundle:Bundle) -> CovGroup:
    group = CovGroup("rob walk", True)
    return group