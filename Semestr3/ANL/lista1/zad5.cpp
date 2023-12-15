#include <cmath>
#include <iostream>
using namespace std;

int main(){
    double I[21];
    I[0] = log(2024.0/2023.0);
    cout << fixed;
    for(int i = 1; i<=20; i++){
        I[i] = 1.0/double(i) - 2023.0 * I[i-1];
    }
    for(int i = 0; i<=20; i++){
        cout << I[i] << endl;
    }
    //wyniki nie sa wiarygodne, poniewaz co chwile przekraczamy maksymalny rozmiar double i zmieniamy znak.

}