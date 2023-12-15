#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <memory>

enum class Gender { Male, Female };

class llama {
public:
    llama(const std::string& name, Gender gender, const std::shared_ptr<llama>& father = nullptr, const std::shared_ptr<llama>& mother = nullptr)
        : name(name), gender(gender), father(father), mother(mother) {
        std::cout << "Nowa lama o imieniu " << name << " się urodziła." << std::endl;
    }

    ~llama() {
        std::cout << "Lama o imieniu " << name << " została sprzedana lub zmarła." << std::endl;
    }

    const std::string& getName() const {
        return name;
    }

    Gender getGender() const {
        return gender;
    }

    void addChild(const std::weak_ptr<llama>& child) {
        children.push_back(child);
    }

    void setParents(const std::shared_ptr<llama>& newFather, const std::shared_ptr<llama>& newMother) {
        father = newFather;
        mother = newMother;
    }

private:
    std::string name;
    Gender gender;
    std::shared_ptr<llama> father;
    std::shared_ptr<llama> mother;
    std::vector<std::weak_ptr<llama>> children;
};

int main() {
    std::set<llama> herd; // Stado lam (unikatowe imiona)

    std::shared_ptr<llama> father = std::make_shared<llama>("Fred", Gender::Male);
    std::shared_ptr<llama> mother = std::make_shared<llama>("Lucy", Gender::Female);

    // Urodzenie nowej lamy
    std::shared_ptr<llama> babyLlama = std::make_shared<llama>("Lily", Gender::Female, father, mother);
    father->addChild(babyLlama);
    mother->addChild(babyLlama);
    herd.insert(*babyLlama);

    // Nowa lama przychodzi do stada
    std::shared_ptr<llama> newLlama = std::make_shared<llama>("Buddy", Gender::Male);
    herd.insert(*newLlama);

    // Symulacja sprzedaży lamy (usunięcie z kolekcji)
    std::string soldLlamaName = "Lily";
    auto it = std::find_if(herd.begin(), herd.end(), [&soldLlamaName](const llama& l) {
        return l.getName() == soldLlamaName;
    });
    if (it != herd.end()) {
        herd.erase(it);
    }

    // Próba dostępu do lamy, która została sprzedana
    auto weakPtrToSoldLlama = babyLlama;
    auto sharedPtrToSoldLlama = weakPtrToSoldLlama.lock();
    if (sharedPtrToSoldLlama) {
        std::cout << "Lama " << sharedPtrToSoldLlama->getName() << " jest nadal dostępna." << std::endl;
    } else {
        std::cout << "Lama " << soldLlamaName << " została sprzedana lub zmarła." << std::endl;
    }

    return 0;
}
