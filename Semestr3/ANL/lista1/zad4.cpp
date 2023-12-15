#include <cmath>
#include <iostream>
using namespace std;
int main(){
    double wartosci[51];
    wartosci[0] = 1;
    wartosci[1] = -1.0/9.0;
    for(int i = 2; i<=50; i++){
        wartosci[i] = 80/9 * wartosci[i-1] + wartosci[i-2];
    }
    cout <<fixed;
    for(int i = 0; i<=50; i++){
        cout << i << ": " << wartosci[i] << endl;
    }
}