import nest
import pylab
import numpy
import random
import raster_plot_modified
import matplotlib.pyplot as plt

"""V_m        double - Membrane potential in mV
E_L        double - Resting membrane potential in mV.
C_m        double - Capacity of the membrane in pF
tau_m      double - Membrane time constant in ms.
t_ref      double - Duration of refractory period in ms.
V_th       double - Spike threshold in mV.
V_reset    double - Reset potential of the membrane in mV.
tau_syn    double - Rise time of the excitatory synaptic alpha function in ms.
I_e        double - Constant external input current in pA.

C_( 250.0 )             // pF
Tau_( 10.0 )            // ms
tau_syn_( 2.0 )         // ms
TauR_( 2.0 )            // ms
U0_( -70.0 )            // mV
V_reset_( -70.0 - U0_ ) // mV, rel to U0_
Theta_( -55.0 - U0_ )   // mV, rel to U0_
I_e_( 0.0 )             // pA"""

def inh_neuron_parameters(inh_dictionary, neuron_population):

    nest.CopyModel("iaf_neuron", "inh_iaf_neuron", params=inh_dictionary)

    ipop = nest.Create("inh_iaf_neuron", neuron_population)

    for neuron in ipop:
        nest.SetStatus([neuron], {"V_m": inh_dictionary["E_L"]+(inh_dictionary["V_th"]-inh_dictionary["E_L"])*numpy.random.rand()})

    return ipop

def exc_neuron_parameters(exc_dictionary, neuron_population):

    nest.CopyModel("iaf_neuron", "exc_iaf_neuron", params=exc_dictionary)

    epop = nest.Create("exc_iaf_neuron", neuron_population)

    for neuron in epop:
        nest.SetStatus([neuron], {"V_m": exc_dictionary["E_L"]+(exc_dictionary["V_th"]-exc_dictionary["E_L"])*numpy.random.rand()})

    return epop

