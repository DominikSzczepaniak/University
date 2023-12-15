#include <iostream>
#include <regex>
#include <string>

int main() {
    std::string input;

    std::cout << "Podaj godzinę: ";
    std::getline(std::cin, input);

    std::regex pattern(R"((2[0-3]|1[0-9]|0?[0-9]):([0-5][0-9])(:([0-5][0-9]))?)");


    if (std::regex_match(input, pattern)) {
        std::cout << "Wprowadzona godzina jest poprawna." << std::endl;
    } else {
        std::cout << "Wprowadzona godzina jest niepoprawna." << std::endl;
    }

    return 0;
}
