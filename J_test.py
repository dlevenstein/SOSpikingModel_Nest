import nest
import numpy as np


nest.SetKernelStatus({"local_num_threads":8})

neuron_population = 1000
simulation_time = 1000.0

I_e = 0.0

dict_parameters_1 = {"E_L": -70.0, "C_m": 250.0, "tau_m": 20.0, "t_ref": 2.0, "V_th": -55.0, "V_reset": -70.0, "tau_syn":  2.0, "I_e": I_e}

epop_1 = nest.Create("iaf_neuron", neuron_population)

nest.SetStatus(epop_1, params=dict_parameters_1)

for neuron in epop_1:
    nest.SetStatus([neuron], {"V_m": dict_parameters_1["E_L"]+(dict_parameters_1["V_th"]-dict_parameters_1["E_L"])*np.random.rand()})

spikedetector_1 = nest.Create("spike_detector", params={"withgid": True, "withtime": True})

for neuron_1 in epop_1:

    nest.Connect([neuron_1], spikedetector_1)

J_parameters_small = np.arange(0,10,0.2)

mean_rate_string_small = ""

for J_s in J_parameters_small:

    K = 20
    d = 1.0
    J = J_s

    conn_dict_1 = {"rule": "fixed_indegree", "indegree": K}
    syn_dict_1 = {"delay": d, "weight": J}

    nest.Connect(epop_1, epop_1, conn_dict_1, syn_dict_1)

    length = np.float64(0)

    for I in [500,250,0]:

        I_e = float(I)

        nest.SetStatus(epop_1, params={"I_e": I_e})

        nest.Simulate(simulation_time)

        dSD = nest.GetStatus(spikedetector_1, keys='events')[0]
        evs_1 = dSD["senders"]
        ts_1 = dSD["times"]

        total = np.subtract(len(ts_1), length)

        length = np.add(length, total)

        mean_rate = np.divide(total, np.multiply(neuron_population, simulation_time))

        mean_rate_string_small += str(mean_rate) + ","

    mean_rate_string_small += str(J_s) + "\n"

open_file = open("small_J_values", "w")
open_file.write(mean_rate_string_small)
open_file.close()

nest.ResetKernel()
nest.ResetNetwork()

nest.SetKernelStatus({"local_num_threads":8})

neuron_population = 1000
simulation_time = 1000.0

I_e = 0.0

dict_parameters_1 = {"E_L": -70.0, "C_m": 250.0, "tau_m": 20.0, "t_ref": 2.0, "V_th": -55.0, "V_reset": -70.0, "tau_syn":  2.0, "I_e": I_e}

epop_2 = nest.Create("iaf_neuron", neuron_population)

nest.SetStatus(epop_2, params=dict_parameters_1)

for neuron in epop_2:
    nest.SetStatus([neuron], {"V_m": dict_parameters_1["E_L"]+(dict_parameters_1["V_th"]-dict_parameters_1["E_L"])*np.random.rand()})


spikedetector_2 = nest.Create("spike_detector", params={"withgid": True, "withtime": True})

for neuron_2 in epop_2:

    nest.Connect([neuron_2], spikedetector_2)

J_parameters_large = np.arange(0,100,2)

mean_rate_string_large = ""

for J_l in J_parameters_large:

    K = 20
    d = 1.0
    J = float(J_l)

    conn_dict_2 = {"rule": "fixed_indegree", "indegree": K}
    syn_dict_2 = {"delay": d, "weight": J}

    nest.Connect(epop_2, epop_2, conn_dict_2, syn_dict_2)

    length = np.float64(0)

    for I in [500,250,0]:

        I_e = float(I)

        nest.SetStatus(epop_2, params={"I_e": I_e})

        nest.Simulate(simulation_time)

        dSD = nest.GetStatus(spikedetector_2, keys='events')[0]
        evs_2 = dSD["senders"]
        ts_2 = dSD["times"]

        total = np.subtract(len(ts_2), length)

        length = np.add(length, total)

        mean_rate = np.divide(total, np.multiply(neuron_population, simulation_time))

        mean_rate_string_large += str(mean_rate) + ","

    mean_rate_string_large += str(J_l) + "\n"

open_file = open("large_J_values", "w")
open_file.write(mean_rate_string_large)
open_file.close()
