"""
Refractive index module
This module handles the wavelength dependent refractive index of materials - water and various glasses
"""

import numpy as np
import matplotlib.pyplot as plt

def refractiveIndex(wavelength):
    """
    Returns a refractive index with the specified wavelength.
    Based on the experimental model by the International Association for the Properties of Water and Steam
    http://www.iapws.org/relguide/rindex.pdf
    """
    rho = 1000
    T = 298.15
    a0 = 0.244257733
    a1 = 9.74634476*1E-3
    a2 = -3.73234996*1E-3
    a3 = 2.68678472*1E-4
    a4 = 1.58920570*1E-3      
    a5 = 2.45934259*1E-3
    a6 = 0.900704920
    a7 = -1.66626219*1E-2
    lambda_uv2, lambda_ir2 = 0.2292020**2, 5.432937**2
    T_ref = 273.15
    rho_ref = 1000 
    lambda_ref = 0.589*1E-6
    rho_bar = rho/rho_ref
    T_bar = T/T_ref
    lam_bar2 = (wavelength/lambda_ref)**2
    alpha = a0 + a1*rho_bar + a2*T_bar + a3*lam_bar2*T_bar + a4/lam_bar2 + a5/(lam_bar2 - lambda_uv2) + a6/(lam_bar2 - lambda_ir2) + a7*rho_bar**2
    beta = alpha*rho_bar
    n = np.sqrt((2*beta+1)/(1-beta))
    return n

def cauchyIndex(wavelength, material):
    """
    Takes in two parameters, wavelengt and material. Choose between FUSED_SILICA, BK7GLASS, CROWNGLASS, DENSEFLINT
    These calculate the Cauchy Equations for refractive index for a specified material.
    These equations are accurate for the visible light range (380 - 699 nm).
    """
    if material == "FUSED_SILICA":
        B, C = 1.4580, 0.00354
    elif material == "BK7GLASS":
        B, C = 1.5046, 0.00420
    elif material == "CROWNGLASS":
        B, C = 1.5220, 0.00459
    elif material == "DENSEFLINT":
        B, C = 1.7280, 0.01342
    wavelength = wavelength*1E6
    n = B + C/wavelength**2
    return n

def splitAngles(start, end, number, all_angles):
    """
    Separates angles of intersection with plane for plotting as a histogram.
    """
    angle_dict = dict()
    intervals = np.linspace(start, end, number)
    step = (end-start)/number
    for i in intervals:
        N = len([x for x in all_angles if x > i and x < i+step])
        mean = i + step/2
        angle_dict[str(mean)[:4]] = N
    return angle_dict

def plotHistogram(angle_dict):
    """
    Plots a histogram according to the dictionary angle_dict
    """
    x_values = []
    y_values = []
    for i,j in angle_dict.items():
        print(i, j)
        x_values.append(i)
        y_values.append(j)
        
    n_groups = 15
    
    fig, ax = plt.subplots()
    
    index = np.arange(n_groups)
    bar_width = 0.35
    
    opacity = 1.0
    
    rects1 = plt.bar(index, y_values, bar_width, alpha=opacity, color='blue', edgecolor='black')
    
    plt.xlabel('Mean angle (degrees)')
    plt.ylabel('Number')
    plt.xticks(index, x_values)
#    plt.savefig('rainbow_angles.pdf', format='pdf', dpi=3000)    
    plt.show()

def wavelengthToRGB(wavelength, gamma=0.8):
    """ 
    Converts a given wavelength of light to an approximate RGB color value. 
    The wavelength must be given in nanometers in the range from 380 nm to 750 nm.
    Based on code by Dan Bruton:
    http://www.physics.sfasu.edu/astro/color/spectra.html
    """
    wavelength = float(wavelength)
    if wavelength >= 380 and wavelength <= 440:
        attenuation = 0.3 + 0.7 * (wavelength - 380) / (440 - 380)
        R = ((-(wavelength - 440) / (440 - 380)) * attenuation) ** gamma
        G = 0.0
        B = (1.0 * attenuation) ** gamma
    elif wavelength >= 440 and wavelength <= 490:
        R = 0.0
        G = ((wavelength - 440) / (490 - 440)) ** gamma
        B = 1.0
    elif wavelength >= 490 and wavelength <= 510:
        R = 0.0
        G = 1.0
        B = (-(wavelength - 510) / (510 - 490)) ** gamma
    elif wavelength >= 510 and wavelength <= 580:
        R = ((wavelength - 510) / (580 - 510)) ** gamma
        G = 1.0
        B = 0.0
    elif wavelength >= 580 and wavelength <= 645:
        R = 1.0
        G = (-(wavelength - 645) / (645 - 580)) ** gamma
        B = 0.0
    elif wavelength >= 645 and wavelength <= 750:
        attenuation = 0.3 + 0.7 * (750 - wavelength) / (750 - 645)
        R = (1.0 * attenuation) ** gamma
        G = 0.0
        B = 0.0
    else:
        R = 0.0
        G = 0.0
        B = 0.0

    return (float(R), float(G), float(B))