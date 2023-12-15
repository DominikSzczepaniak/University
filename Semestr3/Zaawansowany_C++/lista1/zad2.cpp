#include <iostream>
#include <string>
using namespace std;
int main(){
    string adres = R"(Instytut Informatyki Uniwersytetu Wrocławskiego
Fryderyka Joliot-Curie 15
50-383 Wrocław)";
    string programy = R"(C:\Program Files\)";
    string znaki = R"nowekonczenie( „cudzysłów dwa”
    'cudzysłów jeden'
    (nawias)
    "(nawias cudzyslow)")nowekonczenie";
    cout << adres << endl;
    cout << programy << endl;
    cout << znaki << endl;
}