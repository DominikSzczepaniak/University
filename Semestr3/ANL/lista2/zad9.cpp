#include <cmath>
#include <iostream>
#include <iomanip>

using namespace std;

void pierwsza_wersja(){
    double wyniki[40];
    wyniki[1] = 2;
    for(int k = 2; k<=40; k++){
        wyniki[k] = pow(2,k-1) * sqrt(2 * (1 - sqrt(1 - ((wyniki[k-1] / pow(2, k-1)) * (wyniki[k-1] / pow(2, k-1))) )));
    }
    int licznik = 1;
    for(auto k : wyniki){
        
        cout << licznik << " " << k << endl;
        licznik++;
    }
}

void druga_wersja(){
    double wyniki[400];
    wyniki[1] = 2;
    for(int k = 2; k<400; k++){
        wyniki[k] = sqrt(2 * (wyniki[k-1] * wyniki[k-1]) / (1 + sqrt(1 - ((wyniki[k-1]/pow(2, k-1))*(wyniki[k-1]/pow(2, k-1))) )));
    }
    cout << fixed;
    cout << setprecision(15);
    for(int i = 1; i<=399; i++){
        cout << i << ": " << wyniki[i] << endl;
    }
}

int main(){
    // pierwsza_wersja();
    druga_wersja();
}