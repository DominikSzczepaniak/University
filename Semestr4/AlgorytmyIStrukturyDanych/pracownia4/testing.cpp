#include <iostream>
#include <map>
#include <random>
#include <set>
#include <vector>
using namespace std;
#define ll long long
#define pb push_back
const ll MAX = 1e5;

int randd(int a, int b)
{
    return a + rand() % (b - a + 1);
}

void graph(int maxW, int maxK, int maxV)
{
    int n, m;
    n = randd(2, maxW);
    m = randd(1, maxK);
    cout << n << " " << m << endl;
    map<int, set<int>> obecne;
    for (int i = 0; i < m; i++)
    {
        int a = randd(1, n), c = randd(1, maxV), b;
        do
        {
            b = randd(1, n);
        } while (a == b && obecne[a].count(b) > 0);
        cout << a << " " << b << " " << c << endl;
    }
}

void tablicaN(int granicaN, int granicaL)
{
    int n = randd(1, granicaN);
    cout << n << endl;
    for (int i = 0; i < n; i++)
    {
        cout << randd(1, granicaL) << " ";
    }
    cout << endl;
}

int main(int argc, char *argv[])
{
    srand(atoi(argv[1]));
    int k = 50;
    int l = 1000;
    cout << k << " " << l << endl;
    for (int i = 0; i < l; i++)
    {
        cout << 1000 << " ";
    }
    cout << endl;
    return 0;
}
