#include <iostream>
#include <filesystem>
#include <iomanip>
#include <chrono>
using namespace std;
void printFileDetails(const filesystem::path& filePath) {
    if (filesystem::exists(filePath)) {
        cout << "Informacje o pliku/folderze: " << filePath << endl;
        cout << "Ścieżka kanoniczna: " << filesystem::canonical(filePath) << endl;
        if(filesystem::is_regular_file(filePath))
            cout << "Rozmiar: " << filesystem::file_size(filePath) << " bajtów" << endl;
        cout << "Czy jest katalogiem? " << boolalpha << filesystem::is_directory(filePath) << endl;
        cout << "Czy jest plikiem? " << boolalpha << filesystem::is_regular_file(filePath) << endl;
        cout << "Czy jest pustym plikiem? " << boolalpha << filesystem::is_empty(filePath) << endl;
        cout << "Czy jest dowiązaniem symbolicznym? " << boolalpha << filesystem::is_symlink(filePath) << endl;
        // cout << "Data ostatniej modyfikacji: " << filesystem::last_write_time(filePath) << endl; // NIE DZIAŁA
        // https://omegaup.com/docs/cpp/en/cpp/filesystem/last_write_time.html
        // https://en.cppreference.com/w/cpp/filesystem/last_write_time

    } else {
        cerr << "Plik/folder o nazwie " << filePath << " nie istnieje." << endl;
    }
}

int main(int argc, char* argv[]) {
    if (argc < 2) {
        cerr << "Użycie: " << argv[0] << " <nazwa_pliku/folderu1> <nazwa_pliku/folderu2> ..." << endl;
        return 1;
    }

    for (int i = 1; i < argc; ++i) {
        filesystem::path fileOrFolder(argv[i]);
        printFileDetails(fileOrFolder);
    }

    return 0;
}
