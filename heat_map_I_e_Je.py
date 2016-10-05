import nest
import numpy as np
import simplejson
from sys import argv
from nest import raster_plot
import matplotlib.pyplot as plt
import pylab
nest.SetKernelStatus({"local_num_threads": 8})

neuron_population = 100
simulation_time = 100.0

I_e = 0.0

open_file = open("heat_map_values_I_e_Je.json", "r")
mean_rate_list = simplejson.load(open_file)

mean_rate_Je = []

Je_parameters = np.arange(0,10,0.2)
dict_parameters_exc = {"E_L": -70.0, "C_m": 250.0, "tau_m": 20.0, "t_ref": 2.0, "V_th": -55.0, "V_reset": -70.0, "tau_syn":  2.0, "I_e": I_e}

epop = nest.Create("iaf_neuron", neuron_population)
for neuron in epop:
    nest.SetStatus([neuron], {"V_m": dict_parameters_exc["E_L"]+(dict_parameters_exc["V_th"]-dict_parameters_exc["E_L"])*np.random.rand()})

start = int(argv[1])
end = int(argv[2])

pylab.figure()

number = 1

for i in Je_parameters:

    d = 1.0
    Je = 0.0
    Ke = 20

    conn_dict_ex = {"rule": "fixed_indegree", "indegree": Ke}
    syn_dict_ex = {"delay": d, "weight": Je}

    nest.Connect(epop, epop, conn_dict_ex, syn_dict_ex)

    spikedetector_exc = nest.Create("spike_detector", params={"withgid": True, "withtime": True})

    for neuron_exc in epop:
        nest.Connect([neuron_exc], spikedetector_exc)
    

    for j in range(start, end,-10):
        number += 1
        I_e = float(j)

        nest.SetStatus(epop, {"I_e": I_e})

        nest.Simulate(simulation_time)

        dSD = nest.GetStatus(spikedetector_exc, keys='events')[0]
        evs = dSD["senders"]
        ts = dSD["times"]

        total = 0.0

        for i in range(len(evs)):

            total += evs[i]

        mean_rate = total / (neuron_population * simulation_time)

        nest.ResumeSimulation()

        mean_rate_Je.append(mean_rate)
        
        pylab.plot(number, I_e, ".")

    pylab.figure()
    pylab.plot(ts, evs, ".")
    pylab.ylabel("Neuron Number")
    pylab.xlabel("Time: ms")

    pylab.show()
        
    mean_rate_list.append(mean_rate_Je)
    open_file = open("heat_map_values_I_e_Je.json", "w")
    simplejson.dump(mean_rate_list, open_file)
    open_file.close()
    mean_rate_Je = []
    break
