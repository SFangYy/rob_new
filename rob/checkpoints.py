from toffee.funcov import CovGroup

#from comm import UT_FCOV

def get_coverage_group_of_sc_predict() -> CovGroup:
    slot_name = ["br_slot_0", "tail_slot"]

    g = CovGroup("enq inst", True)
    
    return g
