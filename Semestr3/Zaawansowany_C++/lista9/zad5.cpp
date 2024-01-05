#include <iostream>
#include <filesystem>
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

        uintmax_t totalSize = 0;

        for (const auto& entry : filesystem::recursive_directory_iterator(directory)) {
            if (entry.is_regular_file()) {
                totalSize += entry.file_size();
            }
        }

        cout << "Suma rozmiarów plików: " << totalSize << " bajtów" << endl;
    } catch (const exception& e) {
        cerr << "Wystąpił błąd: " << e.what() << endl;
        return 1;
    }

    return 0;
}
