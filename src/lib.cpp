#include <iostream>
#include <windows.h>
#include <cstring> // 用于strcmp函数
#include <winioctl.h>
#include <vector>
#include <strsafe.h>
#include <map>
#include <sstream>
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
    __declspec(dllexport) // 递归计算目录大小
long long CalculateDirectorySize(const std::wstring& directoryPath, std::map<std::wstring, long long>& sizeMap) {
    WIN32_FIND_DATAW findFileData;  // 使用宽字符版本的结构体
    HANDLE hFind = INVALID_HANDLE_VALUE;
    long long totalSize = 0;
    
    // 准备搜索路径
    std::wstring searchPath = directoryPath + L"\\*";
    
    // 使用宽字符版本的FindFirstFile
    hFind = FindFirstFileW(searchPath.c_str(), &findFileData);
    
    if (hFind == INVALID_HANDLE_VALUE) {
        return 0;
    }
    
    // 遍历目录中的所有文件和子目录
    do {
        // 跳过当前目录和上级目录
        if (wcscmp(findFileData.cFileName, L".") != 0 && 
            wcscmp(findFileData.cFileName, L"..") != 0) {
            
            // 构建完整路径
            std::wstring fullPath = directoryPath + L"\\" + findFileData.cFileName;
            
            // 如果是目录
            if (findFileData.dwFileAttributes & FILE_ATTRIBUTE_DIRECTORY) {
                // 递归计算子目录大小
                long long dirSize = CalculateDirectorySize(fullPath, sizeMap);
                sizeMap[fullPath] = dirSize;
                totalSize += dirSize;
            } 
            // 如果是文件
            else {
                LARGE_INTEGER fileSize;
                fileSize.LowPart = findFileData.nFileSizeLow;
                fileSize.HighPart = findFileData.nFileSizeHigh;
                
                sizeMap[fullPath] = fileSize.QuadPart;
                totalSize += fileSize.QuadPart;
            }
        }
    } while (FindNextFileW(hFind, &findFileData) != 0);  // 使用宽字符版本的FindNextFile
    
    FindClose(hFind);
    return totalSize;
}

};


int main() {
    std::map<std::wstring, long long> sizeMap;
    
    // 计算目录大小
    long long totalSize = CalculateDirectorySize(L"D:\\123_softs\\", sizeMap);
    
    // 输出结果
    std::wcout << L"总大小: " << totalSize << L" 字节" << std::endl;
    
    // 使用迭代器而不是range-based for
    for (std::map<std::wstring, long long>::iterator it = sizeMap.begin(); it != sizeMap.end(); ++it) {
        double percentage = (totalSize > 0) ? (double)it->second / totalSize * 100.0 : 0.0;
        std::wcout << L"路径: " << it->first << std::endl;
        std::wcout << L"大小: " << it->second << L" 字节" << std::endl;
        std::wcout << L"占比: " << percentage << L"%" << std::endl;
        std::wcout << L"---------------------" << std::endl;
    };
    return 0;
}