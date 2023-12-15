#include <iostream>
#include <cmath>
#include <sstream>
#include <string>
using namespace std;

int main(){
    string data;
    cin >> data;
    istringstream ss(data);
    int dzien, miesiac, rok;
    char separator;
    ss >> dzien >> separator >> miesiac >> separator >> rok;
    if(ss.fail() || separator != '.' || ss.get() != EOF){
        cout << "zly format daty" << endl;
    }
    string miesiac_string;
    switch (miesiac) {
        case 1:
            miesiac_string = "stycznia ";
            break;
        case 2:
            miesiac_string = "lutego ";
            break;
        case 3:
            miesiac_string = "marca";
            break;
        case 4:
            miesiac_string = "kwietnia ";
            break;
        case 5:
            miesiac_string = "maja ";
            break;
        case 6:
            miesiac_string = "czerwca ";
            break;
        case 7:
            miesiac_string = "lipca ";
            break;
        case 8:
            miesiac_string = "sierpnia";
            break;
        case 9:
            miesiac_string = "wrzesina ";
            break;
        case 10:
            miesiac_string = "pazdziernika ";
            break;
        case 11:
            miesiac_string = "listopada ";
            break;
        case 12:
            miesiac_string = "grudnia ";
            break;
        default:
            std::cout << "zly miesiac" << std::endl;
            return 1;
    }
    cout << dzien << " " << miesiac_string << " " << rok << endl;

}