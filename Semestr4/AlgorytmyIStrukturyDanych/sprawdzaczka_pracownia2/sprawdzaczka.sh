for((i = 0; i<=1000; ++i)); do
    ./wzorcowka < in/n1000/in$i.txt > sprawdz 
    python3 poprawnyWynik.py out/n1000/out$i.txt sprawdz n1000
    rm sprawdz
done
echo "koniec testow n1000"

for((i = 0; i<=500; ++i)); do
    ./wzorcowka < in/n100000/in$i.txt > sprawdz 
    python3 poprawnyWynik.py out/n100000/out$i.txt sprawdz n100000
    rm sprawdz
done
echo "koniec testow n100000"

for((i = 0; i<=10; ++i)); do
    ./wzorcowka < in/nMAX/in$i.txt > sprawdz 
    python3 poprawnyWynik.py out/nMAX/out$i.txt sprawdz nMAX
    rm sprawdz
done
echo "koniec testow nMAX"