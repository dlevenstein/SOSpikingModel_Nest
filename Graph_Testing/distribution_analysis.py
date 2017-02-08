import nest
import simulation_functions
import pylab
import matplotlib.pyplot as plt
import numpy
import simplejson

times = []

nest.SetKernelStatus({"local_num_threads":8})

for J_mean in range(0,110,10):

    time_mean = []

    for J_sigma in range(0,55,5):

        neurons = simulation_functions.neuron_population([500], J_mean, J_sigma, 70, 100, 500, distribution=True)
        time_sigma = []

        for t in range(1, len(neurons[0])):
            time_gap = numpy.subtract(neurons[0][t],neurons[0][t-1])
            time_sigma.append(time_gap)

        time_mean.append(time_sigma)

    times.append(time_mean)

#times = numpy.asarray(times)

open_file = open("distribution_data.json", "w")
simplejson.dump(times, open_file)
open_file.close()

#numpy.savetxt("distribution_data.csv", times, delimiter=',')
