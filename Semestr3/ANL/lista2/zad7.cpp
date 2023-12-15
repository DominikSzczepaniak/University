#include <cmath>
#include <iostream>
using namespace std;

long double potega(long double x, int a){
    long double ans = 1;
    for(int i = 1; i<=a; i++){
        ans *= x;
    }
    return ans;
}

int main(){
    long double x = 0.001;
    long double pierw = sqrt(potega(x, 14) + 1);
    long double wynik = 4046 / (pierw + 1);
    cout << wynik << endl;
}