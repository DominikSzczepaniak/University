#include <iostream>
#include <ratio>
using namespace std;
template <int N>
struct Harmonic {
    using value = ratio_add<typename Harmonic<N-1>::value, ratio<1, N>>;
};

template <>
struct Harmonic<1> {
    using value = ratio<1, 1>;
};

int main() {
    using wartosc = Harmonic<3>::value;
    cout << wartosc::num << "/" << wartosc::den << endl; //dla wiekszych wartosci sa problemy 
    //dodac flage -ftemplate-depth
    return 0;
}
