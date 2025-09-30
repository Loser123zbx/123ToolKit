
import ctypes
from ctypes import cdll, c_void_p, c_int

try:
    ll = ctypes.cdll.LoadLibrary   
    lib = ll("../library.so")  

except FileNotFoundError:
    print("lib.so not found")
    exit(1)



if __name__ == "__main__":
    
    pass