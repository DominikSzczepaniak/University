#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <sstream>
#include "googletest/googletest/include/gtest/gtest.h"

//nie poradziłoby sobie z grafami, bo działa tylko dla prostych struktur danych.
//musiałbym dodać cokolwiek aby zapamiętać czy odwiedziłem już dany Node w grafie przy serializacji i deserializacji np. trzymać te dane w mapie

class Serializable {
public:
    virtual void serialize(std::ostream& os) const = 0;
    virtual void deserialize(std::istream& is) = 0;
};

template <typename T>
void serialize(std::ostream& os, const T& value) {
    os.write(reinterpret_cast<const char*>(&value), sizeof(T));
}

template <typename T>
void deserialize(std::istream& is, T& value) {
    is.read(reinterpret_cast<char*>(&value), sizeof(T));
}

void serialize(std::ostream& os, const std::string& value) {
    serialize(os, value.size());
    os.write(value.c_str(), value.size());
}

void deserialize(std::istream& is, std::string& value) {
    std::size_t size;
    deserialize(is, size);
    value.resize(size);
    is.read(&value[0], size);
}
//vectors
template <typename T>
void serialize(std::ostream& os, const std::vector<T>& array) {
    serialize(os, array.size());
    for (const T& value : array) {
        serialize(os, value);
    }
}

template <typename T>
void deserialize(std::istream& is, std::vector<T>& array) {
    std::size_t size;
    deserialize(is, size);
    array.resize(size);
    for (T& value : array) {
        deserialize(is, value);
    }
}
//arrays
template <typename T, std::size_t N>
void serialize(std::ostream& os, const T (&value)[N]) {
    serialize(os, N); 
    for (std::size_t i = 0; i < N; ++i) {
        serialize(os, value[i]); 
    }
}

template <typename T>
std::pair<T*, std::size_t> deserialize(std::istream& is) {
    std::size_t size;
    deserialize(is, size); 

    T* array = new T[size]; 
    for (std::size_t i = 0; i < size; ++i) {
        deserialize(is, array[i]); 
    }

    return {array, size}; 
}

class Color : public Serializable {
public:
    int r, g, b;

    void serialize(std::ostream& os) const override {
        ::serialize(os, r);
        ::serialize(os, g);
        ::serialize(os, b);
    }

    void deserialize(std::istream& is) override {
        ::deserialize(is, r);
        ::deserialize(is, g);
        ::deserialize(is, b);
    }
};

class Person : public Serializable {
public:
    std::string name, surname;
    int weight;
    double height;
    Color eyeColor;

    void serialize(std::ostream& os) const override {
        ::serialize(os, name);
        ::serialize(os, surname);
        ::serialize(os, weight);
        ::serialize(os, height);
        eyeColor.serialize(os);
    }

    void deserialize(std::istream& is) override {
        ::deserialize(is, name);
        ::deserialize(is, surname);
        ::deserialize(is, weight);
        ::deserialize(is, height);
        eyeColor.deserialize(is);
    }
};

template <>
void serialize<Serializable>(std::ostream& os, const Serializable& value) {
    value.serialize(os);
}

template <>
void deserialize<Serializable>(std::istream& is, Serializable& value) {
    value.deserialize(is);
}


TEST(SerializationTest, PrimitiveType) {
    int original = 123;
    std::stringstream ss;
    serialize(ss, original);

    int deserialized;
    deserialize(ss, deserialized);

    EXPECT_EQ(original, deserialized);
}

TEST(SerializationTest, StringType) {
    std::string original = "Hello, world!";
    std::stringstream ss;
    serialize(ss, original);

    std::string deserialized;
    deserialize(ss, deserialized);

    EXPECT_EQ(original, deserialized);
}

TEST(SerializationTest, CharType) {
    char original = 'b';
    std::stringstream ss;
    serialize(ss, original);

    char deserialized;
    deserialize(ss, deserialized);

    EXPECT_EQ(original, deserialized);
}

TEST(SerializationTest, ShortType) {
    short original = 123;
    std::stringstream ss;
    serialize(ss, original);

    short deserialized;
    deserialize(ss, deserialized);

    EXPECT_EQ(original, deserialized);
}

TEST(SerializationTest, LongType) {
    long original = 123;
    std::stringstream ss;
    serialize(ss, original);

    long deserialized;
    deserialize(ss, deserialized);

    EXPECT_EQ(original, deserialized);
}

TEST(SerializationTest, FloatType) {
    float original = 123.456f;
    std::stringstream ss;
    serialize(ss, original);

    float deserialized;
    deserialize(ss, deserialized);

    EXPECT_EQ(original, deserialized);
}

TEST(SerializationTest, DoubleType) {
    double original = 123.456;
    std::stringstream ss;
    serialize(ss, original);

    double deserialized;
    deserialize(ss, deserialized);

    EXPECT_EQ(original, deserialized);
}

TEST(SerializationTest, LongDoubleType) {
    long double original = 123.456;
    std::stringstream ss;
    serialize(ss, original);

    long double deserialized;
    deserialize(ss, deserialized);

    EXPECT_EQ(original, deserialized);
}

TEST(SerializationTest, BoolType) {
    bool original = true;
    std::stringstream ss;
    serialize(ss, original);

    bool deserialized;
    deserialize(ss, deserialized);

    EXPECT_EQ(original, deserialized);
}

