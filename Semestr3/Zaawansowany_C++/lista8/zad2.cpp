#include <iostream>
#include <regex>
#include <string>

bool isValidDate(const std::string& input) {
    std::regex dateRegex(
        "^(0[1-9]|1[0-9]|2[0-8])-(0[1-9]|1[0-2])-(\\d{4})$"
        "|^(29|30)-(0[13-9]|1[0-2])-(\\d{4})$"
        "|^31-(0[13578]|1[02])-(\\d{4})$"
    );
    return std::regex_match(input, dateRegex);
}

int main() {
    std::string input;

    std::cout << "Podaj date: ";
    std::getline(std::cin, input);

    if (isValidDate(input)) {
        std::cout << "Wprowadzona data jest poprawna." << std::endl;
    } else {
        std::cout << "Wprowadzona data jest niepoprawna." << std::endl;
    }

    return 0;
}
