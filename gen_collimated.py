"""
Collimated Beam module
This module is for creating a bundle of collimated rays 
"""

import numpy as np
import ray_tracer as rt

class CollimatedRay:
    """
    CollimatedRay class
    Generates a bundle of rays with
    __init__: initialises with initial direction, start position, max radius of beam, number of circles, ndots increment for each radius
    rayBundle: returns the rays generated with each position and direction vector
    calcRMS: returns the root-mean-square deviation (RMSD) from the optical axis
    """
    def __init__(self, vec = [0.0, 0.0, 1], start_pos_xy = [0.0, 0.0], max_radius = 20, n_circles = 2, ndots_incre = 3, z = -30.0):
        new_pos = np.append(start_pos_xy, z)
        ray = rt.Ray(pos = new_pos, vec = vec)
        self.__rays = [ray]
        n_dots = 0
        radius = max_radius/n_circles
        for i in range(n_circles):
            n_dots += ndots_incre + 1
            new_radius = radius*(i+1)
            thetas = np.linspace(0, 2*np.pi, n_dots+1)
            j = 0
            while (j < len(thetas)-1):
                x, y = new_radius*np.cos(thetas[j]), new_radius*np.sin(thetas[j])
                ray = rt.Ray(pos = [x, y, z], vec = vec)  
                self.__rays.append(ray)
                j += 1
    def rayBundle(self):
        return self.__rays
    def calcRMS(self, x, y):
        x_mean = np.mean(x)
        y_mean = np.mean(y)
        r_squared_list = (x-x_mean)**2 + (y-y_mean)**2
        r_squared_mean = np.mean(r_squared_list)
        rms = np.sqrt(r_squared_mean)
        return rms