import csv
import pylab
import numpy
spike_times = []

for J in [50]:

    for N in [0]:

        open_file = open("No_adaptation_J_50_spike_values_increasing.csv", "r")
        data = csv.reader(open_file, delimiter=",")


        for line in data:

            data_line = []
            for l in line:
                data_line.append(float(l))

            spike_times.append(data_line)

start = 0.0
end = 0.0
mean_spike_list = []

spike_times = numpy.asarray(spike_times)
#print(spike_times[0])
for d_l in range(0,610,10):
    end += 500.0

    spikes = spike_times[0][(spike_times[0] >= start) & (spike_times[0] < end)]
    print(spikes)
    start = end

    mean_spike_list.append(len(spikes)/(100.0 * 500.0) * 1000.0)


print()
pylab.figure()
pylab.plot(range(0,610,10), mean_spike_list, "r")
pylab.show()
