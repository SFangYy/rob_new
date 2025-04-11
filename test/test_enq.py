import os
from ..dut.Rob import DUTRob
from ..env.env import RobEnv
from ..env.gen.gen_base import GenBase
from .checkpoints import get_coverage_group_of_sc_predict
dut = DUTRob()

print("success")
"Initialize before each test"
import toffee
import toffee_test
#from env.env import RobEnv#，AdderBundle
#from env.bundle.rob bundle import RobBundle
#from env.rob wrapper import *


@toffee_test.testcase
async def test_env(rob_env: RobEnv):
    #env = rob_env
    print("this is test env")


@toffee_test.fixture
def rob_env(toffee_request:toffee_test.ToffeeRequest):

    rob = DUTRob()
    dut = toffee_request.create_dut(DUTRob,"clock")
    env = RobEnv(dut)
    gen = GenBase(env)
    #rob.InitClock("clock")
    #toffee.start_clock(dut)
    # toffee_request.add_cov_group([
    #     get_coverage_group_of_sc_predict
    # ])
    yield env
    #def start code():
     #   mlvp.start_clock （rob）
     #   env = RobEnv（RobBundle （rob）.bind （rob））
     #   print （mlvp.Bundle.detect_unconnected_signals（rob））
     #   return env
#def start_code（）：
    #return start code
