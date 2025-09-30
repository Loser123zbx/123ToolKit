#include <iostream>  
#include <stdlib.h>  
#include <string.h>

class Log{
    /* 日志类 */
    public:
        enum Level {
            Info = 0,
            Debug = 1,
            Warning = 2,
            Error = 3
        };
        
        Level level;
        std::string message;
        
        Log(Level lvl, const std::string& msg) : level(lvl), message(msg) {}
        
        void log(Level lvl, const std::string& msg) {
            std::cout << (lvl == Info ? "[Info] " : 
                         lvl == Debug ? "[Debug] " : 
                         lvl == Warning ? "[Warning] " : 
                         "[Error] ") << msg << std::endl;
        }
};

class ProgressBar {
    /* 进度条 */
    public:

        int total;
        int current;

        ProgressBar(int total) : total(total), current(0) {}

        void update(int current) {
            this->current = current;
            float progress = (float)current / total;
            int barWidth = 50;
            std::cout << "[";
            int pos = barWidth * progress;
            for (int i = 0; i < barWidth; ++i) {
                if (i < pos) std::cout << "=";
                else if (i == pos) std::cout << ">";
                else std::cout << " ";

            }
        }
        void finish() {
            std::cout << "] " << current << "/" << total << std::endl;  
        }
        
};

