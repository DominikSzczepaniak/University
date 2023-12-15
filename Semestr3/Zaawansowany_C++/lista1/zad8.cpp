#include <iostream>
#include <deque>
#include <string>
#include <algorithm>
#include <tuple>

using namespace std;

struct Osoba {
    string nazwisko;
    string imie;
    int rok_urodzenia;
    Osoba(const string& nazwisko, const string& imie, int rok_urodzenia)
        : nazwisko(nazwisko), imie(imie), rok_urodzenia(rok_urodzenia) {}
    friend bool operator<(const Osoba& a, const Osoba& b) {
        return tie(a.nazwisko, a.imie, a.rok_urodzenia) < tie(b.nazwisko, b.imie, b.rok_urodzenia);
    }
};

int main() {
    deque<Osoba> osoby;
    osoby.push_back(Osoba("jeden", "pierwszy", 1111));
    osoby.push_back(Osoba("jeden", "pierwszy", 1110));
    osoby.push_back(Osoba("dwa", "drugi", 2222));
    osoby.push_back(Osoba("trzy", "trzeci", 3333));
    osoby.push_back(Osoba("cztery", "czwarty", 4444));
    sort(osoby.begin(), osoby.end());
    for (const Osoba& os : osoby) {
        cout << os.nazwisko << ", " << os.imie << ", " << os.rok_urodzenia << endl;
    }

    return 0;
}
