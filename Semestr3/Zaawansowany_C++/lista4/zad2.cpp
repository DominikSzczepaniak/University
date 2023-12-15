#include <iostream>
#include <functional>
using namespace std;

template<typename F1, typename F2>
class po_kolei{
    public:
    po_kolei(F1 f1, F2 f2): f1(f1), f2(f2){}

    template<typename T>
    auto operator ()(T &x){
        f1(x);
        f2(x);
        return po_kolei(f1, f2);
    }
    private:
    F1 f1;
    F2 f2;
};

void increase(int x){
    cout << x + 1 << endl;
}

void square(int x){
    cout <<  x*x << endl;
}  

void multiply_by_2(int x){
    cout << 2 * x << endl;
}

void zwieksz(int &x){
    x++;
}

void podwoj(int &x){
    x *= 2;
}

void poteguj(int &x){
    x *= x;
}

int main(){
    // auto f = po_kolei(increase, square);
    // auto g = po_kolei(f, multiply_by_2);
    // int x = 2;
    // g(x);
    // auto h = po_kolei(zwieksz, podwoj);
    // auto i = po_kolei(h, poteguj);
    // int y = 2;
    // i(y);
    auto ff = po_kolei(po_kolei(increase, square), podwoj);
    int z = 2;
    ff(z);
    cout << z << endl;
    // cout << y << endl;
}