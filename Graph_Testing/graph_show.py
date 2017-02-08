import nest
import simulation_functions
import pylab
import matplotlib.pyplot as plt
import numpy

mean_rate = []

nest.SetKernelStatus({"local_num_threads":8})

#for N in range(0,200,100):

neurons = simulation_functions.neuron_population(range(0,510,10), 50, 0, 70, 10, 500, distribution=False)
nest.ResetKernel()

mean_rate.append(neurons[4])

pylab.figure()
pylab.subplot2grid((3,3),(0,0), colspan=3)
pylab.plot(neurons[0], neurons[1], "r.")
pylab.gca().invert_xaxis()
pylab.title("Raster Plot")
pylab.xlabel("Time ms")
pylab.ylabel("Neuron label")

pylab.subplot2grid((3,3),(1,0), colspan=3)
pylab.plot(neurons[2], neurons[3], "b")
pylab.title("Membrane Potential")
pylab.xlabel("Time ms")
pylab.ylabel("Membrane Potential")

pylab.show()
