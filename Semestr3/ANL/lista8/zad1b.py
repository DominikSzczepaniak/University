import numpy as np
from scipy.interpolate import CubicSpline
import matplotlib.pyplot as plt
x = [-7, -4, -2, 0, 1, 5, 10]
y = [-16185, -10116, -6070, -2024, -1, 8091, 18206]

cs = CubicSpline(x, y, bc_type='natural')
for i in cs.c:
    print(i)
xs = np.linspace(-7, 10, 100)
plt.plot(xs, cs(xs), label="S")
plt.plot(x, y, 'o', label='data')
plt.legend(loc='lower left', ncol=2)
plt.show()