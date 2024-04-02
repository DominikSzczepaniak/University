#!/bin/bash
for file in tests/*; do
    filename=$(basename -- "$file")
    filename_without_extension="${filename%.*}"

    ./wzorc < "$file" > "$filename_without_extension"_outtest #zmien na nazwe swojego pliku wykonywalnego

    output_file="out${filename_without_extension:2}.txt"

    diff -b -B "out/$output_file" "$filename_without_extension"_outtest
    

    if [ $? -eq 1 ]; then
        echo "Plik $filename_without_extension: inny wynik"
    fi

    rm "$filename_without_extension"_outtest
done
