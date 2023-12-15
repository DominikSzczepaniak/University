#include <iostream>
#include <cmath>

using namespace std;

int main(){
    double lewo = 0;
    double prawo = 0;
    for(int i = 10; i<10000; i++){
        lewo += pow((1.0 - (2.0 / M_E)), i) / i;
        prawo += pow((1.0 - (2.0 / M_E)), i);
    }
    // prawo *= 10.0/11.0;
    cout << lewo << endl;
    cout << prawo << endl;

}