import toffee_test
from gen import *
from env import *

# case 17
@toffee_test.testcase
async def test_flush_self(rob_base_gen):
    rob_base_gen.init_dut()
    gen = GenWalk(rob_base_gen)
    for i in range(200):
        await gen.gen_isflush_self(1)

# case 18
@toffee_test.testcase
async def test_not_flush_self(rob_base_gen):
    rob_base_gen.init_dut()
    gen = GenWalk(rob_base_gen)
    for i in range(200):
        await gen.gen_isflush_self(0)

# case 19
@toffee_test.testcase
async def test_deq_enq(rob_base_gen):
    rob_base_gen.init_dut()
    gen = GenWalk(rob_base_gen)
    for i in range(200):
        await gen.gen_redirect(0,0,0)

# case 20
@toffee_test.testcase
async def test_deq_enq(rob_base_gen):
    rob_base_gen.init_dut()
    gen = GenWalk(rob_base_gen)
    for i in range(200):
        await gen.gen_redirect(0,1,0)

# case 21
@toffee_test.testcase
async def test_deq_enq(rob_base_gen):
    rob_base_gen.init_dut()
    gen = GenWalk(rob_base_gen)
    for i in range(200):
        await gen.gen_redirect(0,2,0)

# case 22
@toffee_test.testcase
async def test_deq_enq(rob_base_gen):
    rob_base_gen.init_dut()
    gen = GenWalk(rob_base_gen)
    for i in range(200):
        await gen.gen_redirect(0,0,1)

# case 23
@toffee_test.testcase
async def test_deq_enq(rob_base_gen):
    rob_base_gen.init_dut()
    gen = GenWalk(rob_base_gen)
    for i in range(200):
        await gen.gen_redirect(0,1,1)

# case 24
@toffee_test.testcase
async def test_deq_enq(rob_base_gen):
    rob_base_gen.init_dut()
    gen = GenWalk(rob_base_gen)
    for i in range(200):
        await gen.gen_redirect(0,2,2)

# case 25
@toffee_test.testcase
async def test_deq_enq(rob_base_gen):
    rob_base_gen.init_dut()
    gen = GenWalk(rob_base_gen)
    for i in range(200):
        await gen.gen_redirect(1,0,0)

# case 26
@toffee_test.testcase
async def test_deq_enq(rob_base_gen):
    rob_base_gen.init_dut()
    gen = GenWalk(rob_base_gen)
    for i in range(200):
        await gen.gen_redirect(1,1,0)

# case 27
@toffee_test.testcase
async def test_deq_enq(rob_base_gen):
    rob_base_gen.init_dut()
    gen = GenWalk(rob_base_gen)
    for i in range(200):
        await gen.gen_redirect(1,2,0)

# case 28
@toffee_test.testcase
async def test_deq_enq(rob_base_gen):
    rob_base_gen.init_dut()
    gen = GenWalk(rob_base_gen)
    for i in range(200):
        await gen.gen_redirect(1,0,1)

# case 29
@toffee_test.testcase
async def test_deq_enq(rob_base_gen):
    rob_base_gen.init_dut()
    gen = GenWalk(rob_base_gen)
    for i in range(200):
        await gen.gen_redirect(1,1,1)

# case 30
@toffee_test.testcase
async def test_deq_enq(rob_base_gen):
    rob_base_gen.init_dut()
    gen = GenWalk(rob_base_gen)
    for i in range(200):
        await gen.gen_redirect(1,2,2)