"""
Module to run plots and optimisation functions for monochromatic rays
Convex-plano, plano-convex, biconvex and spherical mirror
"""

import lenses as lens
import numpy as np
import optimise_lens as oplens

""" CONVEX PLANO """

def runConvexPlano(x_values, vec):
    convexPlano = lens.Lens(curvature1 = 0.02, z1 = 198.45281342722038, lens = "CONVEXPLANO")
    convexPlano.genPlot(x_values, vec)
    paraxial = np.average(convexPlano.getParaxial())
    rms = convexPlano.genPlotBundle()
    optimal_z = oplens.findCOLC("CONVEXPLANO", curvature1 =  0.02)[0]
    optimal_curvature = oplens.optimiseCurvature(lenstype = "CONVEXPLANO", z1 = 198.45278442247201)[0]
    return (paraxial, rms, optimal_z, optimal_curvature)

""" PLANO CONVEX """

def runPlanoConvex(x_values, vec):
    planoConvex = lens.Lens(curvature1 = -0.02, z1 = 201.74922600619198, lens = "PLANOCONVEX")
    planoConvex.genPlot(x_values, vec)
    paraxial = np.average(planoConvex.getParaxial())
    rms = planoConvex.genPlotBundle()
    optimal_z = oplens.findCOLC("PLANOCONVEX", curvature2 = -0.02, z1 = 201.74922600618754)[0]
    return (paraxial, rms, optimal_z)

""" BICONVEX """

def runBiconvex(x_values, vec):
    biConvex = lens.Lens(lens = "BICONVEX", z1 = 198.46246471, curvature1 = 0.01749563, curvature2 = -0.00263006)
    biConvex.genPlot(x_values, vec)
    paraxial = np.average(biConvex.getParaxial())
    rms = biConvex.genPlotBundle(vec = [0.0, 0.0, 1.0])
    
    optimal_z = oplens.findCOLC(lenstype = "BICONVEX", z1 = 198.45, curvature1 = 0.01749563, curvature2 = -0.00263006)[0]
    optimal_curvatures = oplens.optimiseCurvature(lenstype = "BICONVEX", z1 = 198.45278442247201, curvature1 = 0.02, curvature2 = -0.001)[0]
    c1, c2 = optimal_curvatures[0], optimal_curvatures[1]
    CSF = (1/c2 + 1/c1)/(1/c2 - 1/c1)
    actualCSF = 2*(1.5168**2-1)/(1.5168+2)
    return (paraxial, rms, optimal_z, optimal_curvatures, CSF, actualCSF)

""" MIRROR """    

def runMirror(x_values, vec):
    mirror = lens.Lens(lens = "MIRROR", z1 = 75.09206299, curvature1 = -0.02)
    mirror.genPlot(x_values, vec)
    paraxial = np.average(mirror.getParaxial())
    rms = mirror.genPlotBundle(z = 99)
    optimal_z = oplens.findCOLC("MIRROR", z1 = 75.000000000000014, curvature1 = -0.02)[0]
    return(paraxial, rms, optimal_z)