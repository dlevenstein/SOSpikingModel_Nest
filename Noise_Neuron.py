import nest
import pylab

neuron = nest.Create("iaf_neuron")

multimeter = nest.Create("multimeter")
nest.SetStatus(multimeter, {"withtime": True, "record_from": ["V_m"]})

spikedetector = nest.Create("spike_detector", params={"withgid": True, "withtime": True})

nest.Connect(multimeter, neuron)
nest.Connect(neuron, spikedetector)

noise = nest.Create("poisson_generator", 2)
nest.SetStatus(noise, [{"rate": 80000.0}, {"rate":15000.0}])

nest.SetStatus(neuron, {"I_e":0.0})

syn_dict_ex = {"weight": 1.2}
syn_dict_in = {"weight": -2.0}
nest.Connect([noise[0]], neuron, syn_spec=syn_dict_ex)
nest.Connect([noise[1]], neuron, syn_spec=syn_dict_in)

nest.Simulate(1000.0)

dmm = nest.GetStatus(multimeter)[0]
Vms = dmm["events"]["V_m"]
ts = dmm["events"]["times"]

pylab.figure(1)
pylab.plot(ts, Vms)
pylab.show()

pylab.figure(2)
pylab.plot(ts, noise[0])
pylab.show()

pylab.figure(3)
pylab.plot(ts, noise[1])
pylab.show()

dSD = nest.GetStatus(spikedetector, keys='events')[0]
evs = dSD["senders"]
ts = dSD["times"]
pylab.figure(2)
pylab.plot(ts, evs, ".")
pylab.show()
