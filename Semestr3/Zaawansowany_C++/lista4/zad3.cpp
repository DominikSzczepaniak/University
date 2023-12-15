#include <algorithm>
#include <iostream>
#include <list>
#include <set>
#include <vector>
#include <memory>
using namespace std;

vector<double> v1 = {1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0};
list<string> v2 = {"a", "b", "c"};
set<int> v3 = {4, 5, 6};

template <typename T> class WypiszWartosci {
public:
    WypiszWartosci(T a, T b) : a_(a), b_(b) {}
    void operator()(T x) {
        if (x >= a_ && x <= b_) {
            std::cout << x << std::endl;
        }
    }

private:
    T a_;
    T b_;
};
// 1 2 3 4 5 
//     ^
// 
template <typename T> class WypiszCoK {
public:
    WypiszCoK(int p, int k) : k_(k), p_(-p + 1) {}

    void operator()(T x) {
        if (p_ == 0) {
            p_ = k_;
        }
        if (p_ >= 0) {
            if (p_ % k_ == 0) {
                std::cout << x << std::endl;
            }
        }
        p_++;
    }

private:
    int k_;
    int p_;
};

template <typename T>
class SredniaArytmetyczna {
public:
    SredniaArytmetyczna() : suma(0), ilosc(0) {}
    SredniaArytmetyczna(SredniaArytmetyczna&& other) noexcept {
        suma = other.suma;
        ilosc = other.ilosc;
        other.ilosc = 0;  // Resetujemy ilość w przenoszonym obiekcie
    }
    void operator()(T& x) {
        suma += x;
        ilosc++;
    }
    ~SredniaArytmetyczna() {
        if (ilosc > 0) {
            std::cout << suma / ilosc << std::endl;
        }
    }

private:
    T suma;
    T ilosc;
};

template<typename T>
class MinMax {
public:
    MinMax() : minEl(nullptr), maxEl(nullptr) {}
    MinMax(MinMax&& other) noexcept {
        minEl = other.minEl;
        maxEl = other.maxEl;
        other.minEl = nullptr;  // Ustawiamy na nullptr w przenoszonym obiekcie
        other.maxEl = nullptr;  // Ustawiamy na nullptr w przenoszonym obiekcie
    }
    void operator()(T& x) {
        if (minEl == nullptr) {
            minEl = &x;
        }
        if (maxEl == nullptr) {
            maxEl = &x;
        }
        if (x < *minEl) {
            minEl = &x;
        }
        if (x > *maxEl) {
            maxEl = &x;
        }
    }
    ~MinMax() {
        if (minEl != nullptr && maxEl != nullptr) {
            std::cout << *minEl << " " << *maxEl << std::endl;
        }
    }

private:
    T* minEl;
    T* maxEl;
};

template <typename T>
class SumaWszystkich {
public:
    SumaWszystkich() {
        suma = T();
    }
    SumaWszystkich(SumaWszystkich&& other) noexcept {
        suma = T();
    }
    void operator()(T& x) {
        suma += x;
    }
    ~SumaWszystkich() {
        if(suma != T())
            cout << suma << endl;
    }

private:
    T suma;
};

int main() {
    for_each(v1.begin(), v1.end(), WypiszWartosci<double>(3, 6));
    for_each(v3.begin(), v3.end(), WypiszWartosci<int>(1, 2));

    std::cout << std::endl;
    for_each(v1.begin(), v1.end(), WypiszCoK<double>(2, 2));

    std::cout << std::endl;

    for_each(v1.begin(), v1.end(), SredniaArytmetyczna<double>());
    for_each(v1.begin(), v1.end(), MinMax<double>());
    for_each(v1.begin(), v1.end(), SumaWszystkich<double>());
    for_each(v2.begin(), v2.end(), SumaWszystkich<string>());
    return 0;
}
