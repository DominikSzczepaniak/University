#include <iostream>

template<int a, int b>
struct GCD {
    static constexpr int value = GCD<b, a % b>::value;
};

template<int a>
struct GCD<a, 0> {
    static constexpr int value = a;
};

int main() {
    constexpr int a = 48; 
    constexpr int b = 18; 
    std::cout << "GCD(" << a << ", " << b << ") = " << GCD<a, b>::value << std::endl;

    return 0;
}