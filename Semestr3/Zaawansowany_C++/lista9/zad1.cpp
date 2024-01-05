#include <iostream>
#include <iterator>
#include <sstream>
#include <vector>
#include <numeric>
#include <string>
#include <cmath>
#include <iomanip>
using namespace std;

int main(){
    string s;
    getline(cin, s);
    istringstream iss(s);
    vector<double> numbers;
    copy(istream_iterator<double>(iss), istream_iterator<double>(), back_inserter(numbers));
    double mean = accumulate(numbers.begin(), numbers.end(), 0.0) / numbers.size();
    double sumSquaredDifferences = 0.0;
    for (const auto& value : numbers) {
        double difference = value - mean;
        sumSquaredDifferences += difference * difference;
    }
    double variance = sumSquaredDifferences / (numbers.size() - 1);
    double standardDeviation = sqrt(variance);
    cout << "Średnia arytmetyczna: " << fixed << setprecision(3) << mean << endl;
    cout << "Odchylenie standardowe: " << fixed << setprecision(3) << standardDeviation << endl;




}
