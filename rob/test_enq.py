import toffee_test
from gen import *
from env import *


# case 1
@toffee_test.testcase
async def test_invalid(rob_base_gen):
    gen = GenEnq(rob_base_gen)
    await gen.gen_invalid()


# case 2
@toffee_test.testcase
async def test_env(rob_base_gen):
    gen = GenEnq(rob_base_gen)
    await gen.gen_rob_not_enough()

# case 3
@toffee_test.testcase
async def test_rab(rob_base_gen):
    gen = GenEnq(rob_base_gen)
    await gen.gen_rob_not_enough()

# case 4
@toffee_test.testcase
async def test_vtypebuffer(rob_base_gen):
    gen = GenEnq(rob_base_gen)
    await gen.gen_rob_not_enough()

# case 5
@toffee_test.testcase
async def test_enq_inst(rob_base_gen):
    rob_base_gen.init_dut()
    gen = GenEnq(rob_base_gen)
    for i in range(200):
        await gen.gen_enq_inst()

# case 6
@toffee_test.testcase
async def test_special_inst(rob_base_gen):
    rob_base_gen.init_dut()
    gen = GenEnq(rob_base_gen)
    for i in range(200):
        await gen.gen_special_inst()

# case 7
@toffee_test.testcase
async def test_csr_inst(rob_base_gen):
    rob_base_gen.init_dut()
    gen = GenEnq(rob_base_gen)
    for i in range(200):
        await gen.gen_special_inst()

# case 8
@toffee_test.testcase
async def test_enqflag_reverse(rob_base_gen):
    rob_base_gen.init_dut()
    gen = GenEnq(rob_base_gen)
    for i in range(200):
        await gen.gen_enqflag_reverse()

# case 9
@toffee_test.testcase
async def test_rob_empty(rob_base_gen):
    rob_base_gen.init_dut()
    gen = GenEnq(rob_base_gen)
    for i in range(200):
        await gen.gen_rob_empty()