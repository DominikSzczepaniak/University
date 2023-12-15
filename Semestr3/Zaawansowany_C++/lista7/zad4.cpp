#include <iostream>
#include <complex>
#include <cmath>

const double euler_gamma = 0.5772156649; 
std::complex<double> euler_gamma_function(std::complex<double> z, int iterations) {
    std::complex<double> result = 1.0 / z;

    for (int n = 1; n <= iterations; ++n) {
        result *= pow((1+1.0 / static_cast<double>(n)), z) / (1.0 + z / static_cast<double>(n));
    }

    return result;
}

std::complex<double> inverse_euler_gamma_function(std::complex<double> z, int iterations) {
    std::complex<double> result = z * exp(euler_gamma * z);

    for (int n = 1; n <= iterations; ++n) {
        result *= (1.0 + z / static_cast<double>(n)) * exp(-z / static_cast<double>(n));
    }

    return result;
}

int main() {
    std::complex<double> z(2.0, 3.0); 

    std::complex<double> gamma_value = euler_gamma_function(z, 10000);

    std::complex<double> inverse_gamma_value = inverse_euler_gamma_function(z, 10000);

    std::cout << "Gamma(" << z << ") = " << gamma_value << std::endl;
    std::cout << "1/Gamma(" << z << ") = " << inverse_gamma_value << std::endl;
    std::complex<double> test = 1.0 / gamma_value;
    std::cout << test << std::endl;

    return 0;
}
