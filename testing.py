import nest
import simplejson
import numpy
import pylab
import matplotlib.pyplot as plt

I = 500.0
J = 20.0

nest.SetKernelStatus({"local_num_threads":8})

spike_list = []
list_values = []

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
, "I_e" : 200.0
, "w": 0.0}

neurons = nest.Create("aeif_cond_exp", 100)
noise = nest.Create("poisson_generator")

nest.SetStatus(neurons, params=dict_params)

nest.SetStatus(noise, {"rate": 100.0})

for neuron in neurons:
    nest.SetStatus([neuron], {"V_m": dict_params["E_L"]+(dict_params["V_th"]-dict_params["E_L"])*numpy.random.rand()})

spike_detector = nest.Create("spike_detector")

for n in neurons:
    nest.Connect([n], spike_detector)

nest.Connect(noise, neurons)

K = 10
d = 1.0

conn_dict = {"rule": "fixed_indegree", "indegree": K}
syn_dict = {"delay": d, "weight": float(J)}

nest.Connect(neurons, neurons, conn_dict, syn_dict)

for neuron in neurons:
    nest.SetStatus([neuron], {"V_m": dict_params["E_L"]+(dict_params["V_th"]-dict_params["E_L"])*numpy.random.rand()})

nest.SetStatus(neurons, params={"I_e": float(I)})

nest.Simulate(5000.0)

dSD = nest.GetStatus(spike_detector, keys='events')[0]
evs = dSD["senders"]
ts_s = dSD["times"]

pylab.figure(str(I) + str(J))
pylab.plot(ts_s, evs, "b.")
pylab.show()
