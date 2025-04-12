import random
from dataclasses import dataclass
class Rob_Instr:
    valid:int = 0
    instr:int = 0
    pc:int = 0
    exceptionVec:int = 0
    frontendCanFire:int = 0
    isRVC:int = 0
    ftqPtr_flag:int = 0
    firstUop:int = 0
    lastUop:int = 0
    isVset:int = 0
    flushpipe:int = 0
    numWB:int = 0
    eliminatedMove:int = 0
    snapshot:int = 0
    flushpipe:int = 0
    def __init__(self):
        for name in ['valid', 'instr', 'pc','exceptionVec', 'frontendCanFire', 'frontendHit', 'isRVC', 'ftqPtr_flag', 'ftqPtr_value', 'ftqOffset','ldest', 
                     'fuType', 'fuOpType', 'waitForward', 'blockBackward', 'firstUop', 'lastUop', 'robIdx_flag', 'robIdx_value', 'fpWen', 'rfWen', 'vecWen',
                     'v0Wen', 'v0Wen', 'vlWen', 'isXSTrap', 'flushPipe', 'vpu_vill', 'vpu_vma','vpu_vta','vpu_vsew','vpu_vlmul','vlsInstr','wfflags','isMove',
                     'isVset', 'numWB', 'commitType', 'pdest','instrSize', 'dirtyFs', 'dirtyVs', 'eliminatedMove', 'snapshot', 'debugInfo_eliminatedMove',
                     'debugInfo_renameTime','flushpipef','snapshot','loadWaitBit','singleStep','debug_fuType']:
            setattr(self, name, 0)
            self.exception = 0
        self.inst_list = ["jmp", "brh", "i2f","i2v", "f2v", "ldu", "alu", "mul" ,"div", "fence", "bku",
                        "jmp", "fmac", "fcvt", "fDivSqrt", "ldu", "stu", "mou", "vipu", "vialuF", "vppu", 
                        "vimac", "vidiv", "vfpu","vfpu","vfma","vfidv","vfcvt","vsetiwi", "vsetiwf", "vldu", 
                        "vstu", "vsegldu", "vsegstu" ]
        selected_attr = random.choice(["rfWen","fpWen","vecWen"])
        setattr(self, selected_attr, random.randint(0, 1))
        #self.randmoize()

    def randmoize(self):
        self.valid = random.randint(0,1)
        self.instr = random.randint(0,2**31-1)
        self.pc = random.randint(0,2**40-1)
        self.exceptionVec_0 = random.randint(0,1)
        self.frontendHit = random.randint(0,1)
        self.isRVC = random.randint(0,1)
        self.ftqPtr_flag = random.randint(0,1)
        self.ftqPtr_value = random.randint(0,2**5-1)
        self.ftqOffset = random.randint(0,2**3-1)
        self.ldest = random.randint(1,2**5-1)
        self.fuType = 0
        self.fuOpType = 0     
        self.waitForward = random.randint(0,1)
        self.blockBackward = random.randint(0,1)
        self.firstUop = random.randint(0,1)
        self.lastUop = random.randint(0,1)
        self.robIdx_flag = 1
        self.robIdx_value = random.randint(0,2**7-1)
        self.fpWen = random.randint(0,1)
        self.numWB = random.randint(1,2**4-1)
        self.pdest = random.randint(1,2**8-1)
        self.instrSize = random.randint(0,2**3-1)
        
    def gen_exception(self,indexf):
        self.exceptionVec_0 = 1

    def gen_inst_type(self,inst_type):
        if inst_type in self.inst_list:
            idx = self.inst_list.index(inst_type)
            self.fuType = idx 
            self.fuOpType = 2 ** idx
        if inst_type == "csr":
            self.blockBackward = 1
        elif inst_type in ["ldu","stu","jmp","brh","vldu","vstu"]:
            self.pdest = 1
        elif inst_type == "move":
            self.isMove = 1
            self.eliminatedMove = 1
            self.pdest = 1
            self.numWB = 0
        elif inst_type in self.inst_list[18:34]:
            self.isVset = 1
            self.vpu_vill = 1
            self.vpu_vlmul = 1
            self.vpu_vsew = 1
            self.vpu_vta = 1

    def enq_inst(self,inst_type = None):
        self.randmoize()
        self.valid = 1
        self.firstUop = 1
        self.lastUop = 0
        self.exceptionVec_0 = 0
        self.instrSize = 2
        self.blockBackward = 0
        if inst_type == None:
            inst_type = random.choice(self.inst_list[0:34])

        self.gen_inst_type(inst_type)

        

class Debug_Info:
    def __init__(self):
        self.valid = 0
        self.robIdx = 0
        self.lqIdx = 0
    def enq_debug(self,robIdx,lqIdx):
        self.valid = 1
        self.robIdx = robIdx
        self.lqIdx = lqIdx


class Rob_Entry(Rob_Instr):
    def __init__(self,a_instance,wirteback):
        #super.__init__()
        self.__dict__.update(a_instance.__dict__)
        self.is_writeback = 0
        self.is_commit = 0


class Rob_Writeback:
    def __init__(self):
        for name in ['valid', 'data', 'flushPipe','robIdx_flag', 'robIdx_value', *[f"exceptionVec_{i}" for i in range(24)],'flushPipe',
                     'replay', *[f"debug_{debug_name}" for debug_name in ['isMMIO', 'isPerfCnt','paddr']],*[f"debugInfo_{info_name}"
                      for info_name in ['enqRsTime', 'selectTime', 'issueTime', 'writebackTime']], 'nums']:
            setattr(self,name,0)
        self.exception = -1
        self.channel = 0

    def randmoize(self):
        self.debugInfo_selectTime = random.randint(0,2**63-1)
        self.debugInfo_enqRsTime = random.randint(0,2**63-1)

    def gen_channel(self,fuOpType):
        if fuOpType == 0:
            number = [1,3,5]
            return random.choice(number)
            self.value = 1
        elif fuOpType == 1:
            number = [1,3,4]
            return random.choice(number)
        elif fuOpType == 2:
            return 5
        elif fuOpType == 3:
            return 5
        elif fuOpType == 4:
            return 7
        elif fuOpType == 5:
            return 7
        elif fuOpType == 6:
            number = [1,3,5,7]
            return random.choice(number)
        elif fuOpType == 7:
            number = [0,2]
            return random.choice(number)
        elif fuOpType == 8:
            return 7
        elif fuOpType == 9:
            return 7
        elif fuOpType == 10:
            number = [1,3]
            return random.choice(number)
        elif fuOpType == 11:
            number = [7,14,15,17]
            return random.choice(number)
        elif fuOpType == 12:
            number = [7,14,15,17]
            return random.choice(number)
        elif fuOpType == 13:
            return 7
        elif fuOpType == 14:
            number = [14,15]
            return random.choice(number)
        elif fuOpType == 15:
            number = [21,22,23]
            return random.choice(number)
        elif fuOpType == 16:
            number = [19,7,15,17]
            return random.choice(number)
        elif fuOpType == 17:
            number = [19,3,15,17]
            return random.choice(number)
        elif fuOpType == 18:
            return 15
        elif fuOpType == 19:
            number = [14,16]
            return random.choice(number)
        elif fuOpType == 20:
            return 14
        elif fuOpType == 21:
            return 14
        elif fuOpType == 22:
            return 18
        elif fuOpType == 23:
            return 18
        elif fuOpType == 24:
            number = [15,17]
            return random.choice(number)
        elif fuOpType == 25:
            number = [14,16]
            return random.choice(number)
        elif fuOpType == 26:
            return 18
        elif fuOpType == 27:
            number = [15,17]
            return random.choice(number)
        elif fuOpType == 28:
            return 5
        elif fuOpType == 29:
            return 5
        elif fuOpType == 30:
            return 15
        elif fuOpType == 31:
            number = [24,25]
            return random.choice(number)
        elif fuOpType == 32:
            number = [24,25]
            return random.choice(number)
        elif fuOpType == 33:
            return 24
        elif fuOpType == 34:
            return 24
            
    def gen_exception(self,exceptionTag):
        print("generate exception")

    def writeback_instr(self,data,robIdx_value,fuOpType,nums,hasexception,flushpipe):
        self.valid = 1
        self.data = data
        self.robIdx_flag = 1
        self.robIdx_value = robIdx_value
        self.nums = nums
        self.exception = -1
        self.channel = self.gen_channel(fuOpType)
        
        self.flushpipe = flushpipe
        if hasexception == 1 and (19 <= self.channel and self.channel <= 25):
            number = []
            for i in range(24):
                number.append(i)
            self.exception = random.choice(number)
        elif hasexception == 1 and (self.channel == 14 or self.channel == 15):
            self.exception_0 = 2
        elif hasexception == 1 and self.channel == 5:
            number = [2,3,8,9,10,11,22]
            self.exception = random.choice(number)
       
    def set_attr(self,robIdx_value,nums,channel,exception):
        self.valid = 1
        self.robIdx_value = robIdx_value
        self.robIdx_flag = 1
        self.nums = nums
        self.channel = channel
        self.exception = exception
        
    def writeback_reset(self):
        self.__init__()
    
    def writeback_instr_withexception(self):
        self.writeback_instr()
        #self.exceptionVec_0 = 




