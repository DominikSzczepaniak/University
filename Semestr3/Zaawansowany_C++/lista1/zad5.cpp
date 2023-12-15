#include <cmath>
#include <iostream>

using namespace std;
auto lucas(uint64_t n){
    uint64_t answers[n + 1];
    answers[0] = 2;
    answers[1] = 1;
    for (uint64_t i = 2; i <= n; i++){
        answers[i] = answers[i - 1] + answers[i - 2];
    }
    return answers[n];
}

int main()
{
    cout << lucas(15) << endl;
}