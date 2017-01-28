import nest
import pylab
import numpy as np

neuron_population = nest.Create("iaf_neuron", 1000)

nest.SetStatus(neuron_population, params={"E_L": -70.0, "C_m": 250.0, "tau_m": 20.0, "t_ref": 2.0, "V_th": -55.0, "V_reset": -70.0, "tau_syn":  2.0, "I_e": 0.0})

voltmeter = nest.Create("voltmeter")

for neuron in neuron_population:
    nest.SetStatus([neuron], {"V_m": -70.0+(-55.0-(-70.0))*np.random.rand()})

K = 20
d = 1.0
J = 10.0

conn_dict = {"rule": "fixed_indegree", "indegree": K}
syn_dict = {"delay": d, "weight": J}

nest.Connect(neuron_population, neuron_population, conn_dict, syn_dict)

nest.Connect(voltmeter, [neuron_population[0]])

for i in [500, 0]:

    nest.SetStatus(neuron_population, params={"I_e":float(i)})
    nest.Simulate(10.0)
    nest.ResumeSimulation

dmm = nest.GetStatus(voltmeter)[0]
Vms = dmm["events"]["V_m"]
ts = dmm["events"]["times"]

pylab.figure()
pylab.plot(Vms)
pylab.show()
