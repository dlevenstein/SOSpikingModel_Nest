import nest
import numpy
import random

I_e = 400.0

dict_parameters = {"E_L": -70.0, "C_m": 250.0, "tau_m": 20.0, "t_ref": 2.0, "V_th": -55.0, "V_reset": -70.0, "tau_syn":  2.0, "I_e": I_e}

neurons = nest.Create("iaf_neuron", 10)

nest.SetStatus(neurons, params=dict_parameters)

neuronal_network_0 = []
neuronal_network_1 = []

for n_0 in neurons[0:4]:
    neuronal_network_0.append(n_0)

for n_1 in neurons[5:9]:
    neuronal_network_1.append(n_1)

neuronal_network_0 = numpy.asarray(neuronal_network_0)
neuronal_network_1 = numpy.asarray(neuronal_network_1)

for neuron_0 in neuronal_network_0:

    for neuron_1 in neuronal_network_1:

        nest.Connect(neuron_0, neuron_1, "one_to_one", syn_spec={"delay": 1.0, "weight": 70.0})

print(neuronal_network_0, neuronal_network_1)
