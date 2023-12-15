#include <iostream>
#include <type_traits>
#include <string>
using namespace std;
template <typename Source, typename Dest>
typename enable_if<is_convertible<Source, Dest>::value>::type
TransferValue(const Source& source, Dest& dest) {
    dest = source;
}

template <typename Source, typename Dest>
typename enable_if<is_pointer<Source>::value && is_convertible<typename remove_pointer<Source>::type, Dest>::value>::type
TransferValue(Source source, Dest& dest) {
    if (source) {
        dest = *source;
    }
}

int main() {
    int source = 42;
    double dest1;
    int* sourcePtr = &source;
    double dest2;
    string test;

    TransferValue(source, dest1); 
    TransferValue(sourcePtr, dest2); 

    cout << "dest1: " << dest1 << endl; 
    cout << "dest2: " << dest2 << endl; 
    return 0;
}
