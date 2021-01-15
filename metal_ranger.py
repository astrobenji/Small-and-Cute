'''
metal_ranger.py

You give me a redshift, and I'll tell you the ranges of wavelengths you need 
to be able to cover in order to find its metallicity, using several common
diagnostics.

Created by: Benjamin Metha
Last Updated: Jan 15, 2021
'''

import numpy as np

# These diagnostics are taken from:
# Wavelengths reported in microns.
diags = {'R23': np.array([0.3727, 0.4861, 0.4959, 0.5007]),
         'N2O2': np.array([0.3727, 0.5007]),
         'O3N2': np.array([0.4861, 0.5007, 0.6584, 0.6563])}

if __name__=="__main__":
    z = float(input("Input redshift: "))
    print("At z={0}, Hb={1:.5f} microns\n".format(z, 0.4861*(1+z)))
    for diag in diags.keys():
        waves = diags[diag]*(1+z)
        print("Wavelength range for {0} diagnostic:".format(diag))
        print('\t', waves, '\n')