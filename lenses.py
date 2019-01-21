"""
Lenses module
This module handles the creation of different types of lenses, using the raytracing midule as a basis for 
individual lens components
"""

import ray_tracer as rt
import gen_collimated as rb
import matplotlib.pyplot as plt
import refractive_index as ri
from matplotlib.patches import Arc
import numpy as np

plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams['lines.linewidth'] = 0.8
plt.rcParams.update({'figure.autolayout': True})
plt.rcParams['mathtext.default']='regular'
    
class Lens:
    """
    Lens class
    Generates a lens and propagates rays through it to the output plane
    __init__: initialises with curvature intercept z0, output plane position z1, curvatures of lenses,
    refractive indices n1 and n2, wavelength and lens type. Choose between CONVEXPLANO, PLANOCONVEX, BICONVEX,
    ACHROMATIC, APOCHROMATIC, MIRROR and WATERSPHERE
    propagate_sequence: propagates ray through the sequence of lenses based on specified lens type
    genPlot: 
    genPlotWithLens:
    genPlotBundle:
    getRMS:
    getParaxial:
    """
    def __init__(self, z0 = 100, z1 = 198.45281249084675, curvature1 = 0.02, curvature2 = -0.02, curvature3 = 0.02, curvature4 = 0, n1 = 1, n2 = 1.5168, wavelength = 588*1E-9, lens = "CONVEXPLANO"):
        self.__lens = lens
        self.__z0 = z0
        self.__radius = 1/curvature1
        if self.__lens == "CONVEXPLANO":
            self.__convex = rt.SphericalRefraction(z0, curvature1, n1, n2)
            self.__plano = rt.SphericalRefraction(z0 + 5, 0, n2, n1)
            self.__sequence = [self.__convex, self.__plano]
        elif self.__lens == "PLANOCONVEX":
            self.__plano = rt.SphericalRefraction(z0, 0, n1, n2)
            self.__convex = rt.SphericalRefraction(z0 + 5, curvature2, n2, n1)
            self.__sequence = [self.__plano, self.__convex]            
        elif self.__lens == "BICONVEX":
            n2 = ri.cauchyIndex(wavelength, "BK7GLASS")
            self.__convex1 = rt.SphericalRefraction(z0, curvature1, n1, n2)
            self.__convex2 = rt.SphericalRefraction(z0 + 5, curvature2, n2, n1)
            self.__sequence = [self.__convex1, self.__convex2]            
        elif self.__lens == "ACHROMATIC":
            n_glass = ri.cauchyIndex(wavelength, "BK7GLASS")
            n_flint = ri.cauchyIndex(wavelength, "DENSEFLINT")
            self.__convex1 = rt.SphericalRefraction(z0, curvature1, n1, n_glass)
            self.__convex2 = rt.SphericalRefraction(z0 + 5, curvature2, n_glass, n_flint)            
            self.__convex3 = rt.SphericalRefraction(z0 + 10, curvature3, n_flint, n1)
            self.__sequence = [self.__convex1, self.__convex2, self.__convex3]             
        elif self.__lens == "APOCHROMATIC":
            n_glass = ri.cauchyIndex(wavelength, "BK7GLASS")
            n_flint = ri.cauchyIndex(wavelength, "DENSEFLINT")
            self.__convex1 = rt.SphericalRefraction(z0, curvature1, n1, n_glass)
            self.__convex2 = rt.SphericalRefraction(z0 + 5, curvature2, n_glass, n_flint)            
            self.__convex3 = rt.SphericalRefraction(z0 + 10, curvature3, n_flint, n_glass)
            self.__convex4 = rt.SphericalRefraction(z0 + 15, curvature4, n_glass, n1)
            self.__sequence = [self.__convex1, self.__convex2, self.__convex3, self.__convex4]            
        elif self.__lens == "MIRROR":
            self.__convex = rt.SphericalRefraction(z0, curvature1, n1, 0)
            self.__sequence = [self.__convex]
        elif self.__lens == "WATERSPHERE":
            n_water = ri.refractiveIndex(wavelength)
            self.__convex1 = rt.SphericalRefraction(z0, curvature1, n1, n_water)
            self.__convex2 = rt.SphericalRefraction(z0 + 2/curvature1, curvature2, n_water, 0)
            self.__convex3 = rt.SphericalRefraction(z0 + 2/curvature1, curvature2, n_water, n1)           
            self.__sequence = [self.__convex1, self.__convex2, self.__convex3]
        self.__OutputPlane = rt.OutputPlane(z1)
    def propagateSequence(self, ray):
        for i in self.__sequence:
            i.propagateRay(ray)            
    def genPlot(self, x_values, vec, colour = (1.0, 0.9, 0.0)):
        plt.figure(1)
        for i in x_values:
            ray = rt.Ray(pos = [i, 0.0, 80], vec = vec)
            self.propagateSequence(ray)            
            self.__OutputPlane.intercept(ray)
            vertices = ray.vertices()
            x, y, z = vertices[:, 0], vertices[:, 1], vertices[:, 2]
