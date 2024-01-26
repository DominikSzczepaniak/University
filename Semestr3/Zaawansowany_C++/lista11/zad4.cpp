#include <iostream>

template<size_t N>
struct InnerProduct {
    static double compute(double *x, double *y) {
        return x[N-1] * y[N-1] + InnerProduct<N-1>::compute(x, y);
    }
};

template<>
struct InnerProduct<1> {
    static double compute(double *x, double *y) {
        return x[0] * y[0];
    }
};

template<size_t N, typename T = double>
T inner(T *x, T *y) {
    T result = 0;
    for (size_t i = 0; i < N; ++i) {
        result += x[i] * y[i];
    }
    return result;
}

int main() {
    constexpr size_t N = 3;
    double x[N] = {1.0, 2.0, 3.0};
    double y[N] = {4.0, 5.0, 6.0};

    std::cout << "Inner product: " << inner<N>(x, y) << std::endl;
    std::cout << "Inner product: " << InnerProduct<N>::compute(x, y) << std::endl;

    return 0;
}