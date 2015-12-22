# coding: utf-8

from matplotlib.tri import Triangulation
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import random


class Polygons(object):
    # Кол-во точек
    def __init__(self):
        self.POINTS_NUM = 10

    def create_triangles(self, plot=False):
        random_float = lambda: [random.uniform(0, 1) for i in range(self.POINTS_NUM)]
        x_test = random_float()
        y_test = random_float()
        z_test = random_float()
        triangles = Triangulation(x_test, y_test)

        points = [
            [
                x_test[i],
                y_test[i],
                z_test[i]
            ]
            for i in range(self.POINTS_NUM)
        ]
        points = np.array(points)
        triangles_points = lambda points, triangles: [
            [points[a], points[b], points[c]]
            for a, b, c in triangles
            ]
        triangles_coordinates = triangles_points(points, triangles.triangles)
        if plot:
            fig = plt.figure()
            ax = fig.add_subplot(111, projection='3d')
            plt.gca().set_aspect('equal')
            ax.plot_trisurf(
                points[:, 0], points[:, 1], points[:, 2],
                triangles=triangles.triangles,
                cmap=plt.cm.bone)
            plt.show()

        return triangles_coordinates



