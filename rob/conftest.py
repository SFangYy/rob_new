from picker_out_rob import DUTRob
from env import *
from gen import *
import toffee_test

@toffee_test.fixture
async def rob_base_gen(toffee_request:toffee_test.ToffeeRequest):
    dut = toffee_request.create_dut(DUTRob, "clock")
    toffee.start_clock(dut)
    env = RobEnv(dut)
    gen = GenBase(env)
    # toffee_request.add_cov_group([
    #     get_coverage_group_of_sc_predict
    # ])
    return gen
