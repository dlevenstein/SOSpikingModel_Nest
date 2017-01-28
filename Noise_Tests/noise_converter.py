import csv
import pylab

spike_times = []
for J in [10,50]:

    for N in [0,250,500]:

        open_file = open("J:_" + str(J) + "_N:_" + str(N) + "_simulated_noise_data.csv", "r")
        data = csv.reader(open_file, delimiter=",")

        mean_spike_list = []
        for line in data:

            for l in line:
                print(l)
                mean_spike_list.append(l)

        spike_times.append(mean_spike_list)

print(spike_times)
