#include <iostream>
#include <limits>
using namespace std;

int main(){
    cout << numeric_limits<long long int>::max() << endl;
    cout << numeric_limits<long long int>::min() << endl; 
    cout << "Ilość bitow: " << sizeof(numeric_limits<long long int>::max())*8 << endl;
    // 9 * 10^18 = 19 liczb 
}