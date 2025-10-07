
import ctypes
from ctypes import CDLL, c_double, c_char_p,cdll, POINTER, byref,c_int
import time
import os
import math

class Log:
    """ 日志类 class for log """
    Error = 1
    Warning = 2
    Info = 3
    Debug = 4
    def __init__(self, level, message):
        self.level = level
        self.message = message
    
    def log(self) -> None:
        if self.level == Log.Error :
            print("[Error] " + self.message)
        elif self.level == Log.Warning :
            print("[Warning] " + self.message)
        elif self.level == Log.Info :
            print("[Info] " + self.message)

class progress:
    """ 进度条类 class for progress bar """
    def __init__(self, total = 10):
        self.total :int = total
        self.init :int  = 0
        self.loaded :int = self.init
        self.fill :str  = "|"
        self.empty :str = "·"
        self.totalBlocks :int = 50
        """
        self.text + self.leftbar + ... + self.rightbar 
        """
        self.leftbar :str = "["
        self.rightbar :str = "]"
        self.text :str = ""
        

    def show(self ,text :str = "") -> None:
        """ show progress bar """
        blocks :int = math.floor(self.total / self.totalBlocks) #计算每个块代表的数值
        blocks = math.floor( self.loaded / blocks ) * self.fill + self.empty * (self.totalBlocks - math.floor( self.loaded / blocks ))
        output :str = (self.text + self.leftbar + blocks + self.rightbar +
                       " " + str(self.loaded) + "/" + str(self.total) + "  " + str(round(self.loaded / self.total * 100, 2)) + "%" + " " + text)
        print(output, end="\n")

    def update(self, add :int = 1) -> None:
        """ update progress bar """
        self.loaded += add
        
    def updateto(self, to :int) -> None:
        """ update progress bar to a specific value """
        self.loaded = to
        


if __name__ == "__main__":

    _log:Log = Log(Log.Info, "开始导入lib.dll")
    _log.log()  

    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        lib_path = os.path.join(script_dir, "lib.dll")
        lib = CDLL(lib_path)
        _log = Log(Log.Info, "成功导入lib.dll")
        _log.log()

    except FileNotFoundError:
        _log = Log(Log.Error, "未找到lib.dll")
        _log.log()

    # lib = CDLL("lib.dll")
    # lib.CalculateDirectorySize.argtypes = [c_char_p, POINTER(c_double)]




