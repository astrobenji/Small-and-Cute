'''
Quick little script to make a plot showing how I expect the time to fit a
geostatistical model to extend as a function of the size of the data.

Created by: Benjamin Metha
Last Updated: Feb 24, 2025
'''
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

N_spaxels  = np.array([9673, 9437, 8735, 7589, 4121, 12203, 15255, 16230, 20410])
sec_per_it = np.array([1800, 1500, 1440, 1070,  210, 4400,   7900,  9000, 13400])

min_per_it   = sec_per_it/60
day_per_loop = sec_per_it/60/60/24 * 480 

# Make a line of best fit between the log properties and plot it.
log_N = np.log(N_spaxels)
log_t = np.log(min_per_it)

result = linregress(log_N, log_t)

# log(y) = m log(x) + c
m = result.slope
c = result.intercept

# Conversion for power law:
# y = A x^b
A = np.exp(c)
b = m

# Make a plot with two axes; min/its and day_per_loop vs N_Spaxels

fig, ax = plt.subplots(figsize=(6,3.5))
plt.plot(N_spaxels, min_per_it, markersize=8, color='darkviolet', markeredgecolor='grey', marker='o', linestyle='')

# Add a trend line
x_range = np.logspace(3, 5.5)
pred_time = A * (x_range**b)

plt.plot(x_range, pred_time, color='black', linestyle = '--')

# Add the second axis
total_time_ax = ax.twinx()
total_time_ax.plot(N_spaxels, day_per_loop, linestyle='', zorder=1)

# Do formatting
plt.sca(total_time_ax)
plt.ylabel('Total time (days)', fontsize=12)
plt.yscale('log')

# Other formatting
plt.sca(ax)
plt.xlabel('Number of spaxels', fontsize=12)
plt.ylabel("Time per loop (minutes)", fontsize=12)
plt.xscale('log')
plt.yscale('log')

plt.tight_layout()
plt.show()