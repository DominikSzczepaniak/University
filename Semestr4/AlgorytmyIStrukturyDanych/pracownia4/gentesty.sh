green=$(tput setaf 71);
red=$(tput setaf 1);
blue=$(tput setaf 32);
orange=$(tput setaf 178);
bold=$(tput bold);
reset=$(tput sgr0);

for((i = 0; i<=50; ++i)); do
    ./gen $i > in2/in$i.txt
    ./a.out < in/in$i.txt > out2/out$i.txt
done
