import toffee_test
from gen import *
from env import *

# case 17
@toffee_test.testcase
async def test_flush_self(rob_base_gen):
    rob_base_gen.init_dut()
    gen = GenWb(rob_base_gen)
    for i in range(200):
        await gen.gen_wb_incycle(0)

# case 18
@toffee_test.testcase
async def test_not_flush_self(rob_base_gen):
    rob_base_gen.init_dut()
    gen = GenWb(rob_base_gen)
    for i in range(200):
        await gen.gen_wb_incycle(0)