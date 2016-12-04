import simplejson

file_1 = open("spike_averages.json", "r")

spike_averages = simplejson.load(file_1)

import numpy as np

a = np.asarray(spike_averages)

np.savetxt("spike_averages.csv", a, delimiter=",")
