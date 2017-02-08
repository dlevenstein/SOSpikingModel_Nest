import nest
import simulation_functions
import pylab
import matplotlib.pyplot as plt
import numpy

mean_rate = []

nest.SetKernelStatus({"local_num_threads":8})

for J in range(0,110,10):

    line = []

    for N in range(0,510,10):

        nest.SetKernelStatus({"local_num_threads":8})

        neurons = simulation_functions.neuron_population([350], J, 0, 0, N, 500, distribution=False)
        line.append(neurons[4])

        nest.ResetKernel()

    mean_rate.append(line)

data = numpy.asarray(mean_rate)

numpy.savetxt("Noise_Data.csv", data, delimiter=',')

plt.figure("Mean Spike Rate")
heatmap = plt.imshow(data, cmap='plasma', interpolation='nearest', aspect='auto')
#plt.xticks(range(0,60,10),range(0,600,100))
#plt.yticks(range(0,60,10),range(0,600,100))
plt.xlabel("External Current: I (pA)")
plt.ylabel("Noise (pA)")
cbr = plt.colorbar(heatmap)
cbr.set_label("Neuron Spikes per sec")
plt.title("Mean Spike Rate, External Current Decrease")
#plt.gca().invert_xaxis()
#plt.gca().invert_yaxis()
plt.savefig("noise_figure.png")

plt.rcParams.update({'font.size': 30})

plt.show()
