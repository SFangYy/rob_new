import toffee
from ..dut.Rob import DUTRob
from .agent.enq_agent import EnqAgent
from .bundle.rob_bundle import RobBundle
#from toffee import value

class RobEnv(toffee.Env):
    def __init__(self,dut):
        #super().__init__()
        self.dut = dut
        self.bundle = RobBundle(self.dut).bind(dut)
        self.enq_agent = EnqAgent(self.bundle)
        #self.dut = a
        