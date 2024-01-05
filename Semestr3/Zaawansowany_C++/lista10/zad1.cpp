#include <iostream>
//testuj na parrocie, ten system sie do tego nie nadaje
#include <locale>
int main() {
    setlocale(LC_ALL,"Polish");
    // setlocale(LC_ALL, "pl_PL.ISO-8859-2");
    std::wstring polskieZnaki = L"Żółta kóza pędziła wóz z dębem, ćwicząc język na różnych mężnych spódnicy.";
    std::wcout << polskieZnaki << std::endl;

    return 0;
}
