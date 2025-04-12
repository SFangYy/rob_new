try:
    from UT_Rob import *
except:
    try:
        from Rob import *
    except:
        from __init__ import *


if __name__ == "__main__":
    dut = DUTRob()
    # dut.init_clock("clk")

    dut.Step(1)

    dut.Finish()
