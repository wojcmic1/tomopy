# -*- coding: utf-8 -*-
# Filename: main.py
""" Main program for tomographic reconstruction.
"""
#import tomoRecon.tomoRecon
from preprocessing.preprocess import Preprocess
from tomoRecon import tomoRecon
from visualize import image
from dataio.file_types import Tiff
import numpy as np

# Input HDF file.
#filename = '/local/data/databank/dataExchange/microCT/Blakely_ALS_2011.h5'
filename = '/local/data/databank/dataExchange/microCT/PetraIII_ct4_180.h5'

# Pre-process data.
mydata = Preprocess()
mydata.read_hdf5(filename, slices_start=1200, slices_end=1221)
mydata.normalize()
#mydata.remove_rings(level=12, wname='db10', sigma=2)
mydata.median_filter()
#mydata.optimize_center(center_init=2082)
#mydata.optimize_center()
#mydata.center = 1684
mydata.center = 2081.59
mydata.center = 2177.00
mydata.retrieve_phase(pixel_size=1.43e-6, dist=10, energy=35.4, delta_over_mu=1e-8)
mydata.data = np.exp(-mydata.data)


# Reconstruct data.
recon = tomoRecon.tomoRecon(mydata)
recon.run(mydata)

### Save data.
##f = Tiff()
##f.write(recon.data, file_name='/local/data/databank/PetraIII/ct4/rec_ct4_slice_1200_phase_.tiff')

# Visualize data.
image.show_slice(recon.data)
