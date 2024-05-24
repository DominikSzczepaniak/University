#include <iostream>
#include <vector>
using namespace std;
struct Item
{
    int weight;
    int value;
};

int main(){
    int n, W;
    cin >> W;
    cin >> n;
    // cout << n << " " << W << endl;
    vector<Item> items(n);
    for (int i = 0; i < n; i++)
    {
        cin >> items[i].value >> items[i].weight;
    }
    string wynik;
    cin >> wynik;
    int minw, maxw;
    cin >> minw;
    // cout << wynik << " " << minw << endl;
    {
    long suma = 0;
    long waga = 0;
    vector<int> uzyte(n);
    for(int i = 0; i<n; i++){
        int a;
        cin >> a;
        // cout << a << " ";
        if(a > 0){
            suma += items[i].value * a;
            waga += items[i].weight * a;
        }
    }
    cout << suma << " " << waga << endl;
    }
    cin >> maxw;
    long suma = 0;
    long waga = 0;
    for(int i = 0; i<n; i++){
        int a;
        cin >> a;
        cout << a << " ";
        if(a > 0){
            suma += items[i].value * a;
            waga += items[i].weight * a;
        }
    }
    cout << endl;
    cout << suma << " " << waga << endl;

}