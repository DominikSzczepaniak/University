// Dominik Szczepaniak
// 337456
// MBa 
// (Mateusz Basiak)

#include <iostream>

using namespace std;

int main(){
    int a, b;
    cin >> a >> b;
    int start = (a + 2023) / 2024 * 2024;
    for (int i = start; i <= b; i += 2024) {
        cout << i << " ";
    }
    cout << endl;
}