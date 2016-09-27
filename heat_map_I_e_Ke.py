import nest
import numpy as np
import simplejson

nest.SetKernelStatus({"local_num_threads": 8})

neuron_population = 1000
simulation_time = 10.0

I_e = 0.0

mean_rate_Ke = []
mean_rate_list = []

dict_parameters_exc = {"E_L": -70.0, "C_m": 250.0, "tau_m": 20.0, "t_ref": 2.0, "V_th": -55.0, "V_reset": -70.0, "tau_syn":  2.0, "I_e": I_e}

epop = nest.Create("iaf_neuron", neuron_population)
for neuron in epop:
    nest.SetStatus([neuron], {"V_m": dict_parameters_exc["E_L"]+(dict_parameters_exc["V_th"]-dict_parameters_exc["E_L"])*np.random.rand()})

for i in range(0,500,10):

    I_e = float(i)

    d = 1.0
    Je = 9.0
    Ke = 0

    nest.SetStatus(epop, params={"I_e": I_e})
    for j in range(1,21):

        Ke = j

        conn_dict_ex = {"rule": "fixed_indegree", "indegree": Ke}
        syn_dict_ex = {"delay": d, "weight": Je}

        nest.Connect(epop, epop, conn_dict_ex, syn_dict_ex)

        spikedetector_exc = nest.Create("spike_detector", params={"withgid": True, "withtime": True})

        for neuron_exc in epop:
            nest.Connect([neuron_exc], spikedetector_exc)

        nest.Simulate(simulation_time)

        dSD = nest.GetStatus(spikedetector_exc, keys='events')[0]
        evs = dSD["senders"]
        ts = dSD["times"]

        total = 0.0

        for i in range(len(evs)):

            total += evs[i]

        mean_rate = total / (neuron_population * simulation_time)
        print(I_e, Ke)
        print(total, mean_rate)
        mean_rate_Ke.append(mean_rate)

    mean_rate_list.append(mean_rate_Ke)
    open_file = open("heat_map_values_I_e_Ke.json", "w")
    simplejson.dump(mean_rate_list, open_file)
    open_file.close()
    mean_rate_Ke = []
