#!/bin/bash

for ((i=101; i<=10000; i++))
do
    echo "Test $i"
    ./gen $i > testa
    ./a.out < testa > odpa
    ./brut < testa > odpb

    if ! diff -q odpa odpb &>/dev/null; then
        echo "Test $i: Wyniki są różne"
        break
    fi
done
