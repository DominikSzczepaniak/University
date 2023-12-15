#include <iostream>
#include <fstream>
#include <random>
#include <vector>
#include <map>
using namespace std;

vector<char> litery = {'E', 'T', 'A', 'O', 'I', 'N', 'S', 'R', 'H', 'D', 'L', 'U', 'C', 'M', 'F', 'Y', 'W', 'G', 'P', 'B', 'V', 'K', 'X', 'Q', 'J', 'Z'};

string generateRandomText(int textLength) {
    random_device rd;
    mt19937 generator(rd());

    discrete_distribution<int> letterDistribution({21912, 16587, 14810, 14003, 13318, 12666, 11450,10977,10795,7874,7253,5246,4943,4761,4200,3853,3819,3693,3316,2715,2019,1257,315,205,188,128});
    binomial_distribution<int> binomialDistribution(12, 0.5);

    string randomText;
    randomText.reserve(textLength);
    for (int i = 0; i < textLength; ++i) {

        int wordLength = binomialDistribution(generator);

        for (int j = 0; j < wordLength; ++j) {
            int letterIndex = letterDistribution(generator);
            char litera = litery[letterIndex];
            randomText += litera;
        }
        randomText += ' ';
    }
    return randomText;
}

int main(int argc, char *argv[]) {
    if (argc != 3) {
        cerr << "Użycie: " << argv[0] << " <długość tekstu> <nazwa pliku>" << endl;
        return 1;
    }

    int textLength = stoi(argv[1]);
    string fileName = argv[2];

    string randomText = generateRandomText(textLength);

    ofstream outputFile(fileName);
    if (outputFile.is_open()) {
        outputFile << randomText;
        outputFile.close();
        cout << "Wygenerowany tekst został zapisany do pliku: " << fileName << endl;
    } else {
        cerr << "Błąd podczas zapisu do pliku." << endl;
        return 1;
    }

    return 0;
}
