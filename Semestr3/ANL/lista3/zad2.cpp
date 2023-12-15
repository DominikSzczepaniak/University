#include <iostream>
#include <cmath>
using namespace std;

void metoda_szkolna(double a, double b, double c) {
    double delta = b * b - 4 * a * c;
    double x1 = (-b - sqrt(delta)) / (2 * a);
    double x2 = (-b + sqrt(delta)) / (2 * a);
    cout << x1 << " " << x2 << endl;
}

void moja_metoda(double a, double b, double c){
    double delta = b * b - 4 * a * c;
    double x1 = (-b - sqrt(delta)) / (2 * a);
    double x2 = c / (a * x1);
    cout << x1 << " " << x2 << endl;
}

int main(){
    double a = 0.000000001;
    double b = 1000000000;
    double c = 0.000000001;
    // powinno być
    // x1 = -10^18 
    // x2 = -1*10^-18
    metoda_szkolna(a, b, c);
    moja_metoda(a, b, c);
    return 0;
}