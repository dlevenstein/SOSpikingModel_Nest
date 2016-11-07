import nest
import numpy as np
import pylab

neurons = nest.Create("aeif_cond_exp", 1000)

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
, "a" : 1.0
, "b" : 80.5
, "V_th" : -55.0
, "tau_syn_ex" : 0.2
, "tau_syn_in" : 2.0
, "I_e" : 500.0
, "w": 0.0}

nest.SetStatus(neurons, params=dict_params)

for neuron in neurons:
    nest.SetStatus([neuron], {"V_m": dict_params["E_L"]+(dict_params["V_th"]-dict_params["E_L"])*np.random.rand()})

voltmeter = nest.Create("voltmeter")
spike_detector = nest.Create("spike_detector")

nest.Connect(voltmeter, [neurons[0]])

for neuron in neurons:
    nest.Connect([neuron], spike_detector)

K = 20
d = 1.0
J = 50.0

conn_dict = {"rule": "fixed_indegree", "indegree": K}
syn_dict = {"delay": d, "weight": J}

nest.Connect(neurons, neurons, conn_dict, syn_dict)

nest.Simulate(1000.0)

dmm = nest.GetStatus(voltmeter)[0]
Vms = dmm["events"]["V_m"]
ts = dmm["events"]["times"]

dSD = nest.GetStatus(spike_detector, keys='events')[0]
evs = dSD["senders"]
ts_sp = dSD["times"]



pylab.figure("Membrane Potential")
pylab.plot(ts, Vms)

pylab.figure("Spikes")
pylab.plot(ts_sp, evs, "b.")
pylab.show()
