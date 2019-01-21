"""
Main module to run plots and optimisation functions for monochromatic and chromatic rays
Note: Run one function at a time as optimisation functions can take a while
"""

import numpy as np
import monochromatic as mn
import chromatic as ch

""" 
MONOCHROMATIC RAYS
Functions generate three plots:
1. Path diagram of rays of varying x positions
2. Spot diagram at paraxial focus
3. Ray bundle path of 5mm beam diameter

"""

x_values = np.linspace(-0.5, 0.5, 30)
vec = [0.0, 0.0, 1.0]

#print(mn.runConvexPlano(x_values, vec)) # returns paraxial, rms, optimal_z, optimal_curvature
#print(mn.runPlanoConvex(x_values, vec)) # returns paraxial, rms, optimal_z
#print(mn.runBiconvex(x_values, vec)) # returns paraxial, rms, optimal_z, optimal_curvatures, Collingdon Shape Factor, actualCSF
#print(mn.runMirror(x_values, vec)) # returns paraxial, rms, optimal_z

""" 
CHROMATIC RAYS
"""

""" BICONVEX LENS """
""" Generates a path diagram of white light from 380 to 699 nm through biconvex lens to show chromatic aberration"""

x_values = [-0.01, 0, 0.01]
vec = [0.0, 0.0, 1.0]
wavelengths = np.linspace(380*1E-9, 699*1E-9, 200)
#ch.runBiconvexChrom(x_values, vec, wavelengths)

"""
Functions generate three plots:
1. Path diagram of rays of varying x positions
2. Spot diagram at position of Circle of Least Confusion where minimum RMSD lies
3. Ray bundle path of 5mm beam diameter
"""

""" ACHROMATIC LENS """
x_values = [-5.0, 0, 5.0]
vec = [0.0, 0.0, 1.0]
wavelengths = [486.1*1E-9, 656.3*1E-9]
#print(ch.runAchromatic(x_values, vec, wavelengths))

""" APOCHROMATIC LENS """
x_values = [-5.0, 0, 5.0]
vec = [0.0, 0.0, 1.0]
wavelengths = [486.1*1E-9, 589.3*1E-9, 656.3*1E-9]
#print(ch.runApochromatic(x_values, vec, wavelengths))

""" RAINBOW WATERSPHERE """
""" 
Generates a path diagram of white light from 380 to 699 nm through a spherical 
water droplet to display rainbow formation (x_values = [8.3])
Plots a histogram to show number of rays against angles made with positive z direction 
(use x_values = np.linspace(5, 9.5, 50))
"""

x_values = np.linspace(5, 9.5, 50)
x_values = [8.3]
vec = [0.0, 0.0, 1.0]
wavelengths = np.linspace(380*1E-9, 699*1E-9, 100)
#ch.runWatersphere(x_values, vec, wavelengths)