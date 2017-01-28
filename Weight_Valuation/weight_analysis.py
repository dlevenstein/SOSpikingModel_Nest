import neuron_functions
import nest
import numpy
import matplotlib.pyplot as plt
import pylab


for N in [100]:
    times = []
    end_time_UP = []
    end_time_DOWN = []
    for J in range(0,110,10):

        nest.SetKernelStatus({"local_num_threads":8})

        #data_DOWN = neuron_functions.neuron_population(range(500,-10,-10), J, 0, N, 500, UP=False, DOWN=True)
        data_UP = neuron_functions.neuron_population(range(0,510,10), J, 0, N, 500, UP=True, DOWN=False)


        nest.ResetKernel()

        #print(ts_s)
        #times.append(data[0])
        end_time_UP.append(data_UP[1])
        #end_time_DOWN.append(data_DOWN[1])

        #numpy.append(times, ts_s, axis=0)

    #pylab.figure()
    #pylab.plot(end_time_UP, range(0,110,10), "r")
    #pylab.plot(end_time_DOWN, range(0,110,10), "b")
    #pylab.show()
    #times = numpy.asarray(times)
    #end_time = numpy.asarray(end_time)

    #print(times)
    #numpy.savetxt("Noise:_" + str(N) + "_weight_data_decrease.csv", times, delimiter=",")
    #numpy.savetxt("blue_line_data_w_noise.csv", end_time_DOWN, delimiter=",")
    numpy.savetxt("red_line_data_w_noise.csv", end_time_UP, delimiter=",")

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
