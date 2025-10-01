
import ctypes
from ctypes import CDLL, c_int, c_char_p
import time
import os

class Log:
    """ 日志类 class for log """
    Error = 1
    Warning = 2
    Info = 3
    Debug = 4
    def __init__(self, level, message):
        self.level = level
        self.message = message
    
    def log(self):
        if self.level == Log.Error :
            print("[Error] " + self.message)
        elif self.level == Log.Warning :
            print("[Warning] " + self.message)
        elif self.level == Log.Info :
            print("[Info] " + self.message)

if __name__ == "__main__":

    _log:Log = Log(Log.Info, "开始导入lib.dll")
    _log.log()  

    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        lib_path = os.path.join(script_dir, "lib.dll")

        _log = Log(Log.Info, "成功导入lib.dll")
        _log.log()

    except FileNotFoundError:
        _log = Log(Log.Error, "未找到lib.dll")
        _log.log()

        exit()
    
