import toffee_test
from gen import *
from env import *

@toffee_test.testcase
async def test_env(rob_base_gen):
    gen = GenEnq(rob_base_gen)
    await gen.gen_rob_not_enough()
