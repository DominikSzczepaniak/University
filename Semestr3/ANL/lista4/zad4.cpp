// https://www.desmos.com/calculator
// szukamy przeciec
// czyli szukamy kiedy sie zeruje miedzy [-1.5, 0.5] oraz [0.5, 1.5]
#include <iostream>
#include <cmath>
double funkcja(double x){
    return x*x*x*x - log(x+4);
}
// Epsilon = 10^-8 => n = ceil(log2((b0-a0)/2Epsilon)) = ceil(log2(1/2*10^-8)) = ceil(log2(10^8)) = 27
const int OBROTY_PETLY = 27;
double bisekcja(double c, double d){
    double a = c;
    double b = d;
    for(int i = 0; i<OBROTY_PETLY; i++){
        double m = 0.5 * (a + b);
        double wartosc = funkcja(m);
        if(wartosc < 0){
            if(c < 0 && d < 0){
                b = m;
            }
            else{
                a = m;
            }
        }
        else{
            if(c < 0 && d < 0){
                a = m;
            }
            else{
                b = m;
            }
        }
    } 
    std::cout << a << " " << b << std::endl; 
    return 0.5*(a+b); 
}

int main(){
    //std::cout << "Miejsce zerowe 1: " << bisekcja(-1.5, -0.5) << " Miejsce zerowe 2: " << bisekcja(0.5, 1.5) << std::endl;
    bisekcja(-1.5, -0.5);
    bisekcja(0.5, 1.5);
}