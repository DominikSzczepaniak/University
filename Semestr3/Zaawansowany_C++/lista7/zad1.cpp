#include <random>
#include <cmath>
#include <iostream>

double custom_distribution(double a, double b) {
    static std::random_device rd;
    static std::mt19937 gen(rd());
    std::uniform_real_distribution<> dis(0, 1);

    double mid = (a + b) / 2.0;
    double range = b - a;
    double raw_random = dis(gen);
    double transformed_random = std::sin((raw_random - 0.5) * M_PI);

    return mid + (transformed_random / 2.0) * range;
}

int main() {
    for(int i = 0; i < 10; ++i) {
        std::cout << custom_distribution(0, 10) << std::endl;
    }

    return 0;
}