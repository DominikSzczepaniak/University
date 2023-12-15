#include <iostream>
#include <regex>
#include <string>

bool isValidCityName(const std::string& input) {
    std::regex pattern("^[A-Z][a-z]*(?:-[A-Z][a-z]*)*$");
    return std::regex_match(input, pattern);
}

int main() {
    std::string input;

    std::cout << "Podaj nazwe miejscowosci: ";
    std::getline(std::cin, input);

    if (isValidCityName(input)) {
        std::cout << "Wprowadzona nazwa miejscowosci jest poprawna." << std::endl;
    } else {
        std::cout << "Wprowadzona nazwa miejscowosci jest niepoprawna." << std::endl;
    }

    return 0;
}
