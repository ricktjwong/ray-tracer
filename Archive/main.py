# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 14:09:47 2017

@author: rtw16
"""

import lenses as lens
import numpy as np
import refractive_index as ri
import optimise_lens as oplens
from scipy.optimize import fmin_tnc

x_values = np.linspace(-0.5, 0.5, 30)
#wavelengths = np.linspace(380*1E-9, 699*1E-9, 200)
wavelengths = [486.1*1E-9, 656.3*1E-9]
#wavelengths = [486.1*1E-9, 589.3*1E-9, 656.3*1E-9]
colours = [ri.wavelengthToRGB(i*1e9) for i in wavelengths]
#vec = [-0.358367, 0, 0.93358]
vec = [0.0, 0.0, 1.0]

""" CONVEX PLANO """

#convexPlano = lens.Lens(curvature1 = 0.01995765, z1 = 198.45278442247201, lens = "CONVEXPLANO")
#vertices = convexPlano.genPlot(x_values, vec)
#print(convexPlano.getParaxial())
#print(convexPlano.genSpot())
#print(convexPlano.getRMS(radius = 5.0))

#print(oplens.findCOLC("CONVEXPLANO", curvature =  0.01995765))
# Before: 198.45281342722038, 0.00835606914552
# After: 198.24715235, 0.00275128327853

""" PLANO CONVEX """

#planoConvex = lens.Lens(curvature1 = -0.02, z1 = 201.74922600618754, lens = "PLANOCONVEX")
#vertices = planoConvex.genPlot(x_values, vec)
#print(planoConvex.getParaxial())
#print(planoConvex.genSpot())

#print(oplens.findCOLC("PLANOCONVEX", curvature = -0.02, z1 = 201.74922600618754))
# Before: 201.74922600619195, 0.0332918435432
# After: 200.93247322, 0.0109530374221

""" BICONVEX """

#biConvex = lens.Lens(lens = "BICONVEX", z1 = 152.5362269967614, curvature1 = 0.02, curvature2 = -0.02)
#vertices = biConvex.genPlot(x_values, vec)
#print(biConvex.getParaxial())
#print(biConvex.genSpot())

#print(oplens.findCOLC("BICONVEX", z1 = 152.5362269967614))
# Before: 152.5362269967645, 0.0465926663529
# After: 151.95751599, 0.0153633721648

""" Dispersive BICONVEX """

#x_value = [-5.0, 0, 5.0]
#
#rms2 = []
#for i, j in zip(wavelengths, colours):
#    biConvex = lens.Lens(lens = "BICONVEX", z1 = 200, wavelength = i, curvature1 =  2.00000000e-02, curvature2 = -1.00000076e-08)
#    vertices = biConvex.genPlot(x_value, vec, j)
#    print(biConvex.getParaxial([-5.0, 0, 5.0]))
#    print(biConvex.genSpot(j, radius = 5.0))
#    rms2.append((biConvex.getRMS(radius = 5.0))**2)
#rms_new = np.sqrt(np.mean(rms2))
#print(rms_new)

#oplens.findCOLCWavelength("BICONVEX", z1 = 199.34570794, curvature1 = 0.02, curvature2 = -1.00000076e-08, wavelengths = wavelengths)

#print(oplens.optimiseBiconvex(wavelengths))

""" MIRROR """    

#mirror = lens.Lens(lens = "MIRROR", z1 = 75.000000000000014, curvature1 = -0.02)
#vertices = mirror.genPlot(x_values, vec)
#print(mirror.getParaxial())
#print(mirror.genSpot())

#print(oplens.findCOLC("MIRROR", z1 = 75.000000000000014, curvature = -0.02))
# Before: 75.000000000000014, 0.0145869882892
# After: 75.09206299, 0.00479635918572

""" ACHROMATIC ABERRATION """

""" ACHROMATIC DOUBLET """

#x_value = [-5.0, 0, 5.0]
#rms2 = []
#
#for i, j in zip(wavelengths, colours):
#    achromaticLens = lens.Lens(lens = "ACHROMATIC", z1 = 200, wavelength = i, curvature1 = 0.02035545, curvature2 = -0.0181481, curvature3 = -0.00603903)
#    vertices = achromaticLens.genPlot(x_value, vec, j)
#    print(achromaticLens.getParaxial([-5.0, 0, 5.0]))
#    print(achromaticLens.genSpot(j, radius = 5.0))
#    rms2.append((achromaticLens.getRMS(radius = 5.0))**2)
#rms_new = np.sqrt(np.mean(rms2))
#print(rms_new)

#print(oplens.optimiseAchrom(wavelengths))
    
""" APOCHROMATIC TRIPLET """

#x_value = [-5.0, 0, 5.0]
#
#rms2 = []
#for i, j in zip(wavelengths, colours):
#    apochromaticLens = lens.Lens(lens = "APOCHROMATIC", z1 = 200, wavelength = i, curvature1 = 0.02167312, curvature2 = -0.01374189, curvature3 = -0.00124032, curvature4 = -0.00540239)
#    vertices = apochromaticLens.genPlot(x_value, vec, j)
#    print(apochromaticLens.getParaxial([-5.0, 0, 5.0]))
#    print(apochromaticLens.genSpot(j, radius = 5.0))
#    rms2.append((apochromaticLens.getRMS(radius = 5.0))**2)
#rms_new = np.sqrt(np.mean(rms2))
#print(rms_new)

#print(oplens.optimiseApochrom(wavelengths))
    
""" WATER SPHERE """

#sphericalWater = lens.Lens(lens = "WATERSPHERE", z1 = 300)
#vertices = sphericalWater.genPlot(x_value, vec)

#COLOUR
#x_value = np.linspace(5, 9, 10)
#for i, j in zip(wavelengths, colours):
#    sphericalWater = lens.Lens(lens = "WATERSPHERE", z1 = 300, wavelength = i, curvature1 = 0.1, curvature2 = -0.1)
#    vertices = sphericalWater.genPlotWithLens(x_value, vec, j)

#for i in wavelengths:
#    sphericalWater = lens.Lens(lens = "WATERSPHERE", z1 = 300, wavelength = i)
#    vertices = sphericalWater.genPlotWithLens(x_value, vec)

#sphericalWater = lens.Lens(lens = "WATERSPHERE", z1 = 300, curvature1 = 0.1, curvature2 = -0.1)
##vertices = sphericalWater.genPlot(x_value, vec)
#vertices = sphericalWater.genPlotWithLens(x_value, vec)

curvatures = oplens.optimiseCurvature("BICONVEX")[0]
#print(curvatures)
#c1, c2 = curvatures[0], curvatures[1]
##c1, c2 = 0.0174, -0.00260 
#CSF = (1/c2 + 1/c1)/(1/c2 - 1/c1)
#print(CSF)
#actualC = 2*(1.5168**2-1)/(1.5168+2)
#print(actualC)
    
#Longitudinal aberration = 0.3623221645363799, 0.1913045393927746
    
#biConvex = lens.Lens(lens = "BICONVEX", z1 = 152.5362269967614, curvature1 = 0.03317745, curvature2 = -0.00523252)
#print(biConvex.getParaxial())
#print(biConvex.genSpot())

#curvature = oplens.optimisePlano()[0]

#curvature = oplens.optimiseCurvature(lenstype = "PLANOCONVEX", z1 = 198.45278442247201)[0]
#print(curvature)

#convexPlano = lens.Lens(lens = "CONVEXPLANO", z1 = 198.45278442247201, curvature1 = 0.01995766)
#print(convexPlano.getParaxial())
#print(convexPlano.genSpot())

#planoConvex = lens.Lens(lens = "PLANOCONVEX", z1 = 198.45278442247201, curvature1 = -0.02052101)
#print(planoConvex.getParaxial())
#print(planoConvex.genSpot())
