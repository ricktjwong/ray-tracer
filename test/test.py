# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 09:36:16 2017

@author: rtw16
"""

import numpy as np

# Line-plane intersection

def line_plane_intersect(ray_point, k_hat, plane_point, n_hat):
    n_dot_u = np.dot(k_hat, n_hat)
    print(n_dot_u)
    if abs(n_dot_u) == 0:
        raise RuntimeError("No intersection, or line is within plane")
    ray_point = np.array(ray_point)
    k_hat = np.array(k_hat)
    n_hat = np.array(n_hat)
    plane_point = np.array(plane_point)
    gamma = -(np.dot(-plane_point, n_hat) + np.dot(ray_point, n_hat))/(np.dot(k_hat, n_hat))
    intersection = ray_point + gamma*k_hat
    return intersection

print(line_plane_intersect([1,4,0], [1, 2, 1], [2,5,5], [0,0,-1]))

def intercept2(self, ray, n_hat, ray_point, plane_point):
    n_dot_u = np.dot(ray.k(), n_hat)
    print(n_dot_u)
    if abs(n_dot_u) == 0:
        raise RuntimeError("No intersection, or line is within plane")
    ray_point = np.array(ray_point)
    n_hat = np.array(n_hat)
    plane_point = np.array(plane_point)
    gamma = -(np.dot(-plane_point, n_hat) + np.dot(ray_point, n_hat))/(np.dot(ray.k(), n_hat))
    intersection = ray_point + gamma*ray.k()
    return intersection

## Circle
#z = np.linspace(66.6, 100, 100)
#print (z0-radius)
#new_z = []
#x_top, x_bottom = [], []
#for i in z:
#    if (radius**2>(i-z0)**2):
#        new_z.append(i)
#        x_top.append(+np.sqrt(radius**2 - (i-z0)**2))
#        x_bottom.append(-np.sqrt(radius**2 - (i-z0)**2))
#plt.figure(1)
#plt.plot(new_z, x_bottom, color = 'black')
#plt.plot(new_z, x_top, color = 'black')
#plt.xlabel("position, z")
#plt.ylabel("position, x")

#a = np.array([])
#b = np.array([2, 3])
#c = np.vstack((a, b))
#print(c)
#
#vertices = np.array([[ -5.00000000e-01,   0.00000000e+00,  -5.00000000e+01], [-5.00000000e-01,   0.00000000e+00,   1.00002500e+02], [ -4.82971476e-01,   0.00000000e+00,   1.05000122e+02], [1.43996350e-05,   0.00000000e+00,   1.98452812e+02]])
#vertice2 = np.array([[  5.00000000e-01,   0.00000000e+00,  -5.00000000e+01], [5.00000000e-01,   0.00000000e+00,   1.00002500e+02], [  4.82971476e-01,   0.00000000e+00,   1.05000122e+02], [ -1.43996350e-05,   0.00000000e+00,   1.98452812e+02]])
#x, y, z = vertices[:, 0], vertices[:, 1], vertices[:, 2]
#plt.figure(1)
#plt.plot(z, x)
#x, y, z = vertice2[:, 0], vertices[:, 1], vertices[:, 2]
#plt.plot(z, x)
#vertices = np.vstack((vertices, vertice2))
#x, y, z = vertices[:, 0], vertices[:, 1], vertices[:, 2]
#plt.figure(2)
#plt.plot(z, x)
    
#wavelengths = np.linspace(0, 10, 10)
#print(wavelengths)
#print(np.repeat(wavelengths, 2))
#
#print(-7.10542733101e-14 > -1E-10)
    
x = [1,2,3,4,5]
print(np.mean(x))

