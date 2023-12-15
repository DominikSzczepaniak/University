import numpy as np
from matplotlib import pyplot as plt
from scipy.special import comb
from dane import punkty_kontrolne, wagi

def bernstein(i, n, t):
    """
     The i-th Bernstein polynomial of degree n
    """
    return comb(n, i) * (t ** (n - i)) * (1 - t) ** i


def bezier_curve(nodes, weights = None, mesh_size = 100):
    """
        Returns the x- and y-arrays of points in the (weighted) Bézier curve
        constructed for the given nodes and weights.
        weights = array with length equal to number of nodes
        mesh_size = number of points in the Bézier curve rendering.
    """
    if weights is None:
        node_x = np.array([n[0] for n in nodes])
        node_y = np.array([n[1] for n in nodes])
        t = np.linspace(0.0, 1.0, mesh_size)
        numerator = np.array(
            [bernstein(i, len(nodes) - 1, t) for i in
             range(0, len(nodes))])
        p_x = np.dot(node_x, numerator)
        p_y = np.dot(node_y, numerator)
        return p_x, p_y
    else:
        if mesh_size is None:
            return _weighted_bezier_curve(nodes, weights)
        else:
            return _weighted_bezier_curve(nodes, weights,
                                          mesh_size = mesh_size)


def _weighted_bezier_curve(nodes, weights, mesh_size = 100):
    node_x = np.array([n[0] for n in nodes])
    node_y = np.array([n[1] for n in nodes])
    weights = np.array(weights)

    t = np.linspace(0.0, 1.0, mesh_size)
    weighted_bernstein = np.array(
        [bernstein(i, len(nodes) - 1, t) * weights[i] for i in
         range(0, len(nodes))])

    sum_weighted_bernstein = np.sum(weighted_bernstein, axis = 0)

    p_x = np.divide(np.dot(node_x, weighted_bernstein), sum_weighted_bernstein)
    p_y = np.divide(np.dot(node_y, weighted_bernstein), sum_weighted_bernstein)
    return p_x, p_y


if __name__ == '__main__':
    # Define nodes & weights
    nodes = punkty_kontrolne
    weights = wagi

    # Compute curve 
    p_x, p_y = bezier_curve(nodes, weights = weights, mesh_size = 100)

    # Plot curve
    plt.plot(p_x, p_y, 'r-')

    # Plot nodes
    nodes_x = [n[0] for n in nodes]
    nodes_y = [n[1] for n in nodes]
    dot_size = [1 + w ** 2 for w in weights]
    plt.scatter(nodes_x, nodes_y, c = 'k', s = dot_size)

    for n in range(len(nodes)):
        plt.text(nodes_x[n], nodes_y[n], n)

    plt.show()