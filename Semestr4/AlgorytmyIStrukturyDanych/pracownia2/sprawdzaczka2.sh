#!/bin/bash

# Ustawienie licznika testów
numerTestu=1

# Przejście przez wszystkie pliki w folderze 'tests'
for((i = 0; i<=2000; ++i)); do
    # Wykonanie programu 'wzorc' z przekierowaniem wejścia i wyjścia
    ./wzorc < "tests/in$i.txt" > "out$i"

    # Wykonanie skryptu Pythona z numerem testu jako argumentem
    python3 sprawdz.py $i
    wait $!

    rm "out$i"
done
