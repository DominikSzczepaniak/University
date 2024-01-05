#include <iostream>
#include <filesystem>
#include <algorithm>
using namespace std;
int main() {
    cout << "Podaj ścieżkę do katalogu: ";
    string directoryPath;
    getline(cin, directoryPath);

    try {
        filesystem::path directory(directoryPath);

        if (!filesystem::exists(directory) || !filesystem::is_directory(directory)) {
            cerr << "Podany katalog nie istnieje lub nie jest katalogiem." << endl;
            return 1;
        }

        cout << "Nazwa kanoniczna katalogu: " << filesystem::canonical(directory) << endl;

        for (const auto& entry : filesystem::directory_iterator(directory)) {
            if (entry.is_directory()) {
                cout << "[Katalog] " << entry.path().filename() << endl;
            } else if (entry.is_regular_file()) {
                cout << "[Plik] " << entry.path().filename() << endl;
            }
        }
    } catch (const exception& e) {
        cerr << "Wystąpił błąd: " << e.what() << endl;
        return 1;
    }

    return 0;
}
