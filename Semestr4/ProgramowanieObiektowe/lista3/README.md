Dominik Szczepaniak
dotnet new classlib -n Zadanie2Biblioteka
dotnet new classlib -n Zadanie4Biblioteka
dotnet new console -n Zadanie2
dotnet new console -n Zadanie4
dotnet add Zadanie2 reference Zadanie2Biblioteka/Zadanie2Biblioteka.csproj
dotnet add Zadanie4 reference Zadanie4Biblioteka/Zadanie4Biblioteka.csproj
cd Zadanie2 && dotnet build
cd Zadanie4 && dotnet build


dotnet --version
8.0.21
