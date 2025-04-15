import toffee_test
from gen import *
from env import *

# case 10
@toffee_test.testcase
async def test_wb_single_cycle(rob_base_gen):
    await rob_base_gen.init_dut()
    gen = GenWb(rob_base_gen)
    for i in range(200):
        await gen.gen_wb_incycle(0)
    #await gen.gen_invalid()


# case 11
@toffee_test.testcase
async def test_wb_multi_cycle(rob_base_gen):
    await rob_base_gen.init_dut()
    gen = GenWb(rob_base_gen)
    for i in range(200):
        await gen.gen_wb_incycle(0)

# case 12
@toffee_test.testcase
async def test_wb_special_inst(rob_base_gen):
    await rob_base_gen.init_dut()
    gen = GenWb(rob_base_gen)
    for i in range(200):
        await gen.gen_wb_special_inst()

# case 13
@toffee_test.testcase
async def test_wb_not_old_inst(rob_base_gen):
    await rob_base_gen.init_dut()
    gen = GenWb(rob_base_gen)
    for i in range(200):
        await gen.gen_wb_not_old_inst()

# case 14
@toffee_test.testcase
async def test_canot_commit(rob_base_gen):
    await rob_base_gen.init_dut()
    gen = GenWb(rob_base_gen)
    for i in range(200):
        await gen.gen_canot_commit()

# case 15
@toffee_test.testcase
async def test_line_sub_commit(rob_base_gen):
    await rob_base_gen.init_dut()
    gen = GenWb(rob_base_gen)
    for i in range(200):
        await gen.gen_line_isall_commit(0)

# case 16
@toffee_test.testcase
async def test_line_all_commit(rob_base_gen):
    await rob_base_gen.init_dut()
    gen = GenWb(rob_base_gen)
    for i in range(200):
        await gen.gen_line_isall_commit(1)

# case 32
@toffee_test.testcase
async def test_wb_with_exception(rob_base_gen):
    await rob_base_gen.init_dut()
    gen = GenWb(rob_base_gen)
    for i in range(200):
        await gen.gen_wb_with_exception()
