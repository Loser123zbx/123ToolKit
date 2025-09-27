import os
import sys


class Log:
    """ 日志 """
    Error = 1
    Warning = 2
    Info = 3
    Debug = 4

    def __init__(self, level, message):
        self.level = level
        self.message = message

    def log(self):
        if self.level == Log.Error:
            print("[Error] " + self.message)
        elif self.level == Log.Warning:
            print("[Warning] " + self.message)
        elif self.level == Log.Info:
            print("[Info] " + self.message)

class ProgressBar:
    """ 进度条 """
    full : int = 100
    loaded : int = 0
    def __init__(self ,full ):
        self.full = full

    def load(self , loadBy ,step):
        """
        :param loadBy: 增加数量
        :param step: 相当于附加消息
        :return:
        """
        self.loaded += loadBy
        print(f"[{self.loaded} / {self.full}]{step}")


    def loadTo(self , loadto, step):
        """
        :param loadTo: 增加到
        :param step: 相当于附加消息
        :return:
        """
        self.loaded = loadto
        print(f"[{self.loaded} / {self.full}]{step}")






