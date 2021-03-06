import nest
import numpy as np
import pylab


nest.SetKernelStatus({"local_num_threads":8})

neuron_population = 100
simulation_time = 5000.0

dict_params = {"V_peak" : 0.0
, "V_reset" : -70.0
, "t_ref" : 2.0
, "g_L" : 1.0
, "C_m" : 250.0
, "E_ex" : 0.0
, "E_in" : 0.0
, "E_L" : -70.0
, "Delta_T" : 2.0
, "tau_w" : 1.0
, "a" : 0.0
, "b" : 70.0
, "V_th" : -55.0
#, "tau_syn_ex" : 0.2
, "tau_syn_in" : 2.0
, "I_e" : 500.0
, "w": 0.0}

neurons = nest.Create("aeif_cond_exp", neuron_population)

nest.SetStatus(neurons, params=dict_params)

for neuron in neurons:
    nest.SetStatus([neuron], {"V_m": dict_params["E_L"]+(dict_params["V_th"]-dict_params["E_L"])*np.random.rand()})

spikedetector = nest.Create("spike_detector", params={"withgid": True, "withtime": True})

for neuron in neurons:

    nest.Connect([neuron], spikedetector)

K = 10
d = 1.0
J = 70.0

conn_dict = {"rule": "fixed_indegree", "indegree": K}
syn_dict = {"delay": d, "weight": J}

nest.Connect(neurons, neurons, conn_dict, syn_dict)

length = np.float64(0)

for I in range(500, -10, -10):

    I_e = float(I)

    nest.SetStatus(neurons, params={"I_e": I_e})

    nest.Simulate(simulation_time)

    dSD = nest.GetStatus(spikedetector, keys='events')[0]
    evs = dSD["senders"]
    ts = dSD["times"]

    nest.ResumeSimulation()

pylab.figure("Spike Raster Decreasing I: " + str(I) + ", J: " + str(J))
pylab.title("Spike Raster Decreasing I: " + str(I) + ", J: " + str(J))
pylab.plot(ts, evs, "b.")
pylab.xlabel("Time: ms")
pylab.ylabel("Neuron ID")
pylab.savefig("Spike Raster Decreasing I: " + str(I) + ", J: " + str(J) + ".png")
plt.show()
