import nest
import numpy as np
import simplejson
from sys import argv
import pylab

nest.SetKernelStatus({"local_num_threads": 8})

neuron_population = 1000
simulation_time = 1.0

I_e = 0.0

dict_parameters_1 = {"E_L": -70.0, "C_m": 250.0, "tau_m": 20.0, "t_ref": 2.0, "V_th": -55.0, "V_reset": -70.0, "tau_syn":  2.0, "I_e": I_e}

epop_1 = nest.Create("iaf_neuron", neuron_population)

nest.SetStatus(epop_1, params=dict_parameters_1)

for neuron in epop_1:
    nest.SetStatus([neuron], {"V_m": dict_parameters_1["E_L"]+(dict_parameters_1["V_th"]-dict_parameters_1["E_L"])*np.random.rand()})

Ke = 20
d = 1.0
Je = 5.0

conn_dict_1 = {"rule": "fixed_indegree", "indegree": Ke}
syn_dict_1 = {"delay": d, "weight": Je}

nest.Connect(epop_1, epop_1, conn_dict_1, syn_dict_1)

spikedetector_1 = nest.Create("spike_detector", params={"withgid": True, "withtime": True})

multimeter_exc = nest.Create("multimeter")
nest.SetStatus(multimeter_exc, {"withtime":True, "record_from":["V_m"]})

for neuron_1 in epop_1:
    nest.Connect([neuron_1], spikedetector_1)

nest.Connect(multimeter_exc, [epop_1[0]])

length = 0

for i in range(10000):

    I_e = 250.0

    nest.SetStatus(epop_1, params={"I_e": I_e})

    nest.Simulate(simulation_time)

    dSD = nest.GetStatus(spikedetector_1, keys='events')[0]
    evs_1 = dSD["senders"]
    ts_1 = dSD["times"]

    V_thresh = -55.0

    if len(evs_1) >= neuron_population:

        length -= neuron_population

        V_thresh += 10.0

        nest.SetStatus(epop_1, params={"V_th": V_thresh})

    length = len(evs_1)

    nest.ResumeSimulation()

pylab.figure("1")
pylab.plot(ts_1, evs_1, "r.")

pylab.show()
