# -*- coding: utf-8 -*-
"""
Raytracer module
This module is a simple 3-D optical ray tracer and is used to model
simple optical systems. It contains the fundamental elements of optical
systems such as rays and spherical surfaces.
"""

import numpy as np

class Ray:
    """
    Ray class
    	Creates a ray propagating through a medium with the following methods 
	__init__: initialises a ray with an inital point and direction
	p: returns the list of points that the ray has propagated through
	k: returns the current direction vector of the ray
	append: appends a new point and direction to the ray
	vertices: returns the list of points
    """
    def __init__(self, pos = [0.0, 0.0, 0.0], vec = [0.0, 0.0, 0.0]):
        self.__pos = np.array(pos)
        self.__vec = np.array(vec)
        self.__allpos = np.array(pos)  
        if (len(self.__pos) != 3 or len(self.__vec) != 3):
            raise Exception("Only three parameters accepted")        
    def __repr__(self):
        return "%s(pos=%s, vec=%s)" % ("Ray", self.__pos, self.__vec)
    def __str__(self):
        return "(%s, %s)" % (self.__pos, self.__vec)
    def p(self):
        return self.__pos
    def k(self):
        return self.__vec
    def append(self, p, k):
        p, k = np.array(p), np.array(k)
        self.__allpos = np.vstack((self.__allpos, p))
        self.__pos, self.__vec = p, k
        return  self
    def vertices(self):
        return self.__allpos

class OpticalElement:
    """
    OpticalElement class
    Base class for all optical elemnents in this project
    """   
    def propagateRay(self, ray):
        "propagate a ray through the optical element"
#        raise NotImplementedError()
        pos_q = self.intercept(ray)
        k2_hat = self.refract(ray)
        ray.append(pos_q, k2_hat)
        return ray.p(), ray.k()
        
class SphericalRefraction(OpticalElement):
    """
    SphericalRefraction class
    Creates a ray propagating through a medium with the following methods 
	__init__: initialises a spherical surface with z-intercept, curvature, refractive index n1, n2
    refractive indices and aperture radius
    intercept: returns the position vector of the ray at the intercept
    refract: handles the refraction of the ray. For reflection, set n2 = 0
    """
    def __init__(self, z0 = 100, curvature = 0.03, n1 = 1, n2 = 1.5, a_radius = 0.0):
        if curvature > 0:            
            self.__radius = abs(1/curvature)
            self.__z0 = np.array([0, 0, z0 + self.__radius])
        elif curvature < 0:
            self.__radius = abs(1/curvature)
            self.__z0 = np.array([0, 0, z0 - self.__radius])
        else:
            self.__z0 = z0
        self.__curvature = curvature
        self.__n1, self.__n2 = n1, n2
        self.__a_radius = a_radius
    def intercept(self, ray):
        pos_p, vec_k = ray.p() - self.__z0, ray.k()
        mag_p = np.linalg.norm(pos_p)
        k_hat = vec_k/np.linalg.norm(vec_k)
        p_dot_k = np.dot(pos_p, k_hat)
        if self.__curvature == 0:
            l = (self.__z0-ray.p()[2])/ray.k()[2]
        if self.__curvature > 0:
            sqrt_term = p_dot_k**2 - (mag_p**2 - self.__radius**2)
            if sqrt_term < 0 and sqrt_term > -1E-10:
                l = -p_dot_k
            else:    
                l = -p_dot_k - np.sqrt(sqrt_term)
        elif self.__curvature < 0:
            sqrt_term = p_dot_k**2 - (mag_p**2 - self.__radius**2)
            if sqrt_term < 0 and sqrt_term > -1E-10:
                l = -p_dot_k
            else:
                l = -p_dot_k + np.sqrt(sqrt_term)
        self.__pos_q = pos_p + l*k_hat + self.__z0
        return self.__pos_q
    def refract(self, ray):
        n1, n2 = self.__n1, self.__n2
        vec_k = ray.k()
        i_vec = vec_k/np.linalg.norm(vec_k)
        n = self.__pos_q - self.__z0
        if self.__curvature == 0:
            n_hat = np.array([0, 0, -1])
        elif self.__curvature > 0:
            n_hat = n/np.linalg.norm(n)
        elif self.__curvature < 0:
            n_hat = -n/np.linalg.norm(n)
        if n2 == 0:
            k2 = i_vec - 2*n_hat*(np.dot(i_vec, n_hat))
            k2_hat = k2/np.linalg.norm(k2)
            return k2_hat
        else:
            n_ratio = n1/n2
            theta_i = np.arccos(np.dot(i_vec, n_hat))
            if (np.sin(theta_i) > n2/n1 and n1 > n2):
                k2 = i_vec - 2*n_hat*(np.dot(i_vec, n_hat))
                k2_hat = k2/np.linalg.norm(k2)
                return k2_hat
            else:
                cos_theta_i = -np.dot(i_vec, n_hat)
                theta_i = np.arccos(np.dot(i_vec, n_hat))
                theta_r = np.arcsin((n1/n2)*np.sin(theta_i))
                k2 = n_ratio*i_vec + (n_ratio*cos_theta_i-np.cos(theta_r))*n_hat
                k2_hat = k2/np.linalg.norm(k2)
                return k2_hat
                
class OutputPlane(OpticalElement):
    """
    OutputPlane class
    Inherits from OpticalElement, handles intercept and angles on intersection with plane
	__init__: initialises a plane at position z1
    intercept: returns the position of ray intersection with plane
    getAngles: returns angle made with plane
    """
    def __init__(self, z1 = 20):
        self.__z1 = z1
    def intercept(self, ray):
        distance = (self.__z1 - ray.p()[2])/ray.k()[2]
        if distance < 0:
            self.__z1 = -self.__z1
            distance = (self.__z1 - ray.p()[2])/ray.k()[2]
#            raise Exception("distance is less than zero")
        intercept = ray.p() + distance*ray.k()
        ray.append(intercept, ray.k())
        angle = -np.dot(ray.k()/np.linalg.norm(ray.k()), [0, 0, 1.0])
        self.__angle = np.arccos(angle)*180/np.pi
        return intercept
    def getAngles(self):
        return self.__angle