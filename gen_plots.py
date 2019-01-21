# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 13:53:31 2017

@author: rtw16
"""

z0 = 100
curvature = 0.03
radius = 1/curvature
n1 = 1.0
n2 = 1.5
z1 = 190
lens = SphericalRefraction(z0, curvature, n1, n2)
OutputPlane = OutputPlane(z1)
x_values = np.linspace(-0.5, 0.5, 30)

z, x = z0, 0

# Figure setup
fig, ax = plt.subplots()
ax.set_xlim(166.65, 166.68)
ax.set_ylim(-0.0001, 0.0001)
#ax.xaxis.set_major_formatter(mtick.FormatStrFormatter('%.3f'))
#ax.yaxis.set_major_formatter(mtick.FormatStrFormatter('%.1e'))
ax.set_xlabel("z displacement (mm)")
ax.set_xlabel("x displacement (mm)")
#ax.set_ylabel("x displacement ($x10^{-4}$ mm)")
ax.ticklabel_format(useOffset=False)
# Arcs
ax.add_patch(Arc((z, x), 2*radius, 2*radius, theta1=179, theta2=-179, edgecolor='white', lw=1))
ax.set_facecolor('black')

for i in x_values:
    ray1 = Ray(pos = [i, 0.0, -50.0], vec = [0.0, 0.0, 1])
    lens.propagateRay(ray1)
    OutputPlane.intercept(ray1)
    vertices = ray1.vertices()
#    print(vertices)
    x, y, z = vertices[:, 0], vertices[:, 1], vertices[:, 2]
    plt.figure(1)
#    x = [i*10000 for i in x]
    plt.plot(z, x, color='white')
    plt.figure(2)
    plt.scatter(y[2], x[2])
    plt.xlabel("position, y")
    plt.ylabel("position, x")
    
z = 30*[166+2/3]
plt.figure(1)
#x_values = [i*10000 for i in x_values]
plt.plot(z, x_values, color='white')
#plt.savefig('aberration.pdf', format='pdf', dpi=3000)

z0 = 100
curvature = 0.03
radius = 1/curvature
n1 = 1.0
n2 = 1.5
z1 = 220
lens = SphericalRefraction(z0, curvature, n1, n2)
OutputPlane = OutputPlane(z1)
x_values = np.linspace(-0.5, 0.5, 30)

z, x = z0 + radius, 0

# Figure setup
fig, ax = plt.subplots()
ax.set_xlim(199.98, 200.01)
ax.set_ylim(-0.00008, 0.00008)
#ax.xaxis.set_major_formatter(mtick.FormatStrFormatter('%.3f'))
#ax.yaxis.set_major_formatter(mtick.FormatStrFormatter('%.1e'))
ax.set_xlabel("z displacement (mm)")
ax.set_xlabel("x displacement (mm)")
#ax.set_ylabel("x displacement ($x10^{-4}$ mm)")
ax.ticklabel_format(useOffset=False)
# Arcs
ax.add_patch(Arc((z, x), 2*radius, 2*radius, theta1=179, theta2=-179, edgecolor='white', lw=1))
ax.set_facecolor('black')

for i in x_values:
    ray1 = Ray(pos = [i, 0.0, -50.0], vec = [0.0, 0.0, 1])
    lens.propagateRay(ray1)
    OutputPlane.intercept(ray1)
    vertices = ray1.vertices()
#    print(vertices)
    x, y, z = vertices[:, 0], vertices[:, 1], vertices[:, 2]
    plt.figure(1)
#    x = [i*10000 for i in x]
    plt.plot(z, x, color='white')
    plt.figure(2)
    plt.scatter(y[2], x[2])
    plt.xlabel("position, y")
    plt.ylabel("position, x")
    
z = 30*[200]
plt.figure(1)
#x_values = [i*10000 for i in x_values]
plt.plot(z, x_values, color='white')
#plt.savefig('aberration.pdf', format='pdf', dpi=3000)

print(paraxial())

def genPlot(self, x_values):
    z, x = self.__z0 + self.__radius, 0
    fig, ax = plt.subplots()
    #ax.set_xlim(199.98, 200.01)
    #ax.set_ylim(-0.00008, 0.00008)
    ax.set_xlabel("z displacement (mm)")
    ax.set_ylabel("x displacement (mm)")
    #ax.set_ylabel("x displacement ($x10^{-4}$ mm)")
    ax.ticklabel_format(useOffset=False)
    ax.add_patch(Arc((z, x), 2*self.__radius, 2*self.__radius, theta1=179, theta2=-179, edgecolor='black', lw=1))
    #ax.set_facecolor('black')
    for i in x_values:
        ray = rt.Ray(pos = [i, 0.0, -50.0], vec = [0.0, 0.0, 1])
        self.propagateSequence(ray)            
        self.__OutputPlane.intercept(ray)
        vertices = ray.vertices()
        x, y, z = vertices[:, 0], vertices[:, 1], vertices[:, 2]
        plt.plot(z, x)
    z = 30*[self.__z1]
    plt.plot(z, x_values)