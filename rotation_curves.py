import os

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from data_extract import extract_galaxy_data

data_path = "alldata"
datafiles = os.listdir(data_path)

plt.figure(figsize=(15, 10))

for datafile in datafiles:
    filepath = os.path.join(data_path, datafile)
    gdata = extract_galaxy_data(filepath)

    vel = [float(elem) for elem in gdata["data"]["V(km/s)"]]
    dist = [float(elem) for elem in gdata["data"]["R(kpc)"]]
    
    plt.plot(dist, vel)

plt.xlabel("Distance from center (kPc)")
plt.ylabel("Radial velocity (km/s)")
plt.title("Galactic Rotation Curves of 50 Galaxies")

plt.savefig("rotation_curves.png")
plt.show()