TEST(SerializationTest, VectorType) {
    std::vector<int> original = {1, 2, 3, 4, 5};
    std::stringstream ss;
    serialize(ss, original);

    std::vector<int> deserialized;
    deserialize(ss, deserialized);

    EXPECT_EQ(original, deserialized);
}

TEST(SerializationTest, ArrayType) {
    int original[] = {1, 2, 3, 4, 5};
    std::stringstream ss;
    serialize(ss, original);

    auto [deserialized, size] = deserialize<int>(ss);

    for (std::size_t i = 0; i < size; ++i) {
        EXPECT_EQ(original[i], deserialized[i]);
    }

    delete[] deserialized; 
}

TEST(SerializationTest, SerializableType) {
    Color original;
    original.r = 255;
    original.g = 128;
    original.b = 64;
    std::stringstream ss;
    serialize(ss, original);

    Color deserialized;
    deserialize(ss, deserialized);

    EXPECT_EQ(original.r, deserialized.r);
    EXPECT_EQ(original.g, deserialized.g);
    EXPECT_EQ(original.b, deserialized.b);
}

TEST(SerializationTest, SerializableObjectType) {
    Person original;
    original.name = "John";
    original.surname = "Doe";
    original.weight = 75;
    original.height = 1.8;
    original.eyeColor.r = 0;
    original.eyeColor.g = 0;
    original.eyeColor.b = 255;
    std::stringstream ss;
    serialize(ss, original);

    Person deserialized;
    deserialize(ss, deserialized);

    EXPECT_EQ(original.name, deserialized.name);
    EXPECT_EQ(original.surname, deserialized.surname);
    EXPECT_EQ(original.weight, deserialized.weight);
    EXPECT_EQ(original.height, deserialized.height);
    EXPECT_EQ(original.eyeColor.r, deserialized.eyeColor.r);
    EXPECT_EQ(original.eyeColor.g, deserialized.eyeColor.g);
    EXPECT_EQ(original.eyeColor.b, deserialized.eyeColor.b);
}

TEST(SerializationTest, SerializableObjectTypeVector){
    std::vector<Person> original;
    Person one;
    one.name = "John";
    one.surname = "Doe";
    one.weight = 75;
    one.height = 1.8;
    one.eyeColor.r = 0;
    one.eyeColor.g = 0;
    one.eyeColor.b = 255;
    Person two;
    two.name = "Jane";
    two.surname = "Doe";
    two.weight = 60;
    two.height = 1.6;
    two.eyeColor.r = 0;
    two.eyeColor.g = 255;
    two.eyeColor.b = 0;
    Person three;
    three.name = "Jack";
    three.surname = "Doe";
    three.weight = 90;
    three.height = 1.9;
    three.eyeColor.r = 255;
    three.eyeColor.g = 0;
    three.eyeColor.b = 0;
    original.push_back(one);
    original.push_back(two);
    original.push_back(three);
    std::stringstream ss;
    serialize(ss, original);

    std::vector<Person> deserialized;
    deserialize(ss, deserialized);

    EXPECT_EQ(original.size(), deserialized.size());
    for (std::size_t i = 0; i < original.size(); ++i) {
        EXPECT_EQ(original[i].name, deserialized[i].name);
        EXPECT_EQ(original[i].surname, deserialized[i].surname);
        EXPECT_EQ(original[i].weight, deserialized[i].weight);
        EXPECT_EQ(original[i].height, deserialized[i].height);
        EXPECT_EQ(original[i].eyeColor.r, deserialized[i].eyeColor.r);
        EXPECT_EQ(original[i].eyeColor.g, deserialized[i].eyeColor.g);
        EXPECT_EQ(original[i].eyeColor.b, deserialized[i].eyeColor.b);
    }
}

TEST(SerializationTest, SerializableObjectTypeArray){
    Person original[3];
    original[0].name = "John";
    original[0].surname = "Doe";
    original[0].weight = 75;
    original[0].height = 1.8;
    original[0].eyeColor.r = 0;
    original[0].eyeColor.g = 0;
    original[0].eyeColor.b = 255;
    original[1].name = "Jane";
    original[1].surname = "Doe";
    original[1].weight = 60;
    original[1].height = 1.6;
    original[1].eyeColor.r = 0;
    original[1].eyeColor.g = 255;
    original[1].eyeColor.b = 0;
    original[2].name = "Jack";
    original[2].surname = "Doe";
    original[2].weight = 90;
    original[2].height = 1.9;
    original[2].eyeColor.r = 255;
    original[2].eyeColor.g = 0;
    original[2].eyeColor.b = 0;
    std::stringstream ss;
    serialize(ss, original);

    auto [deserialized, size] = deserialize<Person>(ss);

    for (std::size_t i = 0; i < size; ++i) {
        EXPECT_EQ(original[i].name, deserialized[i].name);
        EXPECT_EQ(original[i].surname, deserialized[i].surname);
        EXPECT_EQ(original[i].weight, deserialized[i].weight);
        EXPECT_EQ(original[i].height, deserialized[i].height);
        EXPECT_EQ(original[i].eyeColor.r, deserialized[i].eyeColor.r);
        EXPECT_EQ(original[i].eyeColor.g, deserialized[i].eyeColor.g);
        EXPECT_EQ(original[i].eyeColor.b, deserialized[i].eyeColor.b);
    }
    delete[] deserialized;
}