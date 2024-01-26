#include <iostream>
#include <thread>
#include <chrono>

int main() {
    std::this_thread::sleep_for(std::chrono::seconds(5));
    std::cout << "Program zakończy się za 5 sekund." << std::endl;

    std::this_thread::sleep_for(std::chrono::seconds(3));
    std::cout << "Program zakończy się za 3 sekundy." << std::endl;

    std::this_thread::sleep_for(std::chrono::seconds(1));
    std::cout << "Program zakończy się za 1 sekundę." << std::endl;

    std::this_thread::sleep_for(std::chrono::seconds(1));

    for (int i = 0; i < 10; ++i) {
        std::cout << "Wykonywanie programu... Czas: " << i + 1 << " sekunda." << std::endl;
        std::this_thread::sleep_for(std::chrono::seconds(1));
    }
    std::cout << "Program zakończony." << std::endl;
    return 0;
}
