green=$(tput setaf 71);
red=$(tput setaf 1);
blue=$(tput setaf 32);
orange=$(tput setaf 178);
bold=$(tput bold);
reset=$(tput sgr0);

/opt/homebrew/bin/g++-13 testing.cpp -o gen -std=c++14
rustc wzorcowka.rs -C opt-level=2 -C target-feature=+crt-static


for((i = 1; i<=1920; ++i)); do
    ./gen $i > in/in$i.txt
    ./wzorcowka < in/in$i.txt > out/out$i.txt
done

