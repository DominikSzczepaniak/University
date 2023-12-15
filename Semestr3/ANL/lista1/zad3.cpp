#include <cmath>
#include <iostream>

using namespace std;

float func(float x){
    return float(14) * (float(1) - (cos(float(17)*x))) / (x*x);
}

// 14 * (1-cos(17 * x)) / x^2 = (14-14cos(17x)) / x^2 = 14/x^2 - 14cos(17x)/x^2

double func(double x){
    return (double)14.0 * ((double)1.0 - (cos((double)17.0*x))) / (x*x);
    //return ((double)14.0/(x*x)) - (14.0 * (cos((double)17.0*x)) / (x*x));
}

int main(){
    for(int i = 11; i<=20; i++){
        double x1 = pow(10, -i);
        cout << "double precision: " << func((double)(pow(10, -i))) << endl;
        cout << "single precision: " << func(float(pow(10, -i))) << endl;
    }
}