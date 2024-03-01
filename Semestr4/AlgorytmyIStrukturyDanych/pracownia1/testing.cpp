#include <iostream>
#include <vector>
#include <random>
#include <map>
#include <set>
using namespace std;
#define ll long long
#define pb push_back
const ll MAX = 1e5;

int randd(int a, int b){
    return a + rand() % (b-a+1);
}

void graph(int maxW, int maxK, int maxV){
    int n, m;
    n = randd(2, maxW);
    m = randd(1, maxK);
    cout << n << " " << m << endl;
    map<int, set<int> > obecne;
    for(int i = 0; i<m; i++){
        int a = randd(1, n), c = randd(1, maxV), b;
        do{
            b = randd(1, n);
        }while(a==b && obecne[a].count(b) > 0);
        cout << a << " " << b << " " << c << endl;
    }
}

void tablicaN(int granicaN, int granicaL){
    int n = randd(1, granicaN);
    cout << n << endl;
    for(int i = 0; i<n; i++){
        cout << randd(1, granicaL) << " ";
    }
    cout << endl;
}

int main(int argc, char* argv[]){
    srand(atoi(argv[1]));
    int n = randd(5, 10);
    int m = randd(5, 10);
    if(atoi(argv[1]) >= 1000 && atoi(argv[1]) <= 1500){
        n = randd(100, 500);
        m = randd(100, 500);
    }
    else if(atoi(argv[1]) > 1500 && atoi(argv[1]) <= 1800){
        n = randd(10000, 50000);
        m = randd(10000, 50000);
    }
    else if(atoi(argv[1]) > 1800 && atoi(argv[1]) <= 1900){
        n = randd(50000, 100000);
        m = 1e5;
    }
    else if(atoi(argv[1]) >1900){
        n = 1e6;
        m = 1e5;
    }
    cout << n << " " << m << endl;
    for(int i = 2; i<=n; i++){
        cout << randd(1, i-1) << endl;
        // cout << i-1 << endl;
    }
    for(int i = 0; i<m; i++){
        int a, b;
        do{
            a = randd(1, n);
            b = randd(1, n);
        }while(a==b);
        cout << a << " " << b << endl;
    }
    return 0;
}