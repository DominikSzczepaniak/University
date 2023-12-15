#include <iostream>
#include <unordered_set>
using namespace std;
using USS = unordered_set<string>;
int main(){
    USS s;
    s.insert("asd");
    s.insert("bzxcv");
    s.insert("qwtreqw");
    for(auto it = s.begin(); it != s.end(); it++){
        cout << *it << endl;
    }
    return 0;
}
