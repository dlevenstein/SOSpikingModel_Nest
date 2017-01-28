import nest
import numpy
import random
import pylab

matrix = []

for exc in range(0,110,10):

    line = []

    for inh in range(0,60,10):

        nest.SetKernelStatus({"local_num_threads":8})

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
        , "I_e" : 500.0
        , "w": 0.0}

        exc_neurons = nest.Create("aeif_cond_exp", 100)
        inh_neurons = nest.Create("aeif_cond_exp", 100)

        noise = nest.Create("noise_generator")

        nest.SetStatus(exc_neurons, params=dict_params)
        nest.SetStatus(inh_neurons, params=dict_params)

        nest.SetStatus(noise, {"std": float(100)})

        for neuron in exc_neurons:
            nest.SetStatus([neuron], {"V_m": dict_params["E_L"]+(dict_params["V_th"]-dict_params["E_L"])*numpy.random.rand()})
        for neuron in inh_neurons:
            nest.SetStatus([neuron], {"V_m": dict_params["E_L"]+(dict_params["V_th"]-dict_params["E_L"])*numpy.random.rand()})

        spike_detector = nest.Create("spike_detector")
        voltmeter = nest.Create("voltmeter")

        for n in exc_neurons:
            nest.Connect([n], spike_detector)
        for n in inh_neurons:
            nest.Connect([n], spike_detector)

        #nest.Connect(voltmeter, [neurons[0]])
        #nest.Connect(noise, neurons)

        K = 10
        d = 1.0

        conn_dict = {"rule": "fixed_indegree", "indegree": K}
        exc_syn_dict = {"delay": d, "weight": float(exc)}
        inh_syn_dict = {"delay": d, "weight": float(-inh)}

        nest.Connect(exc_neurons, exc_neurons, conn_dict, exc_syn_dict)
        nest.Connect(inh_neurons, inh_neurons, conn_dict, inh_syn_dict)
        nest.Connect(exc_neurons, inh_neurons, conn_dict, exc_syn_dict)
        nest.Connect(inh_neurons, exc_neurons, conn_dict, inh_syn_dict)

        for neuron in exc_neurons:
            nest.SetStatus([neuron], {"V_m": dict_params["E_L"]+(dict_params["V_th"]-dict_params["E_L"])*numpy.random.rand()})

        for neuron in inh_neurons:
            nest.SetStatus([neuron], {"V_m": dict_params["E_L"]+(dict_params["V_th"]-dict_params["E_L"])*numpy.random.rand()})

        nest.Simulate(500.0)

        dSD = nest.GetStatus(spike_detector, keys='events')[0]
        evs = dSD["senders"]
        ts_s = dSD["times"]

        firing_rate = numpy.divide(numpy.float64(len(ts_s)),numpy.float64(500.0))

        line.append(firing_rate)

        nest.ResetKernel()

    matrix.append(line)

matrix = numpy.asarray(matrix)

numpy.savetxt("inh_exc_data_0.csv", matrix, delimiter=",")
