#include <iostream>
#include <string>
#include <type_traits>
#include <memory>
#include <array>
#include <fstream>
#include <vector>

template<typename T>
struct on_stack {
    T value;
    T* operator->() { return &value; }
    T& operator*() { return value; }
};

template<typename T>
struct on_heap {
    T* value;
    on_heap() : value(new T) {}
    ~on_heap() { delete value; }
    T* operator->() { return value; }
    T& operator*() { return *value; }
};

template<typename T>
struct obj_holder {
    using type = typename std::conditional<(sizeof(T) <= sizeof(std::string)) && !std::is_array<T>::value, on_stack<T>, on_heap<T>>::type;
};

template<typename T>
struct array_on_heap {
    T* value;
    array_on_heap() : value(new T) {}
    ~array_on_heap() { delete[] value; }
    typename T::value_type& operator[](size_t i) { return value[i]; }
};

template<typename T>
struct array_in_file {
    std::fstream file;
    std::vector<typename T::value_type> buffer;
    array_in_file() : file("temp.bin", std::ios::in | std::ios::out | std::ios::binary | std::ios::trunc) {
        buffer.resize(sizeof(T) / sizeof(typename T::value_type));
    }
    ~array_in_file() { file.close(); }
    typename T::value_type& operator[](size_t i) {
        file.seekg(i * sizeof(typename T::value_type));
        file.read(reinterpret_cast<char*>(&buffer[i]), sizeof(typename T::value_type));
        return buffer[i];
    }
};

template<typename T>
struct arr_holder {
    using type = typename std::conditional<(sizeof(T) <= sizeof(std::string)), array_on_heap<T>, array_in_file<T>>::type;
};

int main() {
    obj_holder<int>::type holder1;
    *holder1 = 10;
    std::cout << *holder1 << std::endl;

    obj_holder<std::array<int, 100>>::type holder2;
    (*holder2)[0] = 20;
    std::cout << (*holder2)[0] << std::endl;

    arr_holder<std::array<int, 10>>::type holder3;
    holder3[0] = 10;
    std::cout << holder3[0] << std::endl;

    arr_holder<std::array<int, 10000>>::type holder4;
    holder4[100] = 20;
    std::cout << holder4[100] << std::endl;


    return 0;
}