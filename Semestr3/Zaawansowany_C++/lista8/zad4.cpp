#include <iostream>
#include <regex>
#include <string>

bool sprawdzLiczbeZespolona(const std::string& liczbaZespolona) {
    std::regex wzorzec("\\((-?\\d+(\\.\\d+)?[-+]\\d+(\\.\\d+)?[iI])\\)");

    return std::regex_match(liczbaZespolona, wzorzec);
}

int main() {
    std::string test1 = "(12+3I)";
    std::string test2 = "(7.4-0.5i)";
    std::string test3 = "(2+0.01i)";
    std::string test4 = "3+4I";
    std::string test5 = "(3,14-2,72i)";
    std::string test6 = "(5.7i)";

    std::cout << test1 << " - " << (sprawdzLiczbeZespolona(test1) ? "Poprawne" : "Błędne") << std::endl;
    std::cout << test2 << " - " << (sprawdzLiczbeZespolona(test2) ? "Poprawne" : "Błędne") << std::endl;
    std::cout << test3 << " - " << (sprawdzLiczbeZespolona(test3) ? "Poprawne" : "Błędne") << std::endl;
    std::cout << test4 << " - " << (sprawdzLiczbeZespolona(test4) ? "Poprawne" : "Błędne") << std::endl;
    std::cout << test5 << " - " << (sprawdzLiczbeZespolona(test5) ? "Poprawne" : "Błędne") << std::endl;
    std::cout << test6 << " - " << (sprawdzLiczbeZespolona(test6) ? "Poprawne" : "Błędne") << std::endl;
    std::string in;
    std::cin >> in;
    std::cout << (sprawdzLiczbeZespolona(in) ? "Poprawne" : "Błędne") << std::endl;
    return 0;
}
