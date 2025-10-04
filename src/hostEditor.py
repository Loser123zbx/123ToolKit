import os
import core
import platform
from core import Log

def readHosts() -> list:
    """ 读取hosts文件 """
    _log: Log = Log(level=core.Log.Info , message = "Reading hosts file")
    _log.log()
    if platform.system() == "Windows":
        with open("C:\Windows\System32\drivers\etc\hosts", 'r' ,encoding="utf-8") as f:
            lines = f.readlines()
        lines = [item for item in lines if item != ' ']
        lines = [item for item in lines if item != '\n']
        _log = Log(level=core.Log.Info , message = "Hosts file read successfully")
        return lines

    else:
        _Log = Log(level=core.Log.Error , message = "Unsupported OS")
    
    _log.log()

def getHostsDict() -> dict:
    """ 获取hosts文件字典 """
    lines:list = readHosts()
    hostsDict:dict = {}
    _log = Log(level=core.Log.Info , message = "Getting hosts file dictionary")
    try:
        for line in lines:
            # 去除 BOM 和首尾空白
            line:str = line.strip().lstrip('\ufeff')

            if line.startswith("#") or line == "":
                _log = Log(level=core.Log.Info , message = f"Comment line: {line}")
                _log.log()
                continue
            else:
                host:list = line.split(" ")[1]
                # host:list = [item for item in host if item != ' ']               

                ip:list = line.split(" ")[0]
                # ip:list = [item for item in ip if item != ' ']

                hostsDict[host] = ip
                _log = Log(level=core.Log.Info , message = f"Host: {host} , IP: {ip}")
                _log.log()

    except TypeError as e:
        _log = Log(level=core.Log.Error , message = f"Error: {e} \n\titem: {line}")
        
        
        _log.log()
    return hostsDict



if __name__ == '__main__':
    lines = readHosts()
    for line in lines:
        print(line)
    
    print(getHostsDict())

    print(platform.system())

    print(readHosts())