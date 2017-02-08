import nest
import numpy
import pylab

b = 60.0

nest.SetKernelStatus({"local_num_threads":8})

Current_increase = []
Current_decrease = []

time_increase = ""
time_decrease = ""

dict_params = {"V_peak" : 0.0
, "V_reset" : -70.0
, "t_ref" : 2.0
, "g_L" :  30.0
, "C_m" : 281.0
, "E_ex" : 0.0
, "E_in" : -85.0
, "E_L" : -70.0
, "Delta_T" : 2.0
, "tau_w" : 100.0
, "a" : 0.0
, "b" : 40.0
, "V_th" : -55.0
, "tau_syn_ex" : 0.2
, "tau_syn_in" : 2.0
, "I_e" : 200.0
, "w": 0.0}

neurons = nest.Create("aeif_cond_exp", 100)
noise = nest.Create("poisson_generator")

nest.SetStatus(neurons, params=dict_params)

nest.SetStatus(noise, {"rate": 100.0})

for neuron in neurons:
    nest.SetStatus([neuron], {"V_m": dict_params["E_L"]+(dict_params["V_th"]-dict_params["E_L"])*numpy.random.rand()})

voltmeter = nest.Create("voltmeter")

spike_detector = nest.Create("spike_detector")

for n in neurons:
    nest.Connect([n], spike_detector)

nest.Connect(voltmeter, [neurons[0]])
nest.Connect(noise, neurons)

K = 10
d = 1.0
J = float(b)

conn_dict = {"rule": "fixed_indegree", "indegree": K}
syn_dict = {"delay": d, "weight": J}

nest.Connect(neurons, neurons, conn_dict, syn_dict)

for neuron in neurons:
    nest.SetStatus([neuron], {"V_m": dict_params["E_L"]+(dict_params["V_th"]-dict_params["E_L"])*numpy.random.rand()})

nest.SetStatus(neurons, params={"I_e": float(400)})

nest.Simulate(1000.0)

#nest.ResumeSimulation()

#nest.SetStatus(neurons, params={"I_e": 0.0})

#nest.Simulate(1000.0)

dSD = nest.GetStatus(spike_detector, keys='events')[0]
evs = dSD["senders"]
ts_s = dSD["times"]

dmm = nest.GetStatus(voltmeter)[0]
Vms = dmm["events"]["V_m"]
ts_v = dmm["events"]["times"]

average_list = []

for i in range(0, 5010, 10):

    spike_number = 0

    for t in ts_s:

        if float(i) <= t <= float(i) + 5.0:

            spike_number += 1.0

    average_spikes = spike_number / 100.0

    average_list.append(average_spikes)

#spike_list.append(average_list)

nest.ResetKernel()


nest.ResetKernel()

pylab.figure("Adaptation b: " + str(400))

pylab.subplot2grid((3,3),(0,0), colspan=3)
pylab.plot(ts_v, Vms)
pylab.xlim(0, 800)
pylab.xlabel("Time ms")
pylab.ylabel("Voltage pA")
pylab.title("Membrane Potential and Spike Raster Plots")


pylab.subplot2grid((3,3),(1,0), colspan=3)
pylab.plot(ts_s, evs, ".")
pylab.xlim(0, 800)
pylab.xlabel("Time ms")
pylab.ylabel("Neuron Label")
pylab.rcParams.update({'font.size': 30})


pylab.savefig("Adaptation_Plot.png")
#pylab.xlim(5100, 6100)



pylab.show()
