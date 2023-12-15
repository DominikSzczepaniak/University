#include <iostream>
#include <algorithm>
#include <iterator>
#include <map>
#include <vector>
using namespace std;

vector<pair<int, int>> najczesciej_wystepujace(vector<int> a){
    map<int, int> wyst;
    for(auto i : a){
        wyst[i]++;
    }
    int maxCount = max_element(wyst.begin(), wyst.end(),
        [](const auto& p1, const auto& p2) {
            return p1.second < p2.second;
        })->second;
    vector<pair<int, int>> wyjscie;
    for_each(wyst.begin(), wyst.end(), [&](const auto& p){
        if(p.second == maxCount){
            wyjscie.push_back(p);
        }
    });
    return wyjscie;
}

int main(){
    vector<int> a = {1,1,3,5,8,9,5,8,8,5};
    vector<pair<int, int>> b = najczesciej_wystepujace(a);
    for(auto i : b){
        cout << i.first << " " << i.second << endl;
    }
}