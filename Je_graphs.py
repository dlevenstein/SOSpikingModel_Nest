import nest
import numpy as np
import simplejson

nest.SetKernelStatus({"local_num_threads": 8})

neuron_population = 1000
simulation_time = 10.0

I_e = 250.0

mean_rate_Je = []
mean_rate_list = []

Je_parameters = np.arange(0,10,2)
dict_parameters_exc = {"E_L": -70.0, "C_m": 250.0, "tau_m": 20.0, "t_ref": 2.0, "V_th": -55.0, "V_reset": -70.0, "tau_syn":  2.0, "I_e": I_e}

epop = nest.Create("iaf_neuron", neuron_population)
multimeter = nest.Create("multimeter")

nest.SetStatus(multimeter, {"withtime":True, "record_from":["V_m"]})
nest.SetStatus(epop, dict_parameters_exc)

for neuron in epop:
    nest.SetStatus([neuron], {"V_m": dict_parameters_exc["E_L"]+(dict_parameters_exc["V_th"]-dict_parameters_exc["E_L"])*np.random.rand()})

nest.Connect(multimeter, [epop[0]])
nest.Connect(multimeter, [epop[1]])
nest.Connect(multimeter, [epop[2]])


spikedetector_exc = nest.Create("spike_detector", params={"withgid": True, "withtime": True})

for neuron_exc in epop:
    nest.Connect([neuron_exc], spikedetector_exc)

multimeter_times = []
spike_raster = []
multimeter_values = []
spike_times = []

for i in range(2,12,2):

    Je = float(i)

    d = 1.0
    Ke = 20

    conn_dict_ex = {"rule": "fixed_indegree", "indegree": Ke}
    syn_dict_ex = {"delay": d, "weight": Je}

    nest.Connect(epop, epop, conn_dict_ex, syn_dict_ex)
    nest.Simulate(simulation_time)

    dSD = nest.GetStatus(spikedetector_exc, keys='events')[0]
    evs = dSD["senders"]
    ts = dSD["times"]

    dmm = nest.GetStatus(multimeter)[0]
    Vms_m = dmm["events"]["V_m"]
    ts_m = dmm["events"]["times"]


    multimeter_times.append(ts_m)
    spike_raster.append(evs)
    spike_times.append(ts)
    multimeter_values.append(Vms_m)

    total = 0.0

    for i in range(len(evs)):

        total += evs[i]

    mean_rate = total / (neuron_population * simulation_time)

    mean_rate_list.append(mean_rate)

import plotly.tools as tls
tls.set_credentials_file(username='jmg1030', api_key='2c0f8cg9h4')

import plotly.plotly as py
import plotly.graph_objs as go

# Create random data with numpy
import numpy as np

print(spike_raster[0])
print(spike_times[0])
k = 0
for i in Je_parameters:

    trace1 = go.Scatter(
        x = spike_raster[k],
        y = spike_times[k],
        mode = 'markers',
        name = 'markers'
    )

    py.iplot(trace1, filename='Spike Raster Je: ')

    k += 1

    trace2 = go.Scatter(
        x = multimfeter_times[k],
        y = multimeter_values[k],
        mode = 'lines',
        name = 'lines'
    )

    py.iplot(trace2, filename='V_m Je: ')

    k += 1
