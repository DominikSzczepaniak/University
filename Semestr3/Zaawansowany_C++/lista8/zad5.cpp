#include <iostream>
#include <fstream>
#include <regex>
#include <string>

void findAndPrintLinks(const std::string& filename) {
    std::ifstream file(filename);
    if (!file.is_open()) {
        std::cerr << "Nie mozna otworzyc pliku: " << filename << std::endl;
        return;
    }
    std::string fileContent((std::istreambuf_iterator<char>(file)), std::istreambuf_iterator<char>());

    std::regex linkRegex(R"(<a[^>]*\s+href=["'](.*?)["'][^>]*>)");
    auto words_begin = std::sregex_iterator(fileContent.begin(), fileContent.end(), linkRegex);
    auto words_end = std::sregex_iterator();

    for (std::sregex_iterator i = words_begin; i != words_end; ++i) {
        std::smatch match = *i;
        std::string hrefValue = match[1].str();
        std::cout << hrefValue << std::endl;
    }
}

int main(int argc, char* argv[]) {
    if (argc < 2) {
        std::cerr << "Uzycie: " << argv[0] << " <filename1> [<filename2> ...]" << std::endl;
        return 1;
    }

    for (int i = 1; i < argc; ++i) {
        findAndPrintLinks(argv[i]);
    }

    return 0;
}
