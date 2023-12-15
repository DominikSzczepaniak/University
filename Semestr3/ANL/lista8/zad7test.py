import numpy as np, matplotlib.pyplot as plt
x0 = np.asarray((5.5, 8.5, 10.5, 13, 17, 20.5, 24.5, 28, 32.5, 37.5, 40.5, 42.5, 45, 47,
49.5, 50.5, 51, 51.5, 52.5, 53, 52.8, 52, 51.5, 53, 54, 55, 56, 55.5, 54.5, 54, 55, 57, 58.5,
59, 61.5, 62.5, 63.5, 63, 61.5, 59, 55, 53.5, 52.5, 50.5, 49.5, 50, 51, 50.5, 49, 47.5, 46,
45.5, 45.5, 45.5, 46, 47.5, 47.5, 46, 43, 41, 41.5, 41.5, 41, 39.5, 37.5, 34.5, 31.5, 28, 24,
21, 18.5, 17.5, 16.5, 15, 13, 10, 8, 6, 6, 6, 5.5, 3.5, 1, 0, 0, 0.5, 1.5, 3.5, 5, 5, 4.5, 4.5, 5.5,
6.5, 6.5, 5.5))
y0 = np.asarray((41, 40.5, 40, 40.5, 41.5, 41.5, 42, 42.5, 43.5, 45, 47, 49.5, 53, 57, 59,
59.5, 61.5, 63, 64, 64.5, 63, 61.5, 60.5, 61, 62, 63, 62.5, 61.5, 60.5, 60, 59.5, 59, 58.5,
57.5, 55.5, 54, 53, 51.5, 50, 50, 50.5, 51, 50.5, 47.5, 44, 40.5, 36, 30.5, 28, 25.5, 21.5,
18, 14.5, 10.5, 7.50, 4, 2.50, 1.50, 2, 3.50, 7, 12.5, 17.5, 22.5, 25, 25, 25, 25.5, 26.5,
27.5, 27.5, 26.5, 23.5, 21, 19, 17, 14.5, 11.5, 8, 4, 1, 0, 0.5, 3, 6.50, 10, 13, 16.5, 20.5,
25.5, 29, 33, 35, 36.5, 39, 41)) 

# Solves linear system given by Tridiagonal Matrix
# Helper for calculating cubic splines
#@numba.njit(cache = True, fastmath = True, inline = 'always')
def tri_diag_solve(A, B, C, F):
    n = B.size
    assert A.ndim == B.ndim == C.ndim == F.ndim == 1 and (
        A.size == B.size == C.size == F.size == n
    ) #, (A.shape, B.shape, C.shape, F.shape)
    Bs, Fs = np.zeros_like(B), np.zeros_like(F)
    Bs[0], Fs[0] = B[0], F[0]
    for i in range(1, n):
        Bs[i] = B[i] - A[i] / Bs[i - 1] * C[i - 1]
        Fs[i] = F[i] - A[i] / Bs[i - 1] * Fs[i - 1]
    x = np.zeros_like(B)
    x[-1] = Fs[-1] / Bs[-1]
    for i in range(n - 2, -1, -1):
        x[i] = (Fs[i] - C[i] * x[i + 1]) / Bs[i]
    return x
    
# Calculate cubic spline params
#@numba.njit(cache = True, fastmath = True, inline = 'always')
def calc_spline_params(x, y):
    a = y
    h = np.diff(x)
    c = np.concatenate((np.zeros((1,), dtype = y.dtype),
        np.append(tri_diag_solve(h[:-1], (h[:-1] + h[1:]) * 2, h[1:],
        ((a[2:] - a[1:-1]) / h[1:] - (a[1:-1] - a[:-2]) / h[:-1]) * 3), 0)))
    d = np.diff(c) / (3 * h)
    b = (a[1:] - a[:-1]) / h + (2 * c[1:] + c[:-1]) / 3 * h
    return a[1:], b, c[1:], d

# Spline value calculating function, given params and "x"
#@numba.njit(cache = True, fastmath = True, inline = 'always')
def func_spline(x, ix, x0, a, b, c, d):
    dx = x - x0[1:][ix]
    return a[ix] + (b[ix] + (c[ix] + d[ix] * dx) * dx) * dx

# Compute piece-wise spline function for "x" out of sorted "x0" points
#@numba.njit([f'f{ii}[:](f{ii}[:], f{ii}[:], f{ii}[:], f{ii}[:], f{ii}[:], f{ii}[:])' for ii in (4, 8)],
#    cache = True, fastmath = True, inline = 'always')
def piece_wise_spline(x, x0, a, b, c, d):
    xsh = x.shape
    x = x.ravel()
    ix = np.searchsorted(x0[1 : -1], x)
    y = func_spline(x, ix, x0, a, b, c, d)
    y = y.reshape(xsh)
    return y

def main():
    t0 = np.arange(len(x0)).astype(np.float64)
    plt.plot(x0, y0)
    vs = []
    for e in (x0, y0):
        a, b, c, d = calc_spline_params(t0, e)
        x = np.linspace(0, t0[-1], 100)
        vs.append(piece_wise_spline(x, t0, a, b, c, d))
    plt.plot(vs[0], vs[1])
    plt.show()

if __name__ == '__main__':
    main()
