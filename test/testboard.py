# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 14:09:47 2017

@author: rtw16
"""

import ray_tracer as rt
import gen_collimated as rb
import matplotlib.pyplot as plt
from matplotlib.patches import Arc
import numpy as np

def paraxial():
    pos1, pos2, pos3, pos4 = ray1.vertices()
    m = (pos3[0] - pos4[0])/(pos3[2] - pos4[2])
    c = pos3[0] - m*pos3[2]
    c2 = pos4[0] - m*pos4[2]
    z0 = c/-m
    z1 = c2/-m
    return (z0, z1)

""" BICONVEX VARYING Z """

z0 = 100
curvature1 = 0.02
curvature2 = -0.02
radius = 1/curvature1
n1 = 1.0
n2 = 1.5168
z1 = 205

x_values = np.linspace(-0.001, 0.001, 30)
convex1 = rt.SphericalRefraction(z0, curvature1 , n1, n2)
convex2 = rt.SphericalRefraction(z0+5, curvature2, n2, n1)
OutputPlane = rt.OutputPlane(z1)

ray_pos = np.empty((0,2))
    
z, x = z0 + radius, 0

# Figure setup
fig, ax = plt.subplots()
#ax.set_xlim(199.98, 200.01)
#ax.set_ylim(-0.00008, 0.00008)
ax.set_xlabel("z displacement (mm)")
ax.set_ylabel("x displacement (mm)")
#ax.set_ylabel("x displacement ($x10^{-4}$ mm)")
ax.ticklabel_format(useOffset=False)
# Arcs
#ax.add_patch(Arc((z, x), 2*radius, 2*radius, theta1=179, theta2=-179, edgecolor='black', lw=1))
#ax.set_facecolor('black')

for i in x_values:
    ray1 = rt.Ray(pos = [i, 0.0, -50.0], vec = [0.0, 0.0, 1])
    convex1.propagateRay(ray1)
    convex2.propagateRay(ray1)    
    OutputPlane.intercept(ray1)
    vertices = ray1.vertices()
#    print(vertices)
    x, y, z = vertices[:, 0], vertices[:, 1], vertices[:, 2]
    plt.figure(8)
#    x = [i*10000 for i in x]
    plt.plot(z, x, color='black')
    
z = 30*[200]
plt.figure(1)
#x_values = [i*10000 for i in x_values]
plt.plot(z, x_values, color='black')
#plt.savefig('aberration.pdf', format='pdf', dpi=3000)

print(paraxial())

""" BICONVEX RMS """

z0 = 100
curvature1 = 0.02
curvature2 = -0.02
radius = 1/curvature1
n1 = 1.0
n2 = 1.5168
z1 = 152.53622696550048

RayBundle = rb.CollimatedRay([0.0, 0.0], 5.0, 10, 3, 0.0)
ray_bundle = RayBundle.rayBundle()

convex1 = rt.SphericalRefraction(z0, curvature1 , n1, n2)
convex2 = rt.SphericalRefraction(z0+5, curvature2, n2, n1)
OutputPlane = rt.OutputPlane(z1)

ray_pos = np.empty((0,2))
    
for i in ray_bundle:
    vertices = i.vertices()
    x, y = vertices[0], vertices[1]
    plt.figure(9)
    plt.axes().set_aspect('equal', 'datalim')
    plt.scatter(x, y)
    convex1.propagateRay(i)        
    convex2.propagateRay(i)
    OutputPlane.intercept(i)
    vertices = i.vertices()  
    x, y, z = vertices[:, 0], vertices[:, 1], vertices[:, 2]
    ray_pos = np.vstack((ray_pos, np.array([x[3], y[3]])))
    plt.ticklabel_format(axis='x', style='sci', useOffset=False)
    plt.figure(10)
    plt.axes().set_aspect('equal', 'datalim')
#    plt.xlim(-0.004, 0.004)  
#    plt.ylim(-0.004, 0.004)
    plt.scatter(x[3], y[3])
    plt.figure(11)
    plt.plot(z, x, color='black')
    
x, y = ray_pos[:, 0], ray_pos[:, 1]

rms = RayBundle.calcRMS(x, y)

print(rms)