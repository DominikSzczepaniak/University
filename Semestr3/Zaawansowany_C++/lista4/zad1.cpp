#include <iostream>
#include <functional>
using namespace std;

template<typename F, typename G, typename H>
class compose{
    public:
    compose(F f, G g, H h): f(f), g(g), h(h){}
    template<typename T>
    auto operator()(T x){
        return f(g(x), h(x));
    }
    private:
    F f;
    G g;
    H h;
};

int add(int a, int b){
    return a + b;
}

int half(int a){
    return a/2;
}

int square(int a){
    return a * a;
}

int main(){
    auto composed = compose(add, half, square);
    auto composed2 = compose(add, compose(add, half, square), square);
    cout << composed2(3) << endl;
    // cout << composed(2) << endl;
}