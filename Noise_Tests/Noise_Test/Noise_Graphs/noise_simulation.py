import neuron_functions
import nest
import numpy
import matplotlib.pyplot as plt
import pylab
import simplejson


end_time_UP = []
end_time_DOWN = []

for J in range(0,110,10):

    N = 250

    nest.SetKernelStatus({"local_num_threads":8})

    spike_data_UP = []
    volt_data_UP = []

    spike_data_DOWN = []
    volt_data_DOWN = []

    data_DOWN = neuron_functions.neuron_population(range(0,510,10), J, 0, N, 500)
    data_UP = neuron_functions.neuron_population(range(500,-10,-10), J, 0, N, 500)

    end_time_UP.append(data_UP[0][-1])
    end_time_DOWN.append(data_DOWN[0][-1])

    count_UP = len(data_UP[0])
    count_DOWN = len(data_DOWN[0])



    nest.ResetKernel()

print(end_time_UP)
print(end_time_DOWN)
