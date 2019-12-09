

import numpy as np
import matplotlib.pyplot as plt

from numpy.random import rand
from matplotlib.colors import ListedColormap

def creation_grille(p, n):
    grille = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if rand() < p:
                grille[i][j] = 1.
    return grille