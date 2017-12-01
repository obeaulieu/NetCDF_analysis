import netCDF4
import numpy as np
from matplotlib import pyplot

nc = netCDF4.Dataset('/home/olivia/Documents/SAFL_Data/Fluvial_2016_Time_Stamp/NetCDF_files/25mmhr/25mmhr_photos.nc', 'r')

"""
# area of channel visited during experiment
visited = np.sum(nc.variables['channel_map'], axis=2)
plt.show (visited)
"""

# reworking through time
a = nc.variables['channel_map'][:,:,0:200]
all_locs = np.cumsum(a, axis=2)
plt.ion()
plt.imshow(all_locs[:,:,199])
#plt.imshow(all_locs[:,:,0])
reworked = all_locs > 0
plt.imshow(reworked[:,:,199]) #shows everything that has been touched by water at somep point over the timestep
n_reworked = np.sum(reworked, axis=(0,1))
plt.figure(); plt.plot(n_reworked) #shows how many cells have been reworked over time

#fix axis, make x actual time
