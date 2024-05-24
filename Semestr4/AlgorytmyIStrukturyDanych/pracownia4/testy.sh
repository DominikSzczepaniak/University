green=$(tput setaf 71);
red=$(tput setaf 1);
blue=$(tput setaf 32);
orange=$(tput setaf 178);
bold=$(tput bold);
reset=$(tput sgr0);

for((i = 0; i<=5000; ++i)); do
    ./gen $i > testowanie
    ./brut < testowanie > check1
    ./a.out < testowanie > check2
    if diff -w check1 check2 &>/dev/null; then
        echo "${green}${bold}Test $i passed!${reset}"
    else
        echo "${red}${bold}Test $i failed!${reset}"
        break
    fi
done
