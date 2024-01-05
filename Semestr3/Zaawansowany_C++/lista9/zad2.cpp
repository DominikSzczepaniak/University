#include <iostream>
#include <fstream>
#include <iterator>
#include <vector>
#include <algorithm>
using namespace std;
int eulerTotientFunction(int n) {
    unsigned int result = 1; 
    for (int i = 2; i < n; i++) 
        if (__gcd(i, n) == 1) 
            result++;
    return result; 
}

int main(int argc, char* argv[]) {
    if (argc != 2) {
        cerr << "Użycie: " << argv[0] << " <k>" << endl;
        return 1;
    }

    int k = stoi(argv[1]);

    if (k < 1) {
        cerr << "Podaj dodatnią wartość k." << endl;
        return 1;
    }

    ofstream outputFile("phi.txt");
    if (!outputFile.is_open()) {
        cerr << "Nie można otworzyć pliku phi.txt do zapisu." << endl;
        return 1;
    }

    vector<int> phiValues;

    for (int n = 1; n <= k; ++n) {
        int phiN = eulerTotientFunction(n);
        phiValues.push_back(phiN);
    }

    copy(phiValues.begin(), phiValues.end(), ostream_iterator<int>(outputFile, "; "));
    outputFile.close();

    cout << "Wartości tocjenta zostały zapisane do pliku phi.txt." << endl;

    return 0;
}