#            plt.axes().set_aspect('equal', 'datalim')
            plt.xlabel("z displacement (mm)")
            plt.ylabel("x displacement (mm)")
            plt.ticklabel_format(useOffset=False)
            plt.plot(z, x, color = colour)
#        plt.savefig('planoconvex_path_zoomed.pdf', format='pdf', dpi=3000)
    def genPlotWithLens(self, x_values, vec, colour = (1.0, 0.9, 0.0)):
        z, x = self.__z0 + self.__radius, 0
        fig1 = plt.figure(2)
        ax = fig1.add_subplot(111)
        ax.set_xlim(80, 122)
        ax.set_ylim(-20, 12)
        ax.set_xlabel("z displacement (mm)")
        ax.set_ylabel("x displacement (mm)")
#        ax.set_ylabel("x displacement ($x10^{-5}$ mm)")
        ax.set_aspect('equal', 'datalim')
#        ax.ticklabel_format(useOffset=False)
        ax.add_patch(Arc((z, x), 2*self.__radius, 2*self.__radius, theta1=0, theta2=360, edgecolor='black', lw=1))
#        ax.add_patch(Arc((z, x), 2*self.__radius, 2*self.__radius, theta1=-270, theta2=-90, edgecolor='black', lw=1))
#        ax.set_facecolor('black')
        angles = []
        for i in x_values:
            ray = rt.Ray(pos = [i, 0.0, -50.0], vec = vec)
            self.propagateSequence(ray)            
            self.__OutputPlane.intercept(ray)
            angles.append(self.__OutputPlane.getAngles())
            vertices = ray.vertices()
            x, y, z = vertices[:, 0], vertices[:, 1], vertices[:, 2]
            ax.plot(z, x, color = colour)
#        fig1.savefig('rainbow_path.pdf', format='pdf', dpi=3000)
        return angles
#        z = 30*[198.45281260228509]
#        x_values =[i*1E5 for i in x_values]
#        plt.plot(z, x_values, color = 'white')
    def genPlotBundle(self, vec = [0.0, 0.0, 1], colour = (1.0, 0.9, 0.0), radius = 5.0, z = 80.0):
        RayBundle = rb.CollimatedRay(start_pos_xy = [0.0, 0.0], vec = vec, max_radius = radius, n_circles = 10, ndots_incre = 3, z = z)
        ray_bundle = RayBundle.rayBundle()
        ray_pos = np.empty((0,2))
        for i in ray_bundle:
            vertices = i.vertices()
            self.propagateSequence(i)
            self.__OutputPlane.intercept(i)
            vertices = i.vertices()
            x, y, z = vertices[:, 0], vertices[:, 1], vertices[:, 2]
            ray_pos = np.vstack((ray_pos, np.array([x[-1], y[-1]])))
            plt.figure(3)
#            plt.xlim(-0.01, 0.01)
#            plt.ylim(-10, 15)
            plt.axes().set_aspect('equal', 'datalim')
            plt.xlabel("y displacement (mm)")
            plt.ylabel("x displacement (mm)")
            plt.scatter(x[-1], y[-1], s = 8, color = colour)
            plt.figure(4)
            plt.xlabel("z displacement (mm)")
            plt.ylabel("x displacement (mm)")
            plt.plot(z, x, color=colour)
#        plt.savefig('mirror_spot.pdf', format='pdf', dpi=3000)    
        x, y = ray_pos[:, 0], ray_pos[:, 1]
        rms = RayBundle.calcRMS(x, y)
        return rms
    def getRMS(self, radius = 5.0):
        RayBundle = rb.CollimatedRay(start_pos_xy = [0.0, 0.0], max_radius = radius, n_circles = 10, ndots_incre = 3, z = 0.0)        
        ray_bundle = RayBundle.rayBundle()
        ray_pos = np.empty((0,2))
        for i in ray_bundle:
            self.propagateSequence(i)
            self.__OutputPlane.intercept(i)
            vertices = i.vertices()
            x, y, z = vertices[:, 0], vertices[:, 1], vertices[:, 2]
            ray_pos = np.vstack((ray_pos, np.array([x[-1], y[-1]])))
        x, y = ray_pos[:, 0], ray_pos[:, 1]
        rms = RayBundle.calcRMS(x, y)
        return rms        
    def getParaxial(self, pos = [0.0000001, 0.0, 0.0]):
        if (len(pos) != 3):
            raise Exception("Position vector must contain a list of three parameters.") 
        ray = rt.Ray(pos = pos, vec = [0.0, 0.0, 1])
        self.propagateSequence(ray)            
        self.__OutputPlane.intercept(ray)
        self.__vertices = np.empty((0, 3))
        for i in ray.vertices():
            self.__vertices = np.vstack((self.__vertices, i))
        x, y, z = self.__vertices[:, 0], self.__vertices[:, 1], self.__vertices[:, 2]
        m = (x[-1] - x[-2])/(z[-1] - z[-2])
        c = x[-1] - m*z[-1]
        c2 = x[-2] - m*z[-2]
        z0 = c/-m
        z1 = c2/-m
        return (z0, z1)