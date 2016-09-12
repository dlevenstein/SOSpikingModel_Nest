import nest
import pylab
import numpy

edict = {"I_e": 200.0, "tau_m": 20.0}
idict = {"I_e": 300.0}

nest.CopyModel("iaf_neuron", "exc_iaf_neuron", params=edict)
nest.CopyModel("iaf_neuron", "inh_iaf_neuron", params=idict)

eneuron = nest.Create("exc_iaf_neuron", 100)
ineuron = nest.Create("inh_iaf_neuron", 100)

noise = nest.Create("poisson_generator", 1)
nest.SetStatus(noise, [{"rate": 80000.0}])

multimeter_exc = nest.Create("multimeter")
multimeter_inh = nest.Create("multimeter")

nest.SetStatus(multimeter_exc, {"withtime":True, "record_from":["V_m"]})
nest.SetStatus(multimeter_inh, {"withtime":True, "record_from":["V_m"]})

nest.Connect(multimeter_exc, eneuron)
nest.Connect(multimeter_inh, ineuron)

spikedetector_exc = nest.Create("spike_detector", params={"withgid": True, "withtime": True})
spikedetector_inh = nest.Create("spike_detector", params={"withgid": True, "withtime": True})

nest.Connect(eneuron, spikedetector_exc)
nest.Connect(ineuron, spikedetector_inh)

nest.Simulate(1000.0)

dmm_exc = nest.GetStatus(multimeter_exc)[0]
Vms_exc = dmm_exc["events"]["V_m"]
ts_exc = dmm_exc["events"]["times"]

pylab.figure(1)
pylab.plot(ts_exc, Vms_exc)
pylab.show()

dmm_inh = nest.GetStatus(multimeter_inh)[0]
Vms_inh = dmm_inh["events"]["V_m"]
ts_inh = dmm_inh["events"]["times"]

pylab.figure(2)
pylab.plot(ts_inh, Vms_inh)
pylab.show()

dSD = nest.GetStatus(spikedetector_inh, keys='events')[0]
evs = dSD["senders"]
ts = dSD["times"]
pylab.figure(3)
pylab.plot(ts, evs, ".")
pylab.show()

dSD = nest.GetStatus(spikedetector_exc, keys='events')[0]
evs = dSD["senders"]
ts = dSD["times"]
pylab.figure(4)
pylab.plot(ts, evs, ".")
pylab.show()
