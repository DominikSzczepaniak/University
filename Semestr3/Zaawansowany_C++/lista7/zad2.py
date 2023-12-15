import matplotlib.pyplot as plt
import numpy as np
import csv

# Wczytaj dane z plików CSV
def read_data(file_path):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        data = [float(row[0]) for row in reader]
    return data

# Dane z rozkładu jednostajnego
uniform_data = read_data('liczby_jednostajne.csv')

# Dane z rozkładu dwumianowego
binomial_data = read_data('liczby_dwumianowe.csv')

# Dane z rozkładu normalnego
normal_data = read_data('liczby_normalne.csv')

# Utwórz wykresy
plt.figure(figsize=(12, 4))

# Wykres dla rozkładu jednostajnego
plt.subplot(1, 3, 1)
plt.hist(uniform_data, bins=20, color='skyblue', edgecolor='black')
plt.title('Rozkład jednostajny')

# Wykres dla rozkładu dwumianowego
plt.subplot(1, 3, 2)
plt.hist(binomial_data, bins=20, color='lightcoral', edgecolor='black')
plt.title('Rozkład dwumianowy')

# Wykres dla rozkładu normalnego
plt.subplot(1, 3, 3)
plt.hist(normal_data, bins=20, color='lightgreen', edgecolor='black')
plt.title('Rozkład normalny')

# Wyświetl wykresy
plt.tight_layout()
plt.show()
