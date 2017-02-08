import neuron_functions
import nest
import numpy
import matplotlib.pyplot as plt
import pylab
import threading

noise_UP = []
noise_DOWN = []

for J in [0,10,50,100]:

    threads = []

    for N in range(0,600,100):

        nest.SetKernelStatus({"local_num_threads":8})

        #data_DOWN = neuron_functions.neuron_population(range(500,-10,-10), J, 0, N, 500, DOWN=True)
        #nest.ResetKernel()
        t = threading.Thread(target=neuron_functions.neuron_population, args=(range(0,510,10), J, 0, N, 500, UP=True))
        #threading.thread(neuron_functions.neuron_population(range(0,510,10), J, 0, N, 500, UP=True), target = )
        data_UP = neuron_functions.neuron_population(range(0,510,10), J, 0, N, 500, UP=True)
        #nest.ResetKernel()

        noise_UP.append(data_UP[0])
        #noise_DOWN.append(data_DOWN[0])
        threads.append(t)
        t.start()
    t.join()

times = numpy.asarray(noise_UP)

plt.figure("Noise Analysis")
heatmap = plt.imshow(times, cmap='plasma', interpolation='nearest', aspect='auto')
#plt.xticks(range(50,-10,-10),range(0,600,100))
#plt.yticks(range(0,60,10),range(0,600,100))
plt.ylabel("Weight")
plt.xlabel("Noise: N (standard deviation: pA)")
cbr = plt.colorbar(heatmap)
cbr.set_label("Mean Spike Rate (Neurons Spiking per ms)")
plt.title("Noise Analysis")
plt.savefig("noise_analysis.png")

plt.show()
