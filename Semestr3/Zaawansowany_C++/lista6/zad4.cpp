#include <iostream>
#include <fstream>
#include <vector>
#include <iterator>
#include <cctype> 
#include <algorithm>
using namespace std;
int main(int argc, char* argv[]) {
    if (argc != 2) {
        cerr << "Użycie: " << argv[0] << " <nazwa_pliku>" << endl;
        return 1;
    }

    ifstream file(argv[1]);
    if (!file.is_open()) {
        cerr << "Nie można otworzyć pliku: " << argv[1] << endl;
        return 1;
    }

    vector<int> histogram(26, 0);

    for_each(istream_iterator<char>(file), istream_iterator<char>(), [&](char c) {
        if (isalpha(c)) {
            if(tolower(c) - 'a' < 0 || tolower(c) - 'a' > 25)
                return;
            histogram[tolower(c) - 'a']++;
        }
    });

    file.close();

    char currentLetter = 'a';
    for (int count : histogram) {
        cout << currentLetter << " " << string(count/100, '#') << endl;
        currentLetter++;
    }

    return 0;
}
