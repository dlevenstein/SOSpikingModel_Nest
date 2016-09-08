import nest
import pylab
import numpy

ndict = {"I_e": 200.0, "tau_m": 20.0}
nest.SetDefaults("iaf_neuron", ndict)

neuronpop1 = nest.Create("iaf_neuron", 100)
neuronpop2 = nest.Create("iaf_neuron", 100)

Vth=-55.
Vrest=-70.
for neuron in neuronpop1:
    nest.SetStatus([neuron], {"V_m": Vrest+(Vth-Vrest)*numpy.random.rand()})

for neuron in neuronpop2:
    nest.SetStatus([neuron], {"V_m": Vrest+(Vth-Vrest)*numpy.random.rand()})

d = 1.0
Je = 2.0
Ke = 20
Ji = -4.0
Ki = 12
conn_dict_ex = {"rule": "fixed_indegree", "indegree": Ke}
conn_dict_in = {"rule": "fixed_indegree", "indegree": Ki}
syn_dict_ex = {"delay": d, "weight": Je}
syn_dict_in = {"delay": d, "weight": Ji}
nest.Connect(neuronpop1, neuronpop2, conn_dict_ex, syn_dict_ex)

multimeter = nest.Create("multimeter")
nest.SetStatus(multimeter, {"withtime": True, "record_from": ["V_m"]})

nest.Connect(multimeter, [neuronpop1[0]])

nest.Simulate(100.0)

dmm = nest.GetStatus(multimeter)[0]
Vms = dmm["events"]["V_m"]
ts = dmm["events"]["times"]

pylab.figure(1)
pylab.plot(ts, Vms)
pylab.show()
