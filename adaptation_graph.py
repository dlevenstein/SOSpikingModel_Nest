import nest
import pylab
import numpy

dict_params = {"V_peak" : 0.0
, "V_reset" : -70.0
, "t_ref" : 2.0
, "g_L" :  30.0
, "C_m" : 281.0
, "E_ex" : 0.0
, "E_in" : -85.0
, "E_L" : -70.0
, "Delta_T" : 2.0
, "tau_w" : 100.0
, "a" : 0.0
, "b" : 70.0
, "V_th" : -55.0
, "tau_syn_ex" : 0.2
, "tau_syn_in" : 2.0
, "I_e" : 400.0
, "w": 0.0}

neurons = nest.Create("aeif_cond_exp", 100)
noise = nest.Create("noise_generator")

nest.SetStatus(neurons, params=dict_params)

nest.SetStatus(noise, {"std": 100.0})

for neuron in neurons:
    nest.SetStatus([neuron], {"V_m": dict_params["E_L"]+(dict_params["V_th"]-dict_params["E_L"])*numpy.random.rand()})

spike_detector = nest.Create("spike_detector")
multimeter = nest.Create("multimeter", 1)

for n in neurons:
    nest.Connect([n], spike_detector)

nest.Connect(multimeter, [neurons[0]])
nest.Connect(noise, neurons)

K = 10
d = 1.0

conn_dict = {"rule": "fixed_indegree", "indegree": K}
syn_dict = {"delay": d, "weight": 70.0}

nest.Connect(neurons, neurons, conn_dict, syn_dict)

for neuron in neurons:
    nest.SetStatus([neuron], {"V_m": dict_params["E_L"]+(dict_params["V_th"]-dict_params["E_L"])*numpy.random.rand()})

nest.Simulate(1000.0)

dmm = nest.GetStatus(multimeter)[0]
Vms = dmm["events"]["w"]
ts = dmm["events"]["times"]

pylab.figure(1)
pylab.plot(ts, Vms)
pylab.show()
