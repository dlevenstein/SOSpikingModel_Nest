import nest
import pylab

neuron1 = nest.Create("iaf_neuron")
neuron2 = nest.Create("iaf_neuron")

nest.GetStatus(neuron1, "I_e")
nest.GetStatus(neuron1, ["V_reset","V_th"])
nest.SetStatus(neuron1, {"I_e": 55.0})

nest.GetStatus(neuron2, "I_e")
nest.GetStatus(neuron2, ["V_reset","V_th"])
nest.SetStatus(neuron2, {"I_e": 376.0})

multimeter = nest.Create("multimeter")
nest.SetStatus(multimeter, {"withtime": True, "record_from": ["V_m"]})

spikedetector = nest.Create("spike_detector", params={"withgid": True, "withtime": True})

nest.Connect(multimeter, neuron2)
nest.Connect(neuron1, neuron2, syn_spec = {"weight":20.0})
nest.Connect(neuron2, spikedetector)

nest.Simulate(1000.0)

"""dmm = nest.GetStatus(multimeter)[0]
Vms = dmm["events"]["V_m"]
ts = dmm["events"]["times"]

pylab.figure(1)
pylab.plot(ts, Vms)
pylab.show()"""

dSD = nest.GetStatus(spikedetector, keys='events')[0]
evs = dSD["senders"]
ts = dSD["times"]
print(ts[0],evs[0])
pylab.figure(2)
pylab.plot(ts, evs, ".")
pylab.show()
