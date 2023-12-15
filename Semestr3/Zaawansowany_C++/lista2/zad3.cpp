#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <memory>

enum class Gender { Male, Female };

class llama {
public:
    llama(const std::string& name, Gender gender, std::shared_ptr<llama> father = nullptr, std::shared_ptr<llama> mother = nullptr)
        : name(name), gender(gender), father(father), mother(mother) {
            //nie mozna uzyc shared_ptr -> addChild jesli konstruktor sie jeszcze nie skonczyl, bo shared_ptr tworzy sie dopiero po zakonczeniu konstruktora, wiec nie dam rady wywolac w konstruktorze addChild dla father i mother, gdyz nie moge stworzyc weak_ptr na this 
            //czyli w szczegolnosci father->addChild(this) i father->addChild(shared_from_this()) nie zadziala, poniewaz shared_ptr jeszcze nie istnieje

            // nie wiem w jaki inny sposob dodac child do vectora children dla father i mother
        }

    ~llama() {
        std::cout << "Lama " << name << " umiera." << std::endl;
    }

    std::string getName() const {
        return name;
    }

    Gender getGender() const {
        return gender;
    }

    std::shared_ptr<llama> getFather() const {
        return father;
    }

    std::shared_ptr<llama> getMother() const {
        return mother;
    }

    void addChild(std::shared_ptr<llama> child) {
        children.push_back(child);
    }

    void printChildren() const {
        std::cout << "Dzieci lamy " << name << ": ";
        for (const auto& child : children) {
            if (auto shared = child.lock()) {
                std::cout << shared->getName() << " ";
            }
        }
        std::cout << std::endl;
    }

    bool operator<(const llama& rhs) {
        return this->getName() < rhs.getName();
    }

private:
    std::string name;
    Gender gender;
    std::shared_ptr<llama> father;
    std::shared_ptr<llama> mother;
    std::vector<std::weak_ptr<llama>> children;
};

void lamaSell(std::set<std::shared_ptr<llama>>& herd, std::shared_ptr<llama>& lama){
    herd.erase(lama);
}

void lamaDies(std::set<std::shared_ptr<llama>>& herd, std::shared_ptr<llama>& lama){
    herd.erase(lama);
    lama.reset();
}

int main() {
    std::set<std::shared_ptr<llama>> herd;

    std::shared_ptr<llama> lama1 = std::make_shared<llama>("Lama1", Gender::Female);
    herd.insert(lama1);
    std::shared_ptr<llama> lama2 = std::make_shared<llama>("Lama2", Gender::Male);
    herd.insert(lama2);
    std::shared_ptr<llama> lama3 = std::make_shared<llama>("Lama3", Gender::Female, lama1, lama2);
    herd.insert(lama3);
    std::shared_ptr<llama> lama4 = std::make_shared<llama>("Lama3", Gender::Female, lama1, lama2);
    lama1->addChild(lama3);
    lama2->addChild(lama3);

    lamaSell(herd, lama3);
    lama1->printChildren(); //lama3 jest dzieckiem lama1 bo zyje, ale nie ma juz jej w stadzie
    lamaDies(herd, lama3);
    lama1->printChildren(); //lama3 juz nie jest dzieckiem lama1, bo nie istnieje (ded)

    //jesli std::shared_ptr jest zwolniony (osiąga licznik odniesien rowny zero) to wskaźnik std::weak_ptr staje sie wskaźnikiem wiszacym (czyli .expired() zwraca true). to znaczy ze nie mozna juz uzyskac dostepu do zasobu na ktory wczesniej wskazywal ten std::weak_ptr.

    return 0;
}
