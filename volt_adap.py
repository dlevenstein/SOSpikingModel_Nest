import nest
import numpy
import pylab

nest.SetKernelStatus({"local_num_threads":8})

Current_increase = []
Current_decrease = []

time_increase = ""
time_decrease = ""

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
, "b" : 0.0
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

voltmeter = nest.Create("voltmeter")

nest.Connect(voltmeter, [neurons[0]])
nest.Connect(noise, neurons)

K = 10
d = 1.0
J = 100.0

conn_dict = {"rule": "fixed_indegree", "indegree": K}
syn_dict = {"delay": d, "weight": J}

nest.Connect(neurons, neurons, conn_dict, syn_dict)

for neuron in neurons:
    nest.SetStatus([neuron], {"V_m": dict_params["E_L"]+(dict_params["V_th"]-dict_params["E_L"])*numpy.random.rand()})

for I in range(500,-10,-10):

    nest.SetStatus(neurons, params={"I_e": float(I)})

    nest.Simulate(100.0)

    nest.ResumeSimulation()

nest.Simulate(1000.0)

dmm = nest.GetStatus(voltmeter)[0]
Vms = dmm["events"]["V_m"]
ts = dmm["events"]["times"]

pylab.figure()
pylab.plot(ts, Vms)
pylab.xlim(5100, 6100)

pylab.show()
