import nest
import numpy
import simplejson
import pylab
import matplotlib.pyplot as plt

spike_list = []

for J in range(0,105,5):

    nest.SetKernelStatus({"local_num_threads":8})

    #list_values = []

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
    , "b" : 70.0
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

    spike_detector = nest.Create("spike_detector")

    for n in neurons:
        nest.Connect([n], spike_detector)

    nest.Connect(noise, neurons)

    K = 10
    d = 1.0

    conn_dict = {"rule": "fixed_indegree", "indegree": K}
    syn_dict = {"delay": d, "weight": float(J)}

    nest.Connect(neurons, neurons, conn_dict, syn_dict)

    for neuron in neurons:
        nest.SetStatus([neuron], {"V_m": dict_params["E_L"]+(dict_params["V_th"]-dict_params["E_L"])*numpy.random.rand()})

    start = 0

    mean_spike_list = []

    for I in range(0,510,10):

        nest.SetStatus(neurons, params={"I_e": float(I)})

        nest.Simulate(5000.0)

        dSD = nest.GetStatus(spike_detector, keys='events')[0]
        evs = dSD["senders"]
        ts_s = dSD["times"]

        end = len(ts_s)

        #end = numpy.add(start, numpy.float64(5000.0))

        #pylab.figure("Spike Raster I: " + str(I) + ", J: " + str(J))
        #pylab.plot(ts_s, evs, "b.")
        #pylab.xlim(start, end)
        #pylab.title("Spike Raster I: " + str(I) + ", J: " + str(J))
        #pylab.xlabel("Time: ms")
        #pylab.ylabel("Neuron ID")

        #pylab.savefig("Spike Raster I: " + str(I) + ", J: " + str(J) + ".png")

        list_spikes = ts_s[start:end - 1]
        count = len(list_spikes)
        average = numpy.divide(numpy.float64(count), numpy.float64(500000.0))
        mean_spike_list.append(average)

        start = end

        #list_values = []

        #for i in range(1, len(analysis_list)):

        #    value = abs(numpy.subtract(numpy.float64(analysis_list[i]),numpy.float64(analysis_list[i-1])))

        #    list_values.append(value)

        #open_file = open(str(I) + "_:_" + str(J) + "_times.json", "w")
        #simplejson.dump(list_values, open_file)
        #open_file.close()

        #numpy.savetxt("Spike_Times_I:_" + str(I) + "_I:_" + str(J) + ".csv", ts_s, delimiter=",")
        #numpy.savetxt("Neuron_ID_I:_" + str(I) + "_I:_" + str(J) + ".csv", evs, delimiter=",")

        #ts_s = ts_s.tolist()
        #evs = evs.tolist()

        #open_file = open("Spike_Times_I:_" + str(I) + "_I:_" + str(J) + ".json", "w")
        #simplejson.dump(ts_s, open_file)
        #open_file.close()

        #open_file = open("Neuron_ID_I:_" + str(I) + "_I:_" + str(J) + ".json", "w")
        #simplejson.dump(evs, open_file)
        #open_file.close()

        nest.ResumeSimulation()

    #numpy.savetxt("Neuron_ID_J_" + str(J) + "_values.csv", evs, delimiter=",")
    #numpy.savetxt("Neuron_Spikes_J_" + str(J) + "_values.csv", ts_s, delimiter=",")

    spike_list.append(mean_spike_list)

    nest.ResetKernel()

list_average_spikes = numpy.asarray(spike_list)
numpy.savetxt("average_mean_spike_list.csv", list_average_spikes, delimiter=",")

plt.figure("Mean Spike Rate")
heatmap = plt.imshow(list_average_spikes, cmap='plasma', interpolation='nearest', aspect='auto')
plt.xticks(range(0,12000,2000),range(500,-100,-100))
plt.yticks(range(0,11,1),range(100,-10,-10))
plt.ylabel("Synaptic Weight: J")
plt.xlabel("External Current: I")
cbr = plt.colorbar(heatmap)
cbr.set_label("Mean Spike Rate")
plt.title("Mean Spike Rate, A: 70.0")
plt.savefig("Mean_Spike_Rate.png")


plt.show()
