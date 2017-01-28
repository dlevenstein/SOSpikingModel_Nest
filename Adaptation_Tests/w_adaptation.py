import nest
import numpy
import pylab

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
, "a" : 4.0
, "b" : 80.5
, "V_th" : -55.0
, "tau_syn_ex" : 0.2
, "tau_syn_in" : 2.0
, "I_e" : 200.0
, "w": 0.0}

I_e_rate_list_increase = ""

I_e_rate_list_decrease = ""

#weight_list = numpy.arange(0,110, 0.2)

for i in range(0,110, 10):

    neurons = nest.Create("aeif_cond_exp", 100)

    nest.SetStatus(neurons, params=dict_params)

    for neuron in neurons:
        nest.SetStatus([neuron], {"V_m": dict_params["E_L"]+(dict_params["V_th"]-dict_params["E_L"])*numpy.random.rand()})

    spike_detector = nest.Create("spike_detector")

    for n in neurons:
        nest.Connect([n], spike_detector)

    K = 10
    d = 1.0
    J = float(i)

    conn_dict = {"rule": "fixed_indegree", "indegree": K}
    syn_dict = {"delay": d, "weight": J}

    nest.Connect(neurons, neurons, conn_dict, syn_dict)

    Time_number = 0.0

    for I in range(0,510,10):

        Time_number += 100.0

        Current_increase.append(I)

        nest.SetStatus(neurons, params={"I_e": float(I)})

        nest.Simulate(100.0)

        nest.ResumeSimulation()

    dSD_inc = nest.GetStatus(spike_detector, keys='events')[0]
    evs_inc = dSD_inc["senders"]
    ts_inc = dSD_inc["times"]

    time_increase += str(ts_inc[0]) + ", "

    for neuron in neurons:
        nest.SetStatus([neuron], {"V_m": dict_params["E_L"]+(dict_params["V_th"]-dict_params["E_L"])*numpy.random.rand()})

    for I in range(500,-10,-10):

        Current_decrease.append(I)

        nest.SetStatus(neurons, params={"I_e": float(I)})

        nest.Simulate(100.0)

        nest.ResumeSimulation()

    dSD_dec = nest.GetStatus(spike_detector, keys='events')[0]
    evs_dec = dSD_dec["senders"]
    ts_dec = dSD_dec["times"]

    time_decrease += str(ts_dec[-1]) + ", "

    nest.ResetNetwork()
    nest.ResetKernel()

open_file = open("w_adaptation_increase.txt", "w")
open_file.write(time_increase)
open_file.close()

open_file = open("w_adaptation_decrease.txt", "w")
open_file.write(time_decrease)
open_file.close()
