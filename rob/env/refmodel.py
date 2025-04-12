from toffee import *


class RobModel(Model):
    def __init__(self):
        super().__init__()

        self.queue = []

    @driver_hook(agent_name="enq_agent")
    def enq_list(self, instr_list):
        print("[RobModel] Enqueueing instructions:")
        for instr in instr_list:
            print(instr)
            # self.queue.append(instr)

    @driver_hook(agent_name="enq_agent")
    def rob_redirect(self, valid, idx_flag, idx_value, level, useSnpt=0):
        print("[RobModel] Rob redirecting:")
        print(f"valid: {valid}, idx_flag: {idx_flag}, idx_value: {idx_value}, level: {level}, useSnpt: {useSnpt}")

    @driver_hook(agent_name="wb_agent")
    def writeback(self, channel, writeback_instr):
        print("[RobModel] Writeback channel:")
        print(f"channel: {channel}, writeback_instr: {writeback_instr}")

