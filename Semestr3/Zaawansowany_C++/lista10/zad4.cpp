#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <locale>
#include <clocale>

int main() {
    std::vector<std::wstring> names = {L"żółw", L"źrebak", L"zając", L"jaśmin", L"jagoda", L"jabłoń"};

    setlocale(LC_ALL, "pl_PL");

    std::sort(names.begin(), names.end(), [](const std::wstring& a, const std::wstring& b) {
        return std::locale()(a, b);
    });

    for (const auto& name : names) {
        std::wcout << name << std::endl;
    }

    return 0;
}