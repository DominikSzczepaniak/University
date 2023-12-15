#include <cmath>
#include <iostream>
#include <vector>
using namespace std;

//szereg naprzemienny jest zbiezny jesli a1 >= a2 >= a3 ... >= ak i lim ak = 0 przy k -> inf
//mamy szereg postaci ∑k=1 ^ inf   [(-1)^k * 1/(2k+1)]
// z tego mamy, ze ak = 1/(2k+1)
// lim ak = lim 1/(2k+1) = 0 przy k -> inf
// oraz a1 >= a2 >= a3 ... >= ak 
// nasz szereg jest wiec zbiezny

// wiemy wtedy wiec, ze 
// |S - Sn| <= a n+1
// gdzie Sn = ∑ k = 1 ^ n   [(-1)^k * ak)]

// tak wiec, musimy znalezc takie a n+1, zeby
// |S - Sn| < 10^6

// takze mamy 4 ∑ k=0 ^ inf [(-1)^k * 1/(2k+1)] = ∑ k=0 ^ inf [(-1)^k * 4/(2k+1)] = ∑ k=0 ^ inf [(-1)^k * ak], gdzie ak = 4/(2k+1)

// 4/2k+1 <= 10^-6
// 4/10^-6 <= 2k+1
// 4000000 <= 2k+1
// 3999999 <= 2k
// 1999999.5 <= k 
// czyli k = 2000000
// stad wiemy, ze obliczenie pi bedzie wymagac okolo 2000000 wyrazow


int main(){
    vector<double> szereg;
    long k = 0;
    double pi_wartosc = 0;
    while(1){
        double gora = (k%2==0?1.0 : -1.0);
        double dol = 2*k+1;
        double wart = gora / dol;
        pi_wartosc += wart;
        szereg.push_back(wart);
        k++;
        if(abs(4*pi_wartosc - M_PI) < 1e-6) break;
    }
    cout << szereg.size() << endl;
    //wedlug obliczen mial byc 2000000, a wychodzi 1000001
    //takze wyszla polowa wyrazow ktora oczekiwalismy
}


