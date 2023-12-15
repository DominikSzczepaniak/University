#include <iostream>
#include <cmath>
#include <iomanip>
using namespace std;

double f(double x){
    return 3*x*x*x + 2*x*x + x +1;
}

double fPrim(double x){
    return 9*x*x + 4*x + 1;
}

double fBis(double x){
    return 18*x + 4;
}

int main(){
    double xnm1 = 1;
    double xn = 1;
    double alfa = -0.78389;
    cout << setprecision(1000000);
    double p;
    for(int i = 0; i<5; i++){
        double xn1 = xn - (f(xn)/fPrim(xn)) - 1/2 * (fBis(xn)/fPrim(xn)) * (f(xn)/fPrim(xn))*(f(xn)/fPrim(xn)); 
        if(i >= 1){
            double epsn = xn-alfa;
            double epsnw1 = xn1-alfa;
            double epsnm1 = xnm1-alfa;
            p = log(abs(epsnw1/epsn)) / log(abs(epsn/epsnm1));
        }
        xnm1 = xn;
        xn = xn1;
    }
    cout << p << endl;

}