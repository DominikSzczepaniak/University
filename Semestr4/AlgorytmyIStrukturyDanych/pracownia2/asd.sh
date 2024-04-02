green=$(tput setaf 71);
red=$(tput setaf 1);
blue=$(tput setaf 32);
orange=$(tput setaf 178);
bold=$(tput bold);
reset=$(tput sgr0);



for((i = 0; i<=2000; ++i)); do
    ./wzorcowka < tests/in$i.txt > out/out$i.txt
done

