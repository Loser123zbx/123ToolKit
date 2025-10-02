import os
import core
import platform

def readHosts() -> list:
    """ 读取hosts文件 """
    Log = core.Log(level=core.Log.Info , message = "Reading hosts file")
    Log.log()
    if platform.system() == "Windows":
        with open("C:\Windows\System32\drivers\etc\hosts", 'r' ,encoding="utf-8") as f:
            lines = f.readlines()
        Log = core.Log(level=core.Log.Info , message = "Hosts file read successfully")
        return lines

    else:
        Log = core.Log(level=core.Log.Error , message = "Unsupported OS")
    
    Log.log()

def getHostsDict() -> dict:
    """ 获取hosts文件字典 """
    lines = readHosts()
    hostsDict = {}
    for line in lines:
        if line.startswith("#") or line == "":
            continue
        else:
            host = line.split(" ")[1]
            ip = line.split(" ")[0]
            hostsDict[host] = ip
    return hostsDict



if __name__ == '__main__':
    lines = readHosts()
    for line in lines:
        print(line)
    
    print(getHostsDict())

    print(platform.system())