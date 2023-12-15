#include <cmath>
#include <iostream>
using namespace std;
enum class Imię : uint16_t {
  Jan,
  Piotr,
  Paweł,
  Anna,
  Maria,
  Ewa,
};

void wyslijKomunikat(const string& komunikat, Imię imię) {
    switch (imię) {
        case Imię::Jan:
            cout << komunikat << "Janku "  << endl;
            break;
        case Imię::Piotr:
            cout << komunikat << "Piotrku "  << endl;
            break;
        case Imię::Paweł:
            cout <<komunikat <<  "Pawle "  << endl;
            break;
        case Imię::Anna:
            cout << komunikat << "Anno "  << endl;
            break;
        case Imię::Maria:
            cout << komunikat << "Mario "  << endl;
            break;
        case Imię::Ewa:
            cout << komunikat << "Ewo "  << endl;
            break;
        default:
            cout << "zle imie" << endl;
        }
}

int main(){
    wyslijKomunikat("czesc", Imię::Jan);
}