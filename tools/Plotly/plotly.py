# -*- coding: utf-8 -*-
# Plotly
"""
Args: {
    object format: stl,
    array data: int,
    coordinates: (int, int, int)
}
Output: temperature: int
"""

import plotly
import numpy as np
from stl import mesh
import plotly.graph_objects as go
import urllib

from setup import ARRAY, MIN, MAX


class Coordinates:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    # Initialization matrix for data
    @classmethod
    def _init_heat(cls):
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
        return heat

    # Console Output temperature
    def coordinates_heat(self):
        heat = []
        heat = self._init_heat()
        ds = u'\N{DEGREE SIGN}'
        x = int(self.x)
        y = int(self.y)
        z = int(self.z)
        pos = heat[x, y, z]
        print(
            f"Значение температуры по значениям [{x}; {y}; {z}] = {pos}{ds}C")


def stl_to_mesh(stl):
    p, q, r = stl.vectors.shape
    vert, ixr = np.unique(stl.vectors.reshape(p*q, r),
                          retur_inverse=True, axis=0)
    I = np.take(ixr, [3*k for k in range(p)])
    J = np.take(ixr, [3*k+1 for k in range(p)])
    K = np.take(ixr, [3*k+2 for k in range(p)])
    return vert, I, J, K


def visual_mesh(path):
    my_mesh = mesh.Mesh.from_file(path)
    verices, I, J, K = stl_to_mesh(my_mesh)
    x, y, z = verices.T
    colorscale = [[0, '#555555'], [1, '#e5dee5']]
    mesh3D = go.Mesh3d(
        x=x,
        y=y,
        z=z,
        i=I,
        j=J,
        k=K,
        flatshading=True,
        colorscale=colorscale,
        intensity=z,
        name="Bulat STHE",
        showscale=False
    )
    title = "Mesh3D Bulat STHE"
    layout = go.Layout(paper_bgcolor='rgb(1,1,1)',
                       title_text=title, title_x=0.5,
                       font_color='white',
                       width=800,
                       height=800,
                       scene_camera=dict(eye=dict(x=1.25, y=-1.25, z=1)),
                       scene_xaxis_visible=False,
                       scene_yaxis_visible=False,
                       scene_zaxis_visible=False,
                       )
    fig = go.Figure(data=[mesh3D], layout=layout)
    fig.show()


if __name__ == '__main__':
    path = 'assets/model.stl'
    visual_mesh(path)
