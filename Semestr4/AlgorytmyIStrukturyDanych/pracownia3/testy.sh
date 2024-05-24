green=$(tput setaf 71);
red=$(tput setaf 1);
blue=$(tput setaf 32);
orange=$(tput setaf 178);
bold=$(tput bold);
reset=$(tput sgr0);

# for((i = 0; i<=150; ++i)); do
#     # ./gen $i > in/n50w1000/in$i.txt
#     ./a.out < in/nMAXwMAX/in$i.txt > out/nMAXwMAX/out$i.txt
# done

for((i = 0; i<=500; ++i)); do
    # ./gen $i > in/n50w1000/in$i.txt
    ./a.out < in/n50w1000/in$i.txt > out/n50w1000/out$i.txt
done
