#!/bin/bash

input_file="zad2_input.txt"
output_file="zad2_input2.txt"
script_file="zad2.py"

# Funkcja wykonująca operację dla każdej linii
function execute_operations() {
    rm -rf zad2_output.txt
    touch zad2_output.txt
    while IFS= read -r line; do
        echo "$line" > "$output_file"
        python3 "$script_file"
    done < "$input_file"
}

# Wywołanie funkcji
execute_operations