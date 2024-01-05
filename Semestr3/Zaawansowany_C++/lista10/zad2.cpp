#include <iostream>
#include <iomanip>
#include <locale>
#include <clocale>
#include <ctime>
using namespace std;
int main() {
    setlocale(LC_ALL, "pl_PL.UTF-8");

    int liczbyCalkowite1[] = {123, 456, 789};
    double liczbyZmiennopozycyjne1[] = {12.34, 56.78, 90.12};
    double wartosciPieniezne1[] = {1234.56, 7890.12, 3456.78};

    std::wcout << L"Lokalizacja 1: Polski" << std::endl;
    for (int i = 0; i < 3; ++i) {
        std::wcout << L"Liczba całkowita: " << liczbyCalkowite1[i] << std::endl;
        std::wcout << L"Liczba zmiennopozycyjna: " << std::fixed << std::setprecision(2) << liczbyZmiennopozycyjne1[i] << std::endl;
        std::wcout << L"Wartość pieniężna: " <<  std::put_money(wartosciPieniezne1[i]) << std::endl;
        std::wcout << L"------------------------" << std::endl;
    }

    std::time_t czasTeraz1 = std::time(nullptr);
    std::tm* dataGodzina1 = std::localtime(&czasTeraz1);
    std::wcout << L"Bieżąca data i godzina: " << std::put_time(dataGodzina1, L"%c") << std::endl;

    setlocale(LC_ALL, "en_US.UTF-8");

    int liczbyCalkowite2[] = {321, 654, 987};
    double liczbyZmiennopozycyjne2[] = {98.76, 54.32, 21.09};
    double wartosciPieniezne2[] = {6543.21, 1098.76, 5432.10};

    std::wcout << L"Lokalizacja 2: Angielski (Stany Zjednoczone)" << std::endl;
    for (int i = 0; i < 3; ++i) {
        std::wcout << L"Liczba całkowita: " << liczbyCalkowite2[i] << std::endl;
        std::wcout << L"Liczba zmiennopozycyjna: " << std::fixed << std::setprecision(2) << liczbyZmiennopozycyjne2[i] << std::endl;
        std::wcout << L"Wartość pieniężna: " <<  std::put_money(wartosciPieniezne2[i]) << std::endl;
        std::wcout << L"------------------------" << std::endl;
    }

    std::time_t czasTeraz2 = std::time(nullptr);
    std::tm* dataGodzina2 = std::localtime(&czasTeraz2);
    std::wcout << L"Bieżąca data i godzina: " << std::put_time(dataGodzina2, L"%c") << std::endl;

    setlocale(LC_ALL, "de_DE.UTF-8");

    int liczbyCalkowite3[] = {555, 888, 111};
    double liczbyZmiennopozycyjne3[] = {23.45, 67.89, 10.11};
    double wartosciPieniezne3[] = {1111.22, 8888.99, 345.67};

    std::wcout << L"Lokalizacja 3: Niemiecki" << std::endl;
    for (int i = 0; i < 3; ++i) {
        std::wcout << L"Liczba całkowita: " << liczbyCalkowite3[i] << std::endl;
        std::wcout << L"Liczba zmiennopozycyjna: " << std::fixed << std::setprecision(2) << liczbyZmiennopozycyjne3[i] << std::endl;
        std::wcout << L"Wartość pieniężna: " <<  std::put_money(wartosciPieniezne3[i]) << std::endl;
        std::wcout << L"------------------------" << std::endl;
    }

    std::time_t czasTeraz3 = std::time(nullptr);
    std::tm* dataGodzina3 = std::localtime(&czasTeraz3);
    std::wcout << L"Bieżąca data i godzina: " << std::put_time(dataGodzina3, L"%c") << std::endl;

    return 0;
}
