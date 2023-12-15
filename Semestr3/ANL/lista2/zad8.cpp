#include <iostream>
#include <cmath>

using namespace std;
//1-cos(17x) zaokragla do 0 bo ucina miejsca znaczace
int main(){
    for(int i = 11; i<=20; i++){
        double x = pow(10, -i);
        double sin_x = x * (17.0/2.0);
        double sin_val = sin(sin_x);
        sin_val = sin_val * sin_val;
        cout << 28.0 * sin_val / x*x << endl;
    }
}