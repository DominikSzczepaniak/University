#include <iostream>
#include <fstream>
#include <complex>
#include <cmath>

const double euler_gamma = 0.5772156649; 
std::complex<double> riemann_zeta(std::complex<double> z, int iterations) {
    std::complex<double> result = 0;

    for (int n = 1; n <= iterations; ++n) {
        result += (1.0/pow(static_cast<double>(n), z));
    }

    return result;
}

int main(){
    std::ofstream outputFile("riemann_zeta_values.csv");
    int iterations = 100; 
    double delta = 0.1;   
    outputFile << "real_part,real_value,imaginary_value" << std::endl;
    for (double real_part = 0.5; real_part <= 30.0; real_part += delta) {
        std::complex<double> z(real_part, 0.0);
        std::complex<double> zeta_value = riemann_zeta(z, iterations);

        outputFile << real_part << "," << zeta_value.real() << "," << zeta_value.imag() << std::endl;
    }

    outputFile.close();

    return 0;
}