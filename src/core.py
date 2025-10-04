
import ctypes
from ctypes import CDLL, c_double, c_char_p,cdll, POINTER, byref
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
    
    def log(self) -> None:
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
        lib = CDLL(lib_path)
        _log = Log(Log.Info, "成功导入lib.dll")
        _log.log()

    except FileNotFoundError:
        _log = Log(Log.Error, "未找到lib.dll")
        _log.log()

        exit()
    lib = cdll.LoadLibrary("lib.dll")
    # 设置函数返回类型
    lib.getDiskFreeSpace.restype = c_double
    # 设置函数参数类型
    lib.getDiskFreeSpace.argtypes = [c_char_p]
    path = b"D:\\123's\\"
 
    lib.convertToGiB.restype = c_double
    lib.convertToGiB.argtypes = [c_double]  # 参数应该是c_double而不是c_char_p
    
    getDiskFreeSpace = lib.getDiskFreeSpace
    convertToGiB = lib.convertToGiB


    result = convertToGiB(getDiskFreeSpace(path))

    print(result)