import neuron_functions
import nest
import numpy

for I in range(0,1010,10):
    nest.SetKernelStatus({"local_num_threads":8})
    data = neuron_functions.neuron_population([I], 50, 0, 100, 5000)
    numpy.savetxt('Adaptation_' + str(0) + '_External_' + str(I) + '.csv', data, delimiter=',')
    nest.ResetKernel()
