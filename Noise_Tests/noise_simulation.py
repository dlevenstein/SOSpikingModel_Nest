import neuron_functions
import nest
import numpy
import matplotlib.pyplot as plt
import pylab

times = []

for J in [10,50]:
    for N in [0,250,500]:
        spike_data = []
        volt_data = []

        nest.SetKernelStatus({"local_num_threads":8})

        data = neuron_functions.neuron_population(range(500,-10,-10), J, 0, N, 500)

        #pylab.figure("Increase_J: " + str(J) + ", N: " + str(N) + "Raster Plot")
        #pylab.plot(data[0], data[1], "b.")
        #pylab.xlabel("Time: ms")
        #pylab.ylabel("Neuron ID")
        #pylab.title("Increase_J: " + str(J) + ", N: " + str(N) + "Raster Plot")
        #pylab.savefig("Increase_J:_" + str(J) + "_N:_" + str(N) + "_Raster_Plot.png")
        #ts_s = ts_s.tolist()
        data[0].tolist()
        data[1].tolist()
        data[2].tolist()
        data[3].tolist()

        spike_data.append(data[0])
        spike_data.append(data[1])
        volt_data.append(data[2])
        volt_data.append(data[3])

        numpy.savetxt("Membrane_Potential_Decrease_External_J:_" + str(J) + "_N:_" + str(N) + "_simulated_noise_data.csv", volt_data, delimiter=",")
        numpy.savetxt("Spike_Raster_Decrease_External_J:_" + str(J) + "_N:_" + str(N) + "_simulated_noise_data.csv", spike_data, delimiter=",")
        nest.ResetKernel()

        #print(ts_s)
        #times.append(ts_s)
        #numpy.append(times, ts_s, axis=0)

#times = numpy.asarray(times)

#print(times)
#numpy.savetxt("simulated_noise_data.csv", times, delimiter=",")

"""plt.figure("Noise Analysis")
heatmap = plt.imshow(times, cmap='plasma', interpolation='nearest', aspect='auto')
plt.xticks(range(50,-10,-10),range(0,600,100))
plt.yticks(range(0,60,10),range(0,600,100))
plt.ylabel("External Current: I (pA)")
plt.xlabel("Noise: N (standard deviation: pA)")
cbr = plt.colorbar(heatmap)
cbr.set_label("Mean Spike Rate (Neurons Spiking per ms)")
plt.title("Noise Analysis")
plt.savefig("noise_analysis.png")


plt.show()"""
