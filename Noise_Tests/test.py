import nest
import pylab
import neuron_functions

data = neuron_functions.neuron_population([500], 70, 0, 100, 500)

dSD = nest.GetStatus(data[0], keys='events')[0]
evs = dSD["senders"]
ts_s = dSD["times"]

pylab.figure()
pylab.plot(ts_s, evs, "b.")
pylab.show()
