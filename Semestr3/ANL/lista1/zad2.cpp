#include <iostream>
#include <cmath>
using namespace std;

double func(double x){
    double pot = pow(x, 14);
    return 4046 * (sqrt(pot + 1.0) - 1.0) / pot;
}

int main(){
    double x = 0.001;
    cout << func(x) << endl;
}