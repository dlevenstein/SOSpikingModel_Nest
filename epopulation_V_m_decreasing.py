import nest
import numpy as np
import pylab

nest.SetKernelStatus({"local_num_threads": 8})

neuron_population = 1000
simulation_time = 100.0

I_e = 0.0

mean_rate_Je = []
mean_rate_list = []

dict_parameters_exc = {"E_L": -70.0, "C_m": 250.0, "tau_m": 20.0, "t_ref": 2.0, "V_th": -55.0, "V_reset": -70.0, "tau_syn":  2.0, "I_e": I_e}

epop = nest.Create("iaf_neuron", neuron_population)

nest.SetStatus(epop, params=dict_parameters_exc)

Ke_list = []
I_e_list = []

multimeter_times = []
multimeter_V_m = []

for neuron in epop:
    nest.SetStatus([neuron], {"V_m": dict_parameters_exc["E_L"]+(dict_parameters_exc["V_th"]-dict_parameters_exc["E_L"])*np.random.rand()})

Je_parameters = np.arange(0,10,0.2)

Ke = 20
d = 1.0
Je = 10.0

conn_dict_ex = {"rule": "fixed_indegree", "indegree": Ke}
syn_dict_ex = {"delay": d, "weight": Je}

nest.Connect(epop, epop, conn_dict_ex, syn_dict_ex)

spikedetector_exc = nest.Create("spike_detector", params={"withgid": True, "withtime": True})

multimeter = nest.Create("multimeter")

nest.SetStatus(multimeter, {"withtime":True, "record_from":["V_m"]})

nest.Connect(multimeter, [epop[0]])

for neuron_exc in epop:
    nest.Connect([neuron_exc], spikedetector_exc)

multimeter_values = []

for i in range(500,0,-10):

    VM_values = []
    TS_values = []

    I_e = float(i)

    nest.SetStatus(epop, params={"I_e": I_e})

    nest.Simulate(simulation_time)

    nest.ResumeSimulation()

dmm = nest.GetStatus(multimeter)[0]
Vms = dmm["events"]["V_m"]
ts = dmm["events"]["times"]

print(Vms)
print(ts)

multimeter_values.append(Vms)
multimeter_values.append(ts)

a = np.asarray(multimeter_values)
print(a)
np.savetxt("I_e_Je_multimeter.csv", a, delimiter=",")
pylab.figure()
pylab.plot(ts, Vms)
pylab.show()
