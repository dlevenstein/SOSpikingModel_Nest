import nest
import numpy as np
import pylab

J_parameters_small = np.arange(0,100,0.2)

mean_rate_string_small = ""

time_string = ""
J_string = ""

for J_s in J_parameters_small:

    nest.SetKernelStatus({"local_num_threads":8})

    neuron_population = 100
    simulation_time = 1000.0

    I_e = 0.0

    dict_parameters_1 = {'a': 4.0,
              'b': 80.8,
              'V_th': -50.4,
              'Delta_T': 2.0,
              'I_e': 0.0,
              'C_m': 281.0,
              'g_L': 30.0,
              'V_reset': -70.6,
              'tau_w': 144.0,
              't_ref': 5.0,
              'V_peak': -40.0,
              'E_L': -70.6,
              'E_ex': 0.,
              'E_in': -70.}

    epop_1 = nest.Create("iaf_neuron", neuron_population)

    nest.SetStatus(epop_1, params=dict_parameters_1)

    for neuron in epop_1:
        nest.SetStatus([neuron], {"V_m": dict_parameters_1["E_L"]+(dict_parameters_1["V_th"]-dict_parameters_1["E_L"])*np.random.rand()})

    spikedetector_1 = nest.Create("spike_detector", params={"withgid": True, "withtime": True})

    for neuron_1 in epop_1:

        nest.Connect([neuron_1], spikedetector_1)

    K = 20
    d = 1.0
    J = float(J_s)

    conn_dict_1 = {"rule": "fixed_indegree", "indegree": K}
    syn_dict_1 = {"delay": d, "weight": J}

    nest.Connect(epop_1, epop_1, conn_dict_1, syn_dict_1)

    length = np.float64(0)

    for I in range(500, -10, -10):
        print(I)
        I_e = float(I)

        nest.SetStatus(epop_1, params={"I_e": I_e})

        nest.Simulate(simulation_time)

        dSD = nest.GetStatus(spikedetector_1, keys='events')[0]
        evs_1 = dSD["senders"]
        ts_1 = dSD["times"]

        nest.ResumeSimulation()

    nest.ResetKernel()
    nest.ResetNetwork()

    time_string += str(ts_1[-1]) + ", "

open_file = open("J_value_map_decrease.txt", "w")
open_file.write(time_string)
open_file.write(J_string)
open_file.close()
