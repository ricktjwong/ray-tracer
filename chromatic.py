"""
Module to run plots and optimisation functions for chromatic rays
Biconvex, achromatic, apochromatic lens and water sphere for rainbow generation
"""

import lenses as lens
import numpy as np
import refractive_index as ri
import optimise_lens as oplens

""" Dispersive BICONVEX """

def runBiconvexChrom(x_values, vec, wavelengths):
    colours = [ri.wavelengthToRGB(i*1e9) for i in wavelengths]
    for i, j in zip(wavelengths, colours):
        biConvex = lens.Lens(lens = "BICONVEX", z1 = 200, wavelength = i, curvature1 =  0.02, curvature2 = -0.02)
        biConvex.genPlot(x_values, vec, j)
#    wavelengths = [380*1E-9, 699*1E-9]
#    optimal_z = oplens.findCOLCWavelength("BICONVEX", z1 = 199.34570794, curvature1 = 0.02, curvature2 = -1.00000076e-08, wavelengths = wavelengths)[0]
#    optimal_curvatures = (oplens.optimiseBiconvexDispersive(wavelengths))[0]

""" ACHROMATIC ABERRATION """

""" ACHROMATIC DOUBLET """

def runAchromatic(x_values, vec, wavelengths):
    colours = [ri.wavelengthToRGB(i*1e9) for i in wavelengths]    
    rms2 = []    
    paraxials = []
    for i, j in zip(wavelengths, colours):
        achromaticLens = lens.Lens(lens = "ACHROMATIC", z1 = 200, wavelength = i, curvature1 = 0.02035545, curvature2 = -0.0181481, curvature3 = -0.00603903)
        achromaticLens.genPlot(x_values, vec, j)
        paraxials.append(np.average(achromaticLens.getParaxial([-5.0, 0, 5.0])))
        achromaticLens.genPlotBundle(colour = j, radius = 5.0)
        rms2.append((achromaticLens.getRMS(radius = 5.0))**2)
    rms_new = np.sqrt(np.mean(rms2))
    optimal_curvatures = oplens.optimiseAchrom(wavelengths)[0]
    return (paraxials, rms_new, optimal_curvatures)
    
""" APOCHROMATIC TRIPLET """

def runApochromatic(x_values, vec, wavelengths):
    colours = [ri.wavelengthToRGB(i*1e9) for i in wavelengths]
    rms2 = []
    paraxials = []
    for i, j in zip(wavelengths, colours):
        apochromaticLens = lens.Lens(lens = "APOCHROMATIC", z1 = 200, wavelength = i, curvature1 = 0.02167312, curvature2 = -0.01374189, curvature3 = -0.00124032, curvature4 = -0.00540239)
        apochromaticLens.genPlot(x_values, vec, j)
        paraxials.append(np.average(apochromaticLens.getParaxial([-5.0, 0, 5.0])))
        apochromaticLens.genPlotBundle(colour = j, radius = 5.0)
        rms2.append((apochromaticLens.getRMS(radius = 5.0))**2)
    rms_new = np.sqrt(np.mean(rms2))
    optimal_curvatures = oplens.optimiseApochrom(wavelengths)[0]
    return (paraxials, rms_new, optimal_curvatures)
    
""" WATER SPHERE """

def runWatersphere(x_values, vec, wavelengths):
    all_angles = []
    colours = [ri.wavelengthToRGB(i*1e9) for i in wavelengths]
    for i, j in zip(wavelengths, colours):
        sphericalWater = lens.Lens(lens = "WATERSPHERE", z1 = 90, wavelength = i, curvature1 = 0.1, curvature2 = -0.1)
        all_angles += (sphericalWater.genPlotWithLens(x_values, vec, j))
    angle_dict = ri.splitAngles(26, 42.5, 15, all_angles)
    ri.plotHistogram(angle_dict)