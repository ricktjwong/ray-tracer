"""
Optimisation module
This module contains functions to optimise (i) z position or (2) curvatures which give the minimum RMSD
"""

import lenses as lens
from scipy.optimize import fmin_tnc
import numpy as np

def findCOLC(lenstype = "CONVEXPLANO", curvature1 = 0.02, curvature2 = 0.02, z1 = 198.45278442247201):
    """ Finds the RMS and position of the Circle of Least Confusion """
    def minRMS(z1):
        lensType = lens.Lens(lens = lenstype, z1 = z1, curvature1 = curvature1, curvature2 = curvature2)
        rms = lensType.getRMS(radius = 5.0)
        return rms
    output = fmin_tnc(func = minRMS, x0 = [z1], approx_grad = True, stepmx = 0.0001, bounds = [(z1 - 20, z1 + 20)])
    return output

def optimiseCurvature(lenstype = "BICONVEX", z1 = 152.5362269967614, curvature1 = 0.02, curvature2 = -0.02):
    def minRMS(curvatures):
        lensType = lens.Lens(lens = lenstype, z1 = z1, curvature1 = curvatures[0], curvature2 = curvatures[1])
        rms = lensType.getRMS()
        return rms
    output = fmin_tnc(func = minRMS, x0 = [curvature1, curvature2], approx_grad = True, stepmx = 0.0001, bounds = [(1e-8, 0.04), (-0.04, -1e-8)])
    return output

def findCOLCWavelength(lenstype = "BICONVEX", curvature1 = 0.02, curvature2 = 0.02, curvature3 = 0.02, z1 = 198.45278442247201, radius = 5.0, wavelengths = [699*1E-9]):
    """ Finds the RMS and position of the Circle of Least Confusion """
    def minRMS(z1):
        rms2 = []
        for i in wavelengths:
            lensType = lens.Lens(lens = lenstype, z1 = z1, curvature1 = curvature1, curvature2 = curvature2, curvature3 = curvature3, wavelength = i)
            rms2.append((lensType.getRMS(radius = radius))**2)
        rms_new = np.sqrt(np.mean(rms2))
        return rms_new
    output = fmin_tnc(func = minRMS, x0 = [z1], approx_grad = True, stepmx = 0.0001, bounds = [(z1 - 20, z1 + 20)])
    return output

def optimiseBiconvexDispersive(wavelengths, curvature1 = 0.02, curvature2 = -0.02):
    def minRMS(curvatures):
        rms2 = []
        for i in wavelengths:
            achromaticLens = lens.Lens(lens = "BICONVEX", z1 = 200, wavelength = i, curvature1 = curvatures[0], curvature2 = curvatures[1])
            print(achromaticLens.getParaxial([-5.0, 0, 5.0]))
            rms2.append((achromaticLens.getRMS(radius = 5.0))**2)
        print(curvatures)
        rms_new = np.sqrt(np.mean(rms2))
        print(rms_new)
        return rms_new
    output = fmin_tnc(func = minRMS, x0 = [curvature1, curvature2], approx_grad = True, stepmx = 0.0001, bounds = [(0.02, 0.09), (-0.09, -1E-8)])
    return output

def optimiseAchrom(wavelengths, curvature1 = 0.02, curvature2 = -0.02, curvature3 = 0.02):
    def minRMS(curvatures):
        rms2 = []
        for i in wavelengths:
            achromaticLens = lens.Lens(lens = "ACHROMATIC", z1 = 200, wavelength = i, curvature1 = curvatures[0], curvature2 = curvatures[1], curvature3 = curvatures[2])
            rms2.append((achromaticLens.getRMS(radius = 5.0))**2)
        rms_new = np.sqrt(np.mean(rms2))
        return rms_new
    output = fmin_tnc(func = minRMS, x0 = [curvature1, curvature2, curvature3], approx_grad = True, stepmx = 0.0001, bounds = [(0.02, 0.09), (-0.09, -1E-8), (-0.09, 0.09)])
    return output

def optimiseApochrom(wavelengths, curvature1 = 0.02, curvature2 = -0.02, curvature3 = 0.02, curvature4 = 0.02):
    def minRMS(curvatures):
        rms2 = []
        for i in wavelengths:
            apochromaticLens = lens.Lens(lens = "APOCHROMATIC", z1 = 200, wavelength = i, curvature1 = curvatures[0], curvature2 = curvatures[1], curvature3 = curvatures[2], curvature4 = curvatures[3])
            rms2.append((apochromaticLens.getRMS(radius = 5.0))**2)
        rms_new = np.sqrt(np.mean(rms2))
        return rms_new
    output = fmin_tnc(func = minRMS, x0 = [curvature1, curvature2, curvature3, curvature4], approx_grad = True, stepmx = 0.0001, bounds = [(0.001, 0.09), (-0.09, -0.001), (-0.09, 0.09), (-0.09, 0.09)])
    return output