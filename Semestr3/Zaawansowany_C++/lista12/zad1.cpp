#include <iostream>
#include <thread>
#include <chrono>
#include <vector>
#include <cstdlib>
#include <ctime>
bool end = false;
void threadFunction(const std::string& threadName) {
    while (!end) {
        std::cout << "Wątek " << threadName << " działa." << std::endl;
        std::chrono::milliseconds sleepTime(rand() % 501 + 500);
        std::this_thread::sleep_for(sleepTime);
    }
}

int main() {
    std::srand(std::time(0));
    std::vector<std::thread> threads;
    for (int i = 0; i < 5; ++i) {
        std::string threadName = "Watek" + std::to_string(i);
        threads.emplace_back(threadFunction, threadName);
    }
    std::this_thread::sleep_for(std::chrono::seconds(5));
    end = true;
    for (auto& thread : threads) {
        thread.join();
    }

    return 0;
}
