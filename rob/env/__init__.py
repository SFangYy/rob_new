import toffee
from .agent import *
from .rob_bundle import *
from .rob_wrapper import *
from .refmodel import *

class RobEnv(toffee.Env):
    def __init__(self, bundle):
        super().__init__()

        self.enq_agent = EnqAgent(bundle)
        self.wb_agent = WritebackAgent(bundle)
