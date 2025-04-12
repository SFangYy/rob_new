import toffee
from .agent import *
from .rob_bundle import *
from .rob_wrapper import *
from .refmodel import *

class RobEnv(toffee.Env):
    def __init__(self, dut):
        super().__init__()

        self.dut = dut
        self.bundle = RobBundle(self.dut).bind(dut)
        self.enq_agent = EnqAgent(self.bundle)
        self.wb_agent = WritebackAgent(self.bundle)