def random_neuron_generator(epop, ipop, simulation_time, d, Je, Ke, Ji, Ki, inh_dictionary, exc_dictionary):

    conn_dict_ex = {"rule": "fixed_indegree", "indegree": Ke}
    conn_dict_in = {"rule": "fixed_indegree", "indegree": Ki}
    syn_dict_ex = {"delay": d, "weight": Je}
    syn_dict_in = {"delay": d, "weight": Ji}
    nest.Connect(epop, ipop, conn_dict_ex, syn_dict_ex)
    nest.Connect(ipop, epop, conn_dict_in, syn_dict_in)
    nest.Connect(epop, epop, conn_dict_ex, syn_dict_ex)
    nest.Connect(ipop, ipop, conn_dict_in, syn_dict_in)

    multimeter_exc = nest.Create("multimeter")
    multimeter_inh = nest.Create("multimeter")

    nest.SetStatus(multimeter_exc, {"withtime":True, "record_from":["V_m"]})
    nest.SetStatus(multimeter_inh, {"withtime":True, "record_from":["V_m"]})

    multimeter_small = nest.Create("multimeter")
    multimeter_large = nest.Create("multimeter")

    nest.SetStatus(multimeter_small, {"withtime":True, "record_from":["V_m"]})
    nest.SetStatus(multimeter_large, {"withtime":True, "record_from":["V_m"]})

    multimeter_exc_0 = nest.Create("multimeter")
    multimeter_exc_1 = nest.Create("multimeter")
    multimeter_exc_2 = nest.Create("multimeter")

    multimeter_inh_0 = nest.Create("multimeter")
    multimeter_inh_1 = nest.Create("multimeter")
    multimeter_inh_2 = nest.Create("multimeter")

    nest.SetStatus(multimeter_exc_0, {"withtime":True, "record_from":["V_m"]})
    nest.SetStatus(multimeter_exc_1, {"withtime":True, "record_from":["V_m"]})
    nest.SetStatus(multimeter_exc_2, {"withtime":True, "record_from":["V_m"]})

    nest.SetStatus(multimeter_inh_0, {"withtime":True, "record_from":["V_m"]})
    nest.SetStatus(multimeter_inh_1, {"withtime":True, "record_from":["V_m"]})
    nest.SetStatus(multimeter_inh_2, {"withtime":True, "record_from":["V_m"]})

    nest.Connect(multimeter_exc, epop[0:2])
    nest.Connect(multimeter_inh, ipop[0:2])

    nest.Connect(multimeter_exc_0, [epop[0]])
    nest.Connect(multimeter_exc_1, [epop[1]])
    nest.Connect(multimeter_exc_2, [epop[2]])

    nest.Connect(multimeter_inh_0, [ipop[0]])
    nest.Connect(multimeter_inh_1, [ipop[1]])
    nest.Connect(multimeter_inh_2, [ipop[2]])

    nest.Connect(multimeter_small, [epop[0]])
    nest.Connect(multimeter_small, [ipop[0]])

    nest.Connect(multimeter_large, epop)
    nest.Connect(multimeter_large, ipop)

    spikedetector_exc = nest.Create("spike_detector", params={"withgid": True, "withtime": True})
    spikedetector_inh = nest.Create("spike_detector", params={"withgid": True, "withtime": True})

    spikedetector = nest.Create("spike_detector", params={"withgid": True, "withtime": True})

    for neuron_exc in epop:
        nest.Connect([neuron_exc], spikedetector_exc)
        nest.Connect([neuron_exc], spikedetector)
    for neuron_inh in ipop:
        nest.Connect([neuron_inh], spikedetector_inh)
        nest.Connect([neuron_inh], spikedetector)

    nest.Simulate(simulation_time)



    dmm_exc_0 = nest.GetStatus(multimeter_exc_0)[0]
    Vms_exc_0 = dmm_exc_0["events"]["V_m"]
    ts_exc_0 = dmm_exc_0["events"]["times"]

    dmm_exc_1 = nest.GetStatus(multimeter_exc_1)[0]
    Vms_exc_1 = dmm_exc_1["events"]["V_m"]
    ts_exc_1 = dmm_exc_1["events"]["times"]

    dmm_exc_2 = nest.GetStatus(multimeter_exc_2)[0]
    Vms_exc_2 = dmm_exc_2["events"]["V_m"]
    ts_exc_2 = dmm_exc_2["events"]["times"]

    pylab.subplot2grid((3,3),(0,0), colspan=1)
    pylab.plot(ts_exc_0, Vms_exc_0)
    pylab.plot(ts_exc_1, Vms_exc_1)
    pylab.plot(ts_exc_2, Vms_exc_2)
    pylab.title("Excitatory Neurons")

    dmm_inh_0 = nest.GetStatus(multimeter_inh_0)[0]
    Vms_inh_0 = dmm_inh_0["events"]["V_m"]
    ts_inh_0 = dmm_inh_0["events"]["times"]

    dmm_inh_1 = nest.GetStatus(multimeter_inh_1)[0]
    Vms_inh_1 = dmm_inh_1["events"]["V_m"]
    ts_inh_1 = dmm_inh_1["events"]["times"]

    dmm_inh_2 = nest.GetStatus(multimeter_inh_2)[0]
    Vms_inh_2 = dmm_inh_2["events"]["V_m"]
    ts_inh_2 = dmm_inh_2["events"]["times"]

    pylab.subplot2grid((3,3),(0,1), colspan=1)
    pylab.plot(ts_inh_0, Vms_inh_0)
    pylab.plot(ts_inh_1, Vms_inh_1)
    pylab.plot(ts_inh_2, Vms_inh_2)
    pylab.title("Inhibitatory Neurons")

    dSD = nest.GetStatus(spikedetector_exc, keys='events')[0]
    evs = dSD["senders"]
    ts = dSD["times"]
    pylab.subplot2grid((3,3),(1,0), colspan=1)
    pylab.plot(ts, evs, ".")
    pylab.title("Excitatory Neurons")

    dSD = nest.GetStatus(spikedetector_inh, keys='events')[0]
    evs = dSD["senders"]
    ts = dSD["times"]
    pylab.subplot2grid((3,3),(1,1))
    pylab.plot(ts, evs, ".")
    pylab.title("Inhibitatory Neurons")

    dmm_exc = nest.GetStatus(multimeter_exc)[0]
    Vms_exc = dmm_exc["events"]["V_m"]
    ts_exc = dmm_exc["events"]["times"]

    pylab.subplot2grid((3,3),(2,0), colspan=1)
    pylab.plot(ts_exc, Vms_exc)
    pylab.title("Excitatory Neurons")

    dmm_inh = nest.GetStatus(multimeter_inh)[0]
    Vms_inh = dmm_inh["events"]["V_m"]
    ts_inh = dmm_inh["events"]["times"]

    pylab.subplot2grid((3,3),(2,1), colspan=1)
    pylab.plot(ts_inh, Vms_inh)
    pylab.title("Inhibitatory Neurons")

    pylab.subplot2grid((3,3),(0,2), rowspan=3)

    i = 0
    pylab.text(0.1, 0.95,"Inhibitatory",horizontalalignment='left',verticalalignment='center',)
    pylab.text(0.5, 0.95,"Excitatory",horizontalalignment='left',verticalalignment='center',)

    for keys in inh_dictionary.items():

        pylab.text(0.1, 0.9 - i,keys,horizontalalignment='left',verticalalignment='center',)
        i += 0.05

    i = 0
    for keys in exc_dictionary.items():

        pylab.text(0.5, 0.9 - i,keys,horizontalalignment='left',verticalalignment='center',)
        i += 0.05

    pylab.text(0.1, 0.9 - i,"Synaptic Connections",horizontalalignment='left',verticalalignment='center',)
    i += 0.05

    pylab.text(0.1, 0.9 - i,"d: " + str(d),horizontalalignment='left',verticalalignment='center',)
    i += 0.05

    pylab.text(0.1, 0.9 - i,"Je: " + str(Je),horizontalalignment='left',verticalalignment='center',)
    i += 0.05

    pylab.text(0.1, 0.9 - i,"Ke: " + str(Ke),horizontalalignment='left',verticalalignment='center',)
    i += 0.05

    pylab.text(0.1, 0.9 - i,"Ji: " + str(Ji),horizontalalignment='left',verticalalignment='center',)
    i += 0.05

    pylab.text(0.1, 0.9 - i,"Ki: " + str(Ki),horizontalalignment='left',verticalalignment='center',)
    i += 0.05


    raster_plot_modified.from_device(spikedetector, hist=True)

    dmm_exc = nest.GetStatus(multimeter_small)[0]
    Vms_exc = dmm_exc["events"]["V_m"]
    ts_exc = dmm_exc["events"]["times"]

    pylab.subplot2grid((3,3),(0,0), colspan=3)
    pylab.plot(ts_exc, Vms_exc)
    pylab.title("Neuron Population")

    dSD = nest.GetStatus(spikedetector, keys='events')[0]
    evs = dSD["senders"]
    ts = dSD["times"]
    pylab.subplot2grid((3,3),(1,0), colspan=3)
    pylab.plot(ts, evs, ".")

    pylab.show()
