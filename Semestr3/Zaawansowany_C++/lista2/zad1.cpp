#include <iostream>
#include <set>
#include <memory>

using namespace std;

class licznik {
public:
    licznik() : wartosc(1) {}

    virtual ~licznik() {
        cerr << wartosc << endl;
    }

    void increment() {
        wartosc++;
    }

    uint64_t getwartosc() const {
        return wartosc;
    }

private:
    uint64_t wartosc;
};

void recursiveIncrement(std::unique_ptr<licznik[]> liczniki, int m, int n) {
    if (m == 0) {
        return;
    }
    set<int> miejsca;
    while(miejsca.size() < 0.1 * n){
        while(int random_numb = rand()%n){
            if(miejsca.count(random_numb) == 0){
                miejsca.insert(random_numb);
            }
        }
    }
    for(int i : miejsca){
        liczniki[i].increment();
    }

    recursiveIncrement(move(liczniki), m - 1, n);
}

int main(){
    int n = 40;
    int m = 20;
    unique_ptr<licznik[]> liczniki(new licznik[n]);
    recursiveIncrement(std::move(liczniki), m, n);
    



}