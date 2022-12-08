# Plotly
"""
Args: {
    object format: stl,
    array data: int,
    coordinates: (int, int, int)
}
Output: temperature: int
"""

import numpy as np

from setup import ARRAY, MIN, MAX


# Initialization matrix for data
def _init_heat():
    heat = np.array([[[0 for _ in range(ARRAY[2])] for _ in range(ARRAY[1])]
                     for _ in range(ARRAY[0])])
    step = round((MAX - MIN) / ARRAY[1])
    for x in range(ARRAY[0]):
        a2 = [0 for _ in range(ARRAY[1])]
        for y in range(ARRAY[1]):
            a3 = [0 for _ in range(ARRAY[2])]
            for z in range(ARRAY[2]):
                a3[z] = MAX if y == 4 else MIN + step * y
            a2[y] = a3
        heat[x] = a2
    print(heat)


if __name__ == '__main__':
    _init_heat()
