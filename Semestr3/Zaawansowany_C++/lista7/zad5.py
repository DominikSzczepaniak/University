import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('riemann_zeta_values.csv')

plt.plot(df['real_part'], df['real_value'], label='Real Part')

plt.plot(df['real_part'], df['imaginary_value'], label='Imaginary Part')

plt.title('Funkcja dzeta Riemanna na prostej krytycznej')
plt.xlabel('Część rzeczywista')
plt.ylabel('Wartość funkcji dzeta Riemanna')
plt.legend()
plt.show()
