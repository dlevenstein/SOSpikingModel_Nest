import neuron_functions
import nest
import numpy
import matplotlib.pyplot as plt
import pylab

times_UP = []
times_DOWN = []

for J in range(0,20,10):
    for N in [250]:

        spike_data_UP = []
        volt_data_UP = []

        spike_data_DOWN = []
        volt_data_DOWN = []

        nest.SetKernelStatus({"local_num_threads":8})

        data_DOWN = neuron_functions.neuron_population(range(0,510,10), J, 0, N, 500)
        data_UP = neuron_functions.neuron_population(range(500,-10,-10), J, 0, N, 500)

        """pylab.figure("External_Increase_J: " + str(J) + ", N: " + str(N) + "_Raster Plot")
        pylab.plot(data_UP[0], data_UP[1], "b.")
        pylab.xlabel("Time: ms")
        #pylab.xlim(0,1000)
        pylab.ylabel("Neuron ID")
        pylab.title("Noise at " + str(N) + " Raster Plot")
        pylab.rcParams.update({'font.size': 30})
        #pylab.savefig("External_Increase_J:_" + str(J) + "_N:_" + str(N) + "_Raster_Plot.png")


        pylab.figure()
        pylab.plot(data_DOWN[0], data_DOWN[1], "b.")
        pylab.xlabel("Time: ms")
        #pylab.xlim(0,1000)
        pylab.ylabel("Neuron ID")
        pylab.title("Noise at " + str(N) + " Raster Plot")
        pylab.rcParams.update({'font.size': 30})


        pylab.figure("External_Increase_J: " + str(J) + ", N: " + str(N) + "_Volt Plot")
        pylab.plot(data[2], data[3], "b")
        pylab.xlabel("Time: ms")
        #pylab.xlim(0,1000)

        pylab.ylabel("Neuron ID")
        pylab.title("Noise at " + str(N) + " Membrane Potential Plot")
        pylab.savefig("External_Increase_J:_" + str(J) + "_N:_" + str(N) + "_Volt_Plot.png")
        pylab.rcParams.update({'font.size': 30})"""

        times_DOWN.append(data_DOWN[0])
        times_UP.append(data_UP[0])

        #ts_s = ts_s.tolist()

        #data_DOWN[0].tolist()
        #data_DOWN[1].tolist()
        #data_DOWN[2].tolist()
        #data_DOWN[3].tolist()

        #data_UP[0].tolist()
        #data_UP[1].tolist()
        #data_UP[2].tolist()
        #data_UP[3].tolist()

        #spike_data_UP.append(data_UP[0])
        #spike_data_UP.append(data_UP[1])
        #volt_data_UP.append(data_UP[2])
        #volt_data_UP.append(data_UP[3])

        #spike_data_DOWN.append(data_DOWN[0])
        #spike_data_DOWN.append(data_DOWN[1])
        #volt_data_DOWN.append(data_DOWN[2])
        #volt_data_DOWN.append(data_DOWN[3])

        #numpy.savetxt("Membrane_Potential_Increase_External_J:_" + str(J) + "_N:_" + str(N) + "_simulated_noise_data.csv", volt_data_UP, delimiter=",")
        #numpy.savetxt("Spike_Raster_Increase_External_J:_" + str(J) + "_N:_" + str(N) + "_simulated_noise_data.csv", spike_data_UP, delimiter=",")

        #numpy.savetxt("Membrane_Potential_Decrease_External_J:_" + str(J) + "_N:_" + str(N) + "_simulated_noise_data.csv", volt_data_DOWN, delimiter=",")
        #numpy.savetxt("Spike_Raster_Decrease_External_J:_" + str(J) + "_N:_" + str(N) + "_simulated_noise_data.csv", spike_data_DOWN, delimiter=",")

        nest.ResetKernel()

#times = numpy.asarray(times)

#print(times)
numpy.savetxt("simulated_noise_data_UP.csv", times_UP, delimiter=",")
numpy.savetxt("simulated_noise_data_DOWN.csv", times_DOWN, delimiter=",")


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
