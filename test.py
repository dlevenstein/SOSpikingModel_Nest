import neuron_functions
import nest
import pylab
import numpy

nest.SetKernelStatus({"local_num_threads":8})

noise_data = []

for N in range(0,510,10):

    data = neuron_functions.neuron_population(380, 50, 0, N, 500)

    dSD = nest.GetStatus(data[0], keys='events')[0]
    evs = dSD["senders"]
    ts_s = dSD["times"]

    ts_s.tolist()

    noise_data.append(ts_s)

noise_data = numpy.asarray(noise_data)

numpy.savetxt("noise_data.csv", noise_data, delimiter=",")
