import nest
import pylab

pop1 = nest.Create("iaf_neuron", 10)
nest.SetStatus(pop1, {"I_e":-376.0})
pop2 = nest.Create("iaf_neuron", 10)
nest.SetStatus(pop2, {"I_e":376.0})
multimeter = nest.Create("multimeter", 10)
nest.SetStatus(multimeter, {"withtime":True, "record_from":["V_m"]})

nest.Connect(pop1, pop2, syn_spec = {"weight":20.0})

nest.Connect(multimeter, pop2)

nest.Simulate(1000.0)

dmm = nest.GetStatus(multimeter)[0]
Vms = dmm["events"]["w"]
ts = dmm["events"]["times"]

pylab.figure(1)
pylab.plot(ts, Vms)
pylab.show()
