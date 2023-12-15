#include <iostream>
#include <fstream>
#include <random>

int main() {
    std::random_device rd;
    std::mt19937 generator(rd());

    // rozkładem jednostajnym
    std::uniform_real_distribution<double> uniformDistribution(0.0, 1.0);
    std::ofstream uniformFile("liczby_jednostajne.csv");
    for (int i = 0; i < 1000; ++i) {
        double randomValue = uniformDistribution(generator);
        uniformFile << randomValue << "\n";
    }
    uniformFile.close();

    // rozkładem dwumianowym
    std::binomial_distribution<int> binomialDistribution(10, 0.5); 
    std::ofstream binomialFile("liczby_dwumianowe.csv");
    for (int i = 0; i < 1000; ++i) {
        int randomValue = binomialDistribution(generator);
        binomialFile << randomValue << "\n";
    }
    binomialFile.close();

    // rozkładem normalnym
    std::normal_distribution<double> normalDistribution(0.0, 1.0);
    std::ofstream normalFile("liczby_normalne.csv");
    for (int i = 0; i < 1000; ++i) {
        double randomValue = normalDistribution(generator);
        normalFile << randomValue << "\n";
    }
    normalFile.close();

    return 0;
}
