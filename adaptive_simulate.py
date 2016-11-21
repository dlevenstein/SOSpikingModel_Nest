import nest
import numpy
import pylab

nest.SetKernelStatus({"local_num_threads":8})

Current_increase = []
Current_decrease = []

Time = []

labels = []


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
, "b" : 0.0
, "V_th" : -55.0
, "tau_syn_ex" : 0.2
, "tau_syn_in" : 2.0
, "I_e" : 200.0
, "w": 0.0}

I_e_rate_list_increase = ""

I_e_rate_list_decrease = ""

#for i in range(0,110,10):

neurons = nest.Create("aeif_cond_exp", 200)

nest.SetStatus(neurons, params=dict_params)

for neuron in neurons:
    nest.SetStatus([neuron], {"V_m": dict_params["E_L"]+(dict_params["V_th"]-dict_params["E_L"])*numpy.random.rand()})

spike_detector = nest.Create("spike_detector")

for n in neurons:
    nest.Connect([n], spike_detector)

K = 10
d = 1.0
J = float(0.0)

conn_dict = {"rule": "fixed_indegree", "indegree": K}
syn_dict = {"delay": d, "weight": J}

nest.Connect(neurons, neurons, conn_dict, syn_dict)

Time_number = 0.0

for I in range(0,510,10):

    Time_number += 100.0

    Current_increase.append(I)

    nest.SetStatus(neurons, params={"I_e": float(I)})

    nest.Simulate(100.0)

    Time.append(Time_number)

    nest.ResumeSimulation()

dSD_inc = nest.GetStatus(spike_detector, keys='events')[0]
evs_inc = dSD_inc["senders"]
ts_inc = dSD_inc["times"]

time_increase = []

for t_i in ts_inc:
    time_increase.append(t_i / 10.0)

for neuron in neurons:
    nest.SetStatus([neuron], {"V_m": dict_params["E_L"]+(dict_params["V_th"]-dict_params["E_L"])*numpy.random.rand()})

for I in range(500,-10,-10):

    labels.append(I)

    Current_decrease.append(I)

    nest.SetStatus(neurons, params={"I_e": float(I)})

    nest.Simulate(100.0)

    nest.ResumeSimulation()


dSD_dec = nest.GetStatus(spike_detector, keys='events')[0]
evs_dec = dSD_dec["senders"]
ts_dec = dSD_dec["times"]

time_decrease = []

for t_d in ts_dec:
    time_decrease.append(t_d/10.0)

pylab.figure("Weight " + str(J))
pylab.subplot2grid((3,3),(0,0), colspan=3)
pylab.plot(ts_inc, evs_inc, ".")
pylab.gca().invert_xaxis()
pylab.xlim(5100,0)
pylab.title("Increasing Current")
pylab.xlabel("Time ms")
pylab.ylabel("Neuron label")
#pylab.xticks(ts_inc, labels, rotation='vertical')

pylab.subplot2grid((3,3),(1,0), colspan=3)
pylab.plot(ts_dec, evs_dec, ".")
pylab.xlim(5100,10200)
pylab.title("Decreasing Current")
pylab.xlabel("Time ms")
pylab.ylabel("Neuron label")
#pylab.xticks(ts_dec, labels, rotation='vertical')



pylab.subplot2grid((3,3),(2,0), colspan=3)
pylab.plot(Time, Current_increase)
pylab.plot(Time, Current_decrease)
pylab.title("Currents I_e")



pylab.show()

"""open_file = open("I_e_rate_list_increase", "w")
open_file.write(I_e_rate_list_increase)
open_file.close()

open_file = open("I_e_rate_list_decrease", "w")
open_file.write(I_e_rate_list_decrease)
open_file.close()"""
