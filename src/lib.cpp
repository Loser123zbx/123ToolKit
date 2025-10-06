#include <iostream>
#include <windows.h>
#include <cstring> // 用于strcmp函数
#include <winioctl.h>
#include <vector>
#include <strsafe.h>
#pragma comment(lib, "User32.lib")

extern "C"{ 

    __declspec(dllexport) double getDiskFreeSpace(const char* path, const char* mode) {
        ULARGE_INTEGER freeBytesAvailable, totalNumberOfBytes, totalNumberOfFreeBytes;

        // 调用GetDiskFreeSpaceExA获取磁盘空间信息
        try{
        if (GetDiskFreeSpaceExA(path, &freeBytesAvailable, &totalNumberOfBytes, &totalNumberOfFreeBytes)) {
                return (double)(totalNumberOfFreeBytes.QuadPart);
            };
        }
        catch (const std::exception& e) {
            std::cerr << "Exception caught: " << e.what() << std::endl;
            return -1;
        };
    };

    __declspec(dllexport) double getDirUsedSpace(const char* path) {
        // 获取目录大小
        // ..
        return 0;

    };

    __declspec(dllexport) double convertToMiB(double size) {
        //将B转换到MiB
        return size / (1024.0 * 1024.0);
    };

    __declspec(dllexport) double convertToGiB(double size) {
        //将B转换到GiB
        return size / (1024.0 * 1024.0 * 1024.0);
    };

    __declspec(dllexport) double convertToTiB(double size) {
        //将B转换到TiB
        return size / (1024.0 * 1024.0 * 1024.0 * 1024.0);
    };
};

int main() {
    std::cout << "Hello World!" << std::endl;
    return 0;
}