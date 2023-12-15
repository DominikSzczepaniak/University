#include <iostream>
#include <algorithm>
#include <iterator>
#include <vector>
using namespace std;

vector<string> generatePermutations(string str){
    sort(str.begin(), str.end());
    vector<string> answer;
    do{
        answer.push_back(str);
    }while(next_permutation(str.begin(), str.end()));
    return answer;
}

int main(){
    string s;
    cin >> s;
    auto a = generatePermutations(s);
    for(auto i : a){
        cout << i << endl;
    }
}