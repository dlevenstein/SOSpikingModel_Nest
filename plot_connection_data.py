import csv
import matplotlib.pyplot as plt
import numpy

csv_file = open("inh_exc_data.csv", "rb")
data = csv.reader(csv_file, delimiter=",")

mean_spike_list = []

for line in data:

    line_data = []

    for l in line:

        line_data.append(numpy.float64(l))

    mean_spike_list.append(line_data)

print(mean_spike_list)

mean_spike_list = numpy.asarray(mean_spike_list)

analysis_list = mean_spike_list[:,0:6]
print(mean_spike_list)
print(analysis_list)

plt.figure("Excitatory and Inhibitory Analysis")
heatmap = plt.imshow(analysis_list, cmap='plasma', interpolation='nearest', aspect='auto')
plt.xticks(range(0,11,1),range(0,-110,-10))
plt.yticks(range(10,-1,-1),range(100,-10,-10))
plt.xlim(0,5)
plt.ylabel("Excitatory Connections")
plt.xlabel("Inhibitory Connection")
cbr = plt.colorbar(heatmap)
cbr.set_label("Mean Spike Rate (Neurons Spiking per ms)")
plt.title("Excitatory and Inhibitory Analysis")
plt.savefig("exc_inh_analysis.png")


plt.show()
