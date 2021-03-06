import nest
import numpy

def neuron_population(I, J_mean, J_sigma, b, N, time, distribution=False):

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

    nest.Connect(voltmeter, [neurons[0]])
    nest.Connect(noise, neurons)

    K = 10
    d = 1.0

    if distribution==False:
        conn_dict = {"rule": "fixed_indegree", "indegree": K}
        syn_dict = {"delay": d, "weight": float(J_mean)}

    if distribution==True:
        conn_dict = {"rule": "fixed_indegree", "indegree": K}
        syn_dict = {"delay": d, "weight": {'distribution': 'normal', 'mu': float(J_mean), 'sigma': float(J_sigma)}}

    nest.Connect(neurons, neurons, conn_dict, syn_dict)

    for neuron in neurons:
        nest.SetStatus([neuron], {"V_m": dict_params["E_L"]+(dict_params["V_th"]-dict_params["E_L"])*numpy.random.rand()})

    start = numpy.float64(0.0)
    end = numpy.float64(0.0)

    I_line = []

    for i in I:

        nest.SetStatus(neurons, params={"I_e": float(i)})

        nest.Simulate(time)
        nest.ResumeSimulation()

        dSD = nest.GetStatus(spike_detector, keys='events')[0]
        evs = dSD["senders"]
        ts_s = dSD["times"]

        dmm = nest.GetStatus(voltmeter)[0]
        Vms = dmm["events"]["V_m"]
        ts_v = dmm["events"]["times"]

        start = end
        end += numpy.float64(time)

        data_set = ts_s[(ts_s > start) & (ts_s <= end)]

        firing_rate = numpy.multiply(numpy.divide(numpy.float64(len(data_set)),numpy.float64(50000.0)),numpy.float64(1000.0))
        I_line.append(firing_rate)

    return ts_s, evs, ts_v, Vms, I_line
