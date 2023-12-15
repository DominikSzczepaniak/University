#include <iostream>
#include <cmath>

using namespace std;

int main(){
    // double end = 1e-6 * 1/2;
    // for(int i = 1; i<=3000; i++){
    //     double lewo = 1.0 / (i+1.0) * pow((1.0 - (2.0 / M_E)), i);
    //     if(lewo < end){
    //         cout << i << endl;
    //         break;
    //     }
    // }
    double end = 1e-6 * 1/2;
    for(int i = 1; i<=3000; i++){
        double lewo = pow( (1.0 - (2.0 / M_E)), i) / (2.0 / M_E);
        if(lewo < end){
            cout << i << endl;
            break;
        }
    }
}