#include <iostream>
#include <vector>
#include <utility>
#include <functional>
using namespace std;

int main() {
    vector<pair<int, int>> values = {{5, 2}, {8, 3}, {10, 4}, {4, 2}, {7, -1}};

    // Deklaracja lambdy przed jej wykorzystaniem
    function<int(int, int)> binomialCoefficient;
    binomialCoefficient = [&binomialCoefficient](int n, int k) -> int {
        if (k == 0 || k == n) {
            return 1;
        }
        return binomialCoefficient(n - 1, k - 1) + binomialCoefficient(n - 1, k);
    };

    for (const auto &pair : values) {
        int n = pair.first;
        int k = pair.second;
        if (n < 0 || k < 0 || k > n) {
            cout << "Nieprawidłowe wartości n = " << n << ", k = " << k << ". Wartości muszą być liczbami naturalnymi oraz k musi być mniejsze lub równe n." << endl;
            continue;
        }
        int result = binomialCoefficient(n, k);
        cout << "Współczynnik dwumianowy (" << n << " po " << k << ") = " << result << endl;
    }

    return 0;
}
