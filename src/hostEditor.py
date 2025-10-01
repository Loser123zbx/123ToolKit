import os
import core
import platform

def readHosts():
    Log = core.Log(level=core.Log.Info , message = "Reading hosts file")
    Log.log()
    if platform.system() == "Windows":
        with open("C:\Windows\System32\drivers\etc\hosts", 'r' ,encoding="utf-8") as f:
            lines = f.readlines()
        Log = core.Log(level=core.Log.Info , message = "Hosts file read successfully")
        return lines
    elif platform.system() == "Linux" or platform.system() == "Darwin":
        with open("/etc/hosts", 'r' ,encoding="utf-8") as f:
            lines = f.readlines()
        Log = core.Log(level=core.Log.Info , message = "Hosts file read successfully")
        return lines
    else:
        Log = core.Log(level=core.Log.Error , message = "Unsupported OS")
    
    Log.log()



if __name__ == '__main__':
    lines = readHosts()
    for line in lines:
        print(line)
    
    print(platform.system())