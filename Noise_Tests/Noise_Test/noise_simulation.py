import neuron_functions
import nest
import numpy
import matplotlib.pyplot as plt
import pylab

times_UP = []
times_DOWN = []

full_data = []

for N in range(0,20,10):

    spike_data_UP = []
    volt_data_UP = []

    spike_data_DOWN = []
    volt_data_DOWN = []

    #nest.SetKernelStatus({"local_num_threads":8})
    #data_DOWN = neuron_functions.neuron_population(range(0,510,10), 100, 0, N, 500)
    #nest.ResetKernel()

    nest.SetKernelStatus({"local_num_threads":8})
    data_UP = neuron_functions.neuron_population(range(0,510,10), 70, 0, N, 500)
    nest.ResetKernel()

    pylab.figure(N)
    pylab.plot(data_UP[0], data_UP[1], "r.")

pylab.show()

""" line_data = []

    for t_interval in range(0,25500,500):

        spike_data_UP = data_UP[0]
        t_n = numpy.float64(t_interval)
        t_n_1 = numpy.add(numpy.float64(t_interval), numpy.float64(500))
        interval = spike_data_UP[(spike_data_UP > t_n) & (spike_data_UP <= t_n_1)]
        count = len(interval)
        average = numpy.multiply(numpy.divide(numpy.float64(count), numpy.float64(50000.0)), numpy.float64(1000))

        line_data.append(average)

    full_data.append(line_data)

matrix_data = numpy.asarray(full_data)

numpy.savetxt("noise_data.csv", matrix_data, delimiter=',')"""
