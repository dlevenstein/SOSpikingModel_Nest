import nest
import pylab
import numpy

def neuron_population(I, J, b, N, time):

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
    , "b" : float(b)
    , "V_th" : -55.0
    , "tau_syn_ex" : 0.2
    , "tau_syn_in" : 2.0
    , "I_e" : 0.0
    , "w": 0.0}

    neurons = nest.Create("aeif_cond_exp", 100)
    noise = nest.Create("noise_generator")

    nest.SetStatus(neurons, params=dict_params)

    nest.SetStatus(noise, {"std": float(N)})

    for neuron in neurons:
        nest.SetStatus([neuron], {"V_m": dict_params["E_L"]+(dict_params["V_th"]-dict_params["E_L"])*numpy.random.rand()})

    spike_detector = nest.Create("spike_detector")
    voltmeter = nest.Create("voltmeter")

    for n in neurons:
        nest.Connect([n], spike_detector)

    K = 10
    d = 1.0

    conn_dict = {"rule": "fixed_indegree", "indegree": K}
    syn_dict = {"delay": d, "weight": float(J)}

    nest.Connect(neurons, neurons, conn_dict, syn_dict)

    for neuron in neurons:
        nest.SetStatus([neuron], {"V_m": dict_params["E_L"]+(dict_params["V_th"]-dict_params["E_L"])*numpy.random.rand()})

    for i in I:

        nest.SetStatus(neurons, params={"I_e": float(i)})

        nest.Simulate(time)
        nest.ResumeSimulation()

        dSD = nest.GetStatus(spike_detector, keys='events')[0]
        evs = dSD["senders"]
        ts_s = dSD["times"]

    return ts_s, evs
