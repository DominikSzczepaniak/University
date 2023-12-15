#include <iostream>
#include <deque>
#include <algorithm>
#include <random>
using namespace std;
class Person {
public:
    string firstName;
    string lastName;
    int age;
    double weight;
    double height;

    Person(string fName, string lName, int personAge, double personWeight, double personHeight)
        : firstName(fName), lastName(lName), age(personAge), weight(personWeight), height(personHeight) {}
};

double bmi(const Person& person) {
    return person.weight / (double(person.height/100) * double(person.height/100));
}

int main() {
    deque<Person> people = {
        {"John", "Doe", 30, 85.5, 180.0},
        {"Alice", "Smith", 25, 65.2, 165.5},
        {"Bob", "Johnson", 35, 92.0, 175.0},
        {"Emma", "Williams", 28, 70.8, 160.0},
        {"Michael", "Brown", 40, 110.5, 185.5},
        {"Olivia", "Jones", 22, 60.0, 170.0},
        {"Daniel", "Miller", 32, 88.7, 177.5},
        {"Sophia", "Davis", 29, 67.3, 168.0},
        {"James", "Taylor", 37, 95.2, 182.5},
        {"Ella", "Moore", 26, 62.5, 155.0},
        {"Matthew", "Wilson", 31, 84.0, 178.0},
        {"Ava", "Martinez", 24, 55.9, 162.5}
    };

    // 1. Sortowanie osób według współczynnika BMI
    sort(people.begin(), people.end(), [](const Person& a, const Person& b) {
        double bmiA = bmi(a);
        double bmiB = bmi(b);
        return bmiA < bmiB;
    });

    cout << "Posortowane osoby według BMI:" << endl;
    for (const auto& person : people) {
        cout << person.firstName << " " << person.lastName << ": " << bmi(person) << endl;
    }

    // 2. Odchudzanie osób
    for_each(people.begin(), people.end(), [](Person& person) {
        person.weight *= 0.9; // Strata 10% wagi
    });

    cout << "\nOsoby po odchudzeniu:" << endl;
    for (const auto& person : people) {
        cout << person.firstName << " " << person.lastName << ": " << person.weight << endl;
    }

    // 3. Podział na grupy: ciężkie i lekkie
    auto heavy = partition(people.begin(), people.end(), [](const Person& person) {
        return person.weight > 100.0;
    });

    cout << "\nOsoby ciężkie:" << endl;
    for (auto it = people.begin(); it != heavy; ++it) {
        cout << it->firstName << " " << it->lastName << ": " << it->weight << endl;
    }

    cout << "\nOsoby lekkie:" << endl;
    for (auto it = heavy; it != people.end(); ++it) {
        cout << it->firstName << " " << it->lastName << ": " << it->weight << endl;
    }

    // 4. Ustawienie osoby o środkowym wzroście na pozycji 5
    auto mid = people.begin() + people.size() / 2;
    nth_element(people.begin(), mid, people.end(), [](const Person& a, const Person& b) {
        return a.height < b.height;
    });

    cout << "\nOsoby po modyfikacji pozycji środkowej:" << endl;
    for (const auto& person : people) {
        cout << person.firstName << " " << person.lastName << ": " << person.height << endl;
    }
    // 5. Losowa modyfikacja pozycji 5 osób
    random_device rd;
    mt19937 gen(rd());
    shuffle(people.begin(), people.begin() + 5, gen);
    shuffle(people.end() - 5, people.end(), gen);

    cout << "\nOsoby po losowej modyfikacji:" << endl;
    for (const auto& person : people) {
        cout << person.firstName << " " << person.lastName << ": " << person.age << endl;
    }

    // 6. Wypisanie najstarszej i najmłodszej osoby
    auto minMax = minmax_element(people.begin(), people.end(), [](const Person& a, const Person& b) {
        return a.age < b.age;
    });

    cout << "\nNajmłodsza osoba: " << minMax.first->firstName << " " << minMax.first->lastName << endl;
    cout << "Najstarsza osoba: " << minMax.second->firstName << " " << minMax.second->lastName << endl;

    return 0;
}
