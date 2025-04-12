import os
from ..dut.Rob import DUTRob
from ..env.env import RobEnv
from ..env.gen.gen_base import GenBase
from ..env.gen.gen_enq import GenEnq
from .checkpoints import get_coverage_group_of_sc_predict
dut = DUTRob()

import toffee
import toffee_test
#from env.env import RobEnv#，AdderBundle
#from env.bundle.rob bundle import RobBundle
#from env.rob wrapper import *


@toffee_test.testcase
async def test_env(rob_base_gen):
    gen = GenEnq(rob_base_gen)
    await gen.gen_rob_not_enough()



@toffee_test.fixture
def rob_base_gen(toffee_request:toffee_test.ToffeeRequest):

    dut = toffee_request.create_dut(DUTRob,"clock")
    env = RobEnv(dut)
    gen = GenBase(env)
    #rob.InitClock("clock")
    toffee.start_clock(dut)
    # toffee_request.add_cov_group([
    #     get_coverage_group_of_sc_predict
    # ])
    yield gen

