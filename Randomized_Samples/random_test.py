import nest
import randomized_functions
import pylab

neurons = randomized_functions.neuron_population([500], 50, 0, 70, 100, 1000, distribution=False)

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
