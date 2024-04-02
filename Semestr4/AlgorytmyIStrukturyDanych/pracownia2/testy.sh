green=$(tput setaf 71);
red=$(tput setaf 1);
blue=$(tput setaf 32);
orange=$(tput setaf 178);
bold=$(tput bold);
reset=$(tput sgr0);

/opt/homebrew/bin/g++-13 testing.cpp -o gen -std=c++14
# rustc wzorc.rs -C opt-level=2 -C target-feature=+crt-static

for((i = 0; i<=1000; ++i)); do
    # ./gen $i > in1/n1000/in$i.txt  
    ./wzorc < in1/n100000/in$i.txt > out1/n100000/out$i.txt
    # if diff -q out out2; then
    #     echo "${green}Test $i passed${reset}"
    # else
    #     echo "${red}Test $i failed${reset}"
    #     break
    # fi
done

