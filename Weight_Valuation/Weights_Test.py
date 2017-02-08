import nest
import numpy
import simplejson
import pylab


for J in [50]:


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
    , "I_e" : 200.0
    , "w": 0.0}

    neurons = nest.Create("aeif_cond_exp", 100)
    #noise = nest.Create("poisson_generator")

    voltmeter = nest.Create("voltmeter")
    nest.SetStatus(neurons, params=dict_params)

    #research noise modules
    #nest.SetStatus(noise, {"rate": 100.0})

    for neuron in neurons:
        nest.SetStatus([neuron], {"V_m": dict_params["E_L"]+(dict_params["V_th"]-dict_params["E_L"])*numpy.random.rand()})

    spike_detector = nest.Create("spike_detector")

    for n in neurons:
        nest.Connect([n], spike_detector)

    #nest.Connect(noise, neurons)

    K = 10
    d = 1.0

    conn_dict = {"rule": "fixed_indegree", "indegree": K}
    syn_dict = {"delay": d, "weight": float(J)}

    nest.Connect(neurons, neurons, conn_dict, syn_dict)
    nest.Connect(voltmeter, [neurons[0]])

    for neuron in neurons:
        nest.SetStatus([neuron], {"V_m": dict_params["E_L"]+(dict_params["V_th"]-dict_params["E_L"])*numpy.random.rand()})

    for I in range(600,-10,-10):

        nest.SetStatus(neurons, params={"I_e": float(I)})

        nest.Simulate(500.0)

        dSD = nest.GetStatus(spike_detector, keys='events')[0]
        evs = dSD["senders"]
        ts_s = dSD["times"]

        nest.ResumeSimulation()

        dmm = nest.GetStatus(voltmeter)[0]
        Vms = dmm["events"]["V_m"]
        ts = dmm["events"]["times"]

    Vms.tolist()
    ts.tolist()

    #print(Vms, ts)
    array_volts = []
    array_volts.append(ts)
    array_volts.append(Vms)


    #numpy.savetxt("No_adaptation_J_" + str(J) + "_volt_values_decreasing.csv", array_volts, delimiter=",")


    #pylab.figure("J: " + str(J) + "Membrane Potential, No Adaptation")
    #pylab.plot(ts, Vms)
    #pylab.xlabel("Time: ms")
    #pylab.ylabel("Membrane Potential")
    #pylab.title("J: " + str(J) + "Membrane Potential, No Adaptation")

    ts_s.tolist()
    evs.tolist()

    array_spikes = []
    array_spikes.append(ts_s)
    array_spikes.append(evs)

    #array_spikes = numpy.asarray(array_spikes)

    #print(array_spikes)
    numpy.savetxt("No_adaptation_J_" + str(J) + "_spike_values_increasing.csv", array_spikes, delimiter=",")

    """#send raw data
    print(len(range(19000,25000,500)), len(range(390, 500, -10)))

    pylab.figure("Full Spike Raster External Increasing, J: " + str(J))
    pylab.plot(ts_s, evs, "b.")
    pylab.xlim(19000,25500)
    pylab.xticks(range(19000,25500,500), range(380, 510, 10))
    #pylab.xlim(0, 5500)
    pylab.title("No Adaptation Spike Raster External Increasing, J: " + str(J))
    pylab.xlabel("External Current: I (pA)")
    pylab.ylabel("Neuron ID")

    pylab.savefig("Full Spike Raster External Increasing, J: " + str(J) + ".png")"""

    nest.ResetKernel()

#pylab.show()
