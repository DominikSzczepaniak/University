#include <iostream>
#include <vector>
#include <random>
#include <chrono>
#include <cmath>
using namespace std;
double randomValue() {
    static random_device rd;
    static mt19937 gen(rd());
    uniform_real_distribution<double> dist(0.5, 2.0);
    return dist(gen);
}

template <typename T>
T multiplicateForIndex(const vector<vector<T>>& matrix, int y, int x){
    T ans = 0;
    for(size_t i = 0; i < matrix.size(); i++){
        ans += matrix[y][i] * matrix[i][x];
    }
    return ans;
}

template <typename T>
double measureTimeForMatrixSquared(const vector<vector<T>>& matrix) {
    auto start = chrono::high_resolution_clock::now();

    vector<vector<T>> result(matrix.size(), vector<T>(matrix[0].size()));
    for (size_t i = 0; i < matrix.size(); i++) {
        for (size_t j = 0; j < matrix[0].size(); j++) {
            result[i][j] = multiplicateForIndex(matrix, i, j);
        }
    }

    auto end = chrono::high_resolution_clock::now();
    chrono::duration<double> duration = end - start;
    return duration.count();
}
template <typename T>
void averageTime(const vector<vector<T>>& matrix, int repetitions){
    double totalTime = 0.0;
    for (int i = 0; i < repetitions; ++i) {
        totalTime += measureTimeForMatrixSquared(matrix);
    }
    double averageTime = totalTime / static_cast<double>(repetitions);
    cout << "Matrix size: " << matrix.size() << "x" << matrix.size() << endl;
    cout << "Average time for squaring: " << averageTime << " seconds" << endl;
}

int main() {
    const int sizes[] = {10, 100, 1000};
    for (int size : sizes) {
        vector<vector<double>> matrix(size, vector<double>(size));
        for (size_t i = 0; i < size; ++i) {
            for (size_t j = 0; j < size; ++j) {
                matrix[i][j] = randomValue();
            }
        }
        switch(size){
            case 10:
                averageTime(matrix, 1000);
                break;
            case 100:
                averageTime(matrix, 100);
                break;
            case 1000:
                averageTime(matrix, 1);
        }
    }

    return 0;
}
