'''
metal_ranger.py

You give me a redshift, and I'll tell you the ranges of wavelengths you need 
to be able to cover in order to find its metallicity, using several common
diagnostics.

Created by: Benjamin Metha
Last Updated: Jan 15, 2021
'''

import numpy as np

diag_names      =          ['R23',  'N2O2',  'O3N2']
min_wavelengths = np.array([0.3727, 0.3727,  0.4861]) # in microns
max_wavelengths = np.array([0.5007, 0.6854,  0.6854])

if __name__=="__main__":
    z = float(input("Input redshift: "))
    min_wavelengths = min_wavelengths*(1+z)
    max_wavelengths = max_wavelengths*(1+z)
    print("At z={0}, Hb={1:.5f} microns\n".format(z, 0.4861*(1+z)))
    for ii, diag in enumerate(diag_names):
        print("Wavelength range for {0} diagnostic: {1:.5f}-{2:.5f} microns".format(diag, min_wavelengths[ii], max_wavelengths[ii]))
        