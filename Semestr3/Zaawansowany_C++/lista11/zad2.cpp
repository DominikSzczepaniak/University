#include <iostream>

template<int N>
struct Factorial {
    static constexpr int value = N * Factorial<N - 1>::value;
};

template<>
struct Factorial<0> {
    static constexpr int value = 1;
};

template<int N, int K>
struct BinomialCoefficient {
    static_assert(K <= N, "K nie moze byc wieksze niz N");
    static constexpr int value = Factorial<N>::value / (Factorial<K>::value * Factorial<N - K>::value);
};

int main() {
    constexpr int n = 8;
    constexpr int k = 3;
    std::cout << "C(" << n << ", " << k << ") = " << BinomialCoefficient<n, k>::value << std::endl;
}