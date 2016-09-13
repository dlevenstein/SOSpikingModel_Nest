import nest
import pylab
import numpy

edict = {"I_e": 220.0, "tau_m": 20.0}
idict = {"I_e": 350.0}

nest.CopyModel("iaf_neuron", "exc_iaf_neuron", params=edict)
nest.CopyModel("iaf_neuron", "inh_iaf_neuron", params=idict)

epop1 = nest.Create("exc_iaf_neuron", 100)
ipop1 = nest.Create("inh_iaf_neuron", 100)
epop2 = nest.Create("exc_iaf_neuron", 100)
ipop2 = nest.Create("inh_iaf_neuron", 100)

Vth=-55.
Vrest=-70.
for neuron in epop1:
    nest.SetStatus([neuron], {"V_m": Vrest+(Vth-Vrest)*numpy.random.rand()})

Vth=-55.
Vrest=-70.
for neuron in epop2:
    nest.SetStatus([neuron], {"V_m": Vrest+(Vth-Vrest)*numpy.random.rand()})

Vth=-55.
Vrest=-70.
for neuron in ipop1:
    nest.SetStatus([neuron], {"V_m": Vrest+(Vth-Vrest)*numpy.random.rand()})

Vth=-55.
Vrest=-70.
for neuron in ipop2:
    nest.SetStatus([neuron], {"V_m": Vrest+(Vth-Vrest)*numpy.random.rand()})

d = 1.0
Je = 5.0
Ke = 20
Ji = -4.0
Ki = 12

conn_dict_ex = {"rule": "fixed_indegree", "indegree": Ke}
conn_dict_in = {"rule": "fixed_indegree", "indegree": Ki}
syn_dict_ex = {"delay": d, "weight": Je}
syn_dict_in = {"delay": d, "weight": Ji}
nest.Connect(epop1, ipop1, conn_dict_ex, syn_dict_ex)
nest.Connect(epop1, epop1, conn_dict_ex, syn_dict_ex)
nest.Connect(ipop1, epop1, conn_dict_in, syn_dict_in)
nest.Connect(ipop1, ipop1, conn_dict_in, syn_dict_in)

multimeter_exc_0 = nest.Create("multimeter")
multimeter_exc_1 = nest.Create("multimeter")
multimeter_exc_2 = nest.Create("multimeter")

nest.SetStatus(multimeter_exc_0, {"withtime":True, "record_from":["V_m"]})
nest.SetStatus(multimeter_exc_1, {"withtime":True, "record_from":["V_m"]})
nest.SetStatus(multimeter_exc_2, {"withtime":True, "record_from":["V_m"]})


multimeter_inh = nest.Create("multimeter")

nest.SetStatus(multimeter_inh, {"withtime":True, "record_from":["V_m"]})

nest.Connect(multimeter_exc_0, [epop1[0]])
nest.Connect(multimeter_exc_1, [epop1[1]])
nest.Connect(multimeter_exc_2, [epop1[2]])


nest.Connect(multimeter_inh, [ipop1[0]])

spikedetector_exc = nest.Create("spike_detector", params={"withgid": True, "withtime": True})
spikedetector_inh = nest.Create("spike_detector", params={"withgid": True, "withtime": True})

for neuron_exc in epop1:
    nest.Connect([neuron_exc], spikedetector_exc)

for neuron_inh in ipop1:
    nest.Connect([neuron_inh], spikedetector_inh)

nest.Simulate(500.0)

dmm_exc = nest.GetStatus(multimeter_exc_0)[0]
Vms_exc = dmm_exc["events"]["V_m"]
ts_exc = dmm_exc["events"]["times"]

dmm_exc = nest.GetStatus(multimeter_exc_1)[0]
Vms_exc = dmm_exc["events"]["V_m"]
ts_exc = dmm_exc["events"]["times"]

dmm_exc = nest.GetStatus(multimeter_exc_2)[0]
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

dSD = nest.GetStatus(spikedetector_exc, keys='events')[0]
evs = dSD["senders"]
ts = dSD["times"]
pylab.figure(3)
pylab.plot(ts, evs, ".")
pylab.show()

dSD = nest.GetStatus(spikedetector_inh, keys='events')[0]
evs = dSD["senders"]
ts = dSD["times"]
pylab.figure(4)
pylab.plot(ts, evs, ".")
pylab.show()
