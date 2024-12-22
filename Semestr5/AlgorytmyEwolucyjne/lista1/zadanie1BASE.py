# # Popularne instancje QAP wraz z dokĹadnym minimum funkcji celu
#    Nug12   12    578 (OPT)    (12,7,9,3,4,8,11,1,5,6,10,2)
#    Nug14   14   1014 (OPT)    (9,8,13,2,1,11,7,14,3,4,12,5,6,10)
#    Nug15   15   1150 (OPT)    (1,2,13,8,9,4,3,14,7,11,10,15,6,5,12)
#    Nug16a  16   1610 (OPT)    (9,14,2,15,16,3,10,12,8,11,6,5,7,1,4,13)
#    Nug16b  16   1240 (OPT)    (16,12,13,8,4,2,9,11,15,10,7,3,14,6,1,5)
#    Nug17   17   1732 (OPT)    (16,15,2,14,9,11,8,12,10,3,4,1,7,6,13,17,5)
#    Nug18   18   1930 (OPT)    (10,3,14,2,18,6,7,12,15,4,5,1,11,8,17,13,9,16)
#    Nug20   20   2570 (OPT)    (18,14,10,3,9,4,2,12,11,16,19,15,20,8,13,17,5,7,1,6)
#    Nug21   21   2438 (OPT)    (4,21,3,9,13,2,5,14,18,11,16,10,6,15,20,19,8,7,1,12,17)
#    Nug22   22   3596 (OPT)    (2,21,9,10,7,3,1,19,8,20,17,5,13,6,12,16,11,22,18,14,15)
#    Nug24   24   3488 (OPT)    (17,8,11,23,4,20,15,19,22,18,3,14,1,10,7,9,16,21,24,12,6,13,5,2)
#    Nug25   25   3744 (OPT)    (5,11,20,15,22,2,25,8,9,1,18,16,3,6,19,24,21,14,7,10,17,12,4,23,13)
# *  Nug27   27   5234 (OPT)    (23,18,3,1,27,17,5,12,7,15,4,26,8,19,20,2,24,21,14,10,9,13,22,25,6,16,11)
# *  Nug28   28   5166 (OPT)    (18,21,9,1,28,20,11,3,13,12,10,19,14,22,15,2,25,16,4,23,7,17,24,26,5,27,8,6)
# *  Nug30   30   6124 (OPT)    (5 12 6 13 2 21 26 24 10 9 29 28 17 1 8 7 19 25 23 22 11 16 30 4 15 18 27 3 14 20)
#
import threading

import numpy as np
import matplotlib.pyplot as plt
import time
import urllib.request

# %matplotlib inline

QAP_INSTANCE_URL = 'https://qaplib.mgi.polymtl.ca/data.d/nug12.dat'

qap_instance_file = urllib.request.urlopen(QAP_INSTANCE_URL)

line = qap_instance_file.readline()
n = int(line.decode()[:-1].split()[0])

print('Problem size: %d' % n)

A = np.empty((n, n))
qap_instance_file.readline()
for i in range(n):
    line = qap_instance_file.readline()
    A[i, :] = list(map(int, line.decode()[:-1].split()))
print('Flow matrix:\n', A)

B = np.empty((n, n))
qap_instance_file.readline()
for i in range(n):
    line = qap_instance_file.readline()
    B[i, :] = list(map(int, line.decode()[:-1].split()))
print('Distance matrix:\n', B)


def qap_objective_function(p):
   s = 0.0
   for i in range(n):
      s += (A[i, :] * B[p[i], p]).sum()
   return s


def random_sampling(n):
   t0 = time.time()

   T = 1000000

   permutations = np.empty((T, n), dtype=np.int64)
   costs = np.zeros(T)
   for i in range(T):
       permutations[i, :] = np.random.permutation(n)
       costs[i] = qap_objective_function(permutations[i, :])

   print(time.time() - t0)

   p = permutations[costs.argmin(), :]
   print(qap_objective_function(p), p)

   plt.figure()
   plt.hist(costs, bins=100)
   plt.show()

   print(costs.mean(), costs.std())


def random_neighbor(p, radius):
   q = p.copy()
   for r in range(radius):
      i, j = np.random.choice(n, 2, replace=False)
      q[i], q[j] = q[j], q[i]
   return q

def simulated_annealing(T, radius, alpha):
   t0 = time.time()

   p = np.random.permutation(n)
   p_cost = qap_objective_function(p)
   costs = np.zeros(T)
   for t in range(T):
       q = random_neighbor(p, radius)
       q_cost = qap_objective_function(q)
       if(q_cost < p_cost):
           p, p_cost = q, q_cost
       elif(np.random.rand() < np.exp(- alpha * (q_cost - p_cost) * t/T)):
           p, p_cost = q, q_cost
       costs[t] = p_cost

   print(time.time() - t0, costs.min())

   plt.figure()
   plt.plot(costs)
   plt.show()




