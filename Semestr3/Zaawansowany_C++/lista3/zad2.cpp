#include <limits>
#include <iostream>
using namespace std; 

int main(){
    cout << "Najmniejsza liczba dodatnia float i double najblizsza 0: " << numeric_limits<float>::lowest() << " " << numeric_limits<double>::lowest() << endl;
    cout << "Maksymalne wartosci dla double i float: " << numeric_limits<double>::max() << " " << numeric_limits<float>::max() << endl;
    cout << "Roznica miedzy 1 a najmniejsza liczba >1 dla double i float: " << numeric_limits<double>::epsilon() << " " << numeric_limits<float>::epsilon() << endl;
}