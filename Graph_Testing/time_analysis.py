import numpy
import matplotlib.pyplot as plt
import simulation_functions
import nest
import pylab

neurons = simulation_functions.neuron_population(range(0,510,10), 50, 0, 70, 0, 500, distribution=False)

"""pylab.figure()
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
pylab.ylabel("Membrane Potential")"""


time_list = []

for t in range(1,len(neurons[0])):

    time_gap = neurons[0][t] - neurons[0][t-1]
    time_list.append(time_gap)

time_list.sort()
time_list = numpy.asarray(time_list)
numpy.savetxt("times.csv", time_list, delimiter=',')
#mean = numpy.(time_list)

#time_list = time_list[(time_list >= mean)]

#print(mean)


n, bins, patches = plt.hist(time_list, 50, lw=3, fc=(0, 0, 0, 0.5))

#plt.xlabel("Time, ms")
#plt.ylabel("Number of DOWN states that last for t ms")

#plt.figure("DOWN_State, External Current: " + str(i) + " Internal Current: " + str(j))
#plt.title("State Analysis")

#pylab.show()

plt.show()
