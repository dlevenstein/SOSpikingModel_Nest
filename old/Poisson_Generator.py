import nest
import pylab

neuron = nest.Create("iaf_neuron")

nest.GetStatus(neuron, "I_e")
nest.GetStatus(neuron, ["V_reset","V_th"])
nest.SetStatus(neuron, {"I_e": 376.0})

multimeter = nest.Create("multimeter")
nest.SetStatus(multimeter, {"withtime": True, "record_from": ["V_m"]})

noise = nest.Create("poisson_generator", 1)
nest.SetStatus(noise, [{"rate": 80000.0}])

syn_dict_ex = {"weight": 1.2}

nest.Connect(multimeter, neuron)
nest.Connect([noise[0]], neuron, syn_spec=syn_dict_ex)

nest.Simulate(1000.0)

dmm = nest.GetStatus(multimeter)[0]
Vms = dmm["events"]["V_m"]
ts = dmm["events"]["times"]

pylab.figure(1)
pylab.plot(ts, Vms)
pylab.show()
