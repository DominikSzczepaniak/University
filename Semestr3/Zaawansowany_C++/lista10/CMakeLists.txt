cmake_minimum_required(VERSION 3.10)
project(MojProjekt)

# Ustaw standard języka C++
set(CMAKE_CXX_STANDARD 14)

# Znajdź i dołącz Boost
find_package(Boost REQUIRED)
include_directories(${Boost_INCLUDE_DIRS})

# Dodaj pliki źródłowe do twojego projektu
set(SOURCES zad3.cpp)

# Dodaj plik wykonywalny
add_executable(MojProjekt ${SOURCES})

# Linkuj z biblioteką Boost
target_link_libraries(MojProjekt ${Boost_LIBRARIES})
