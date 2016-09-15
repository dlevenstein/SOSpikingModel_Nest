import nest
import pylab
import numpy

edict = {"I_e": 220.0, "tau_m": 20.0}
idict = {"I_e": 350.0}

nest.CopyModel("iaf_neuron", "exc_iaf_neuron", params=edict)
nest.CopyModel("iaf_neuron", "inh_iaf_neuron", params=idict)

epop1 = nest.Create("exc_iaf_neuron", 100)
ipop1 = nest.Create("inh_iaf_neuron", 100)

Vth=-55.
Vrest=-70.
for neuron in epop1:
    nest.SetStatus([neuron], {"V_m": Vrest+(Vth-Vrest)*numpy.random.rand()})

Vth=-55.
Vrest=-70.
for neuron in ipop1:
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

multimeter_exc = nest.Create("multimeter")
multimeter_inh = nest.Create("multimeter")

nest.SetStatus(multimeter_exc, {"withtime":True, "record_from":["V_m"]})
nest.SetStatus(multimeter_inh, {"withtime":True, "record_from":["V_m"]})

multimeter_exc_0 = nest.Create("multimeter")
multimeter_exc_1 = nest.Create("multimeter")
multimeter_exc_2 = nest.Create("multimeter")

multimeter_inh_0 = nest.Create("multimeter")
multimeter_inh_1 = nest.Create("multimeter")
multimeter_inh_2 = nest.Create("multimeter")

nest.SetStatus(multimeter_exc_0, {"withtime":True, "record_from":["V_m"]})
nest.SetStatus(multimeter_exc_1, {"withtime":True, "record_from":["V_m"]})
nest.SetStatus(multimeter_exc_2, {"withtime":True, "record_from":["V_m"]})

nest.SetStatus(multimeter_inh_0, {"withtime":True, "record_from":["V_m"]})
nest.SetStatus(multimeter_inh_1, {"withtime":True, "record_from":["V_m"]})
nest.SetStatus(multimeter_inh_2, {"withtime":True, "record_from":["V_m"]})

nest.Connect(multimeter_exc, epop1[0:10])
nest.Connect(multimeter_inh, ipop1[0:10])

nest.Connect(multimeter_exc_0, [epop1[0]])
nest.Connect(multimeter_exc_1, [epop1[1]])
nest.Connect(multimeter_exc_2, [epop1[2]])

nest.Connect(multimeter_inh_0, [ipop1[0]])
nest.Connect(multimeter_inh_1, [ipop1[1]])
nest.Connect(multimeter_inh_2, [ipop1[2]])

spikedetector_exc = nest.Create("spike_detector", params={"withgid": True, "withtime": True})
spikedetector_inh = nest.Create("spike_detector", params={"withgid": True, "withtime": True})

for neuron_exc in epop1:
    nest.Connect([neuron_exc], spikedetector_exc)

for neuron_inh in ipop1:
    nest.Connect([neuron_inh], spikedetector_inh)

nest.Simulate(500.0)

dmm_exc_0 = nest.GetStatus(multimeter_exc_0)[0]
Vms_exc_0 = dmm_exc_0["events"]["V_m"]
ts_exc_0 = dmm_exc_0["events"]["times"]

dmm_exc_1 = nest.GetStatus(multimeter_exc_1)[0]
Vms_exc_1 = dmm_exc_1["events"]["V_m"]
ts_exc_1 = dmm_exc_1["events"]["times"]

dmm_exc_2 = nest.GetStatus(multimeter_exc_2)[0]
Vms_exc_2 = dmm_exc_2["events"]["V_m"]
ts_exc_2 = dmm_exc_2["events"]["times"]

pylab.subplot2grid((3,3),(0,0), colspan=1)
pylab.plot(ts_exc_0, Vms_exc_0)
pylab.plot(ts_exc_1, Vms_exc_1)
pylab.plot(ts_exc_2, Vms_exc_2)
pylab.title("Excitatory Neurons")

dmm_inh_0 = nest.GetStatus(multimeter_inh_0)[0]
Vms_inh_0 = dmm_inh_0["events"]["V_m"]
ts_inh_0 = dmm_inh_0["events"]["times"]

dmm_inh_1 = nest.GetStatus(multimeter_inh_1)[0]
Vms_inh_1 = dmm_inh_1["events"]["V_m"]
ts_inh_1 = dmm_inh_1["events"]["times"]

dmm_inh_2 = nest.GetStatus(multimeter_inh_2)[0]
Vms_inh_2 = dmm_inh_2["events"]["V_m"]
ts_inh_2 = dmm_inh_2["events"]["times"]

pylab.subplot2grid((3,3),(0,1), colspan=1)
pylab.plot(ts_inh_0, Vms_inh_0)
pylab.plot(ts_inh_1, Vms_inh_1)
pylab.plot(ts_inh_2, Vms_inh_2)
pylab.title("Inhibitatory Neurons")

dSD = nest.GetStatus(spikedetector_exc, keys='events')[0]
evs = dSD["senders"]
ts = dSD["times"]
pylab.subplot2grid((3,3),(1,0), colspan=1)
pylab.plot(ts, evs, ".")
pylab.title("Excitatory Neurons")

dSD = nest.GetStatus(spikedetector_inh, keys='events')[0]
evs = dSD["senders"]
ts = dSD["times"]
pylab.subplot2grid((3,3),(1,1))
pylab.plot(ts, evs, ".")
pylab.title("Inhibitatory Neurons")

dmm_exc = nest.GetStatus(multimeter_exc)[0]
Vms_exc = dmm_exc["events"]["V_m"]
ts_exc = dmm_exc["events"]["times"]

pylab.subplot2grid((3,3),(2,0), colspan=1)
pylab.plot(ts_exc, Vms_exc)
pylab.title("Excitatory Neurons")

dmm_inh = nest.GetStatus(multimeter_inh)[0]
Vms_inh = dmm_inh["events"]["V_m"]
ts_inh = dmm_inh["events"]["times"]

pylab.subplot2grid((3,3),(2,1), colspan=1)
pylab.plot(ts_inh, Vms_inh)
pylab.title("Inhibitatory Neurons")

pylab.show()
