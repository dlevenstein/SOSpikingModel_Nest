import nest
import pylab

neuron = nest.Create("iaf_neuron")

nest.GetStatus(neuron, "I_e")
nest.GetStatus(neuron, ["V_reset","V_th"])
nest.SetStatus(neuron, {"I_e": -376.0})

multimeter = nest.Create("multimeter")
nest.SetStatus(multimeter, {"withtime": True, "record_from": ["V_m"]})

spikedetector = nest.Create("spike_detector", params={"withgid": True, "withtime": True})

nest.Connect(multimeter, neuron)
nest.Connect(neuron, spikedetector)

nest.Simulate(1000.0)


dmm = nest.GetStatus(multimeter)[0]
Vms = dmm["events"]["V_m"]
ts = dmm["events"]["times"]

pylab.figure(1)
pylab.plot(ts, Vms)
pylab.show()

'''dSD = nest.GetStatus(spikedetector, keys='events')[0]
evs = dSD["senders"]
ts = dSD["times"]
pylab.figure(2)
pylab.plot(ts, evs, ".")
pylab.show()'''
