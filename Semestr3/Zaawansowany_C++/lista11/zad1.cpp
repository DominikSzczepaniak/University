#include <array>
#include <iostream>

template <int N>
struct Lucas {
    static const int value = Lucas<N - 1>::value + Lucas<N - 2>::value;
};

template <>
struct Lucas<0> {
    static const int value = 2;
};

template <>
struct Lucas<1> {
    static const int value = 1;
};


int main() {
    constexpr int n = 41; 
    std::cout << "L(" << n << ") = " << Lucas<n>::value << std::endl;

    return 0;
}