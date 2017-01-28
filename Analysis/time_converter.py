import csv
import simplejson
import numpy
import matplotlib.pyplot as plt

csv_file = open("average_mean_spike_list.csv", "rb")
data = csv.reader(csv_file, delimiter=',')

mean_spike_list = []

for line in data:

    line_data = []

    for l in line:

        line_data.append(numpy.float64(l))

    mean_spike_list.append(line_data)

print(mean_spike_list)

analysis_list = numpy.asarray(mean_spike_list)

print(analysis_list)
plt.figure("Mean Spike Rate")
heatmap = plt.imshow(analysis_list, cmap='plasma', interpolation='nearest', aspect='auto')
plt.xticks(range(0,60,10),range(500,-100,-100))
plt.yticks(range(0,25,5),range(0,125,25))
plt.ylabel("Synaptic Weight: J")
plt.xlabel("External Current: I")
cbr = plt.colorbar(heatmap)
cbr.set_label("Mean Spike Rate")
plt.title("Mean Spike Rate, Adaptation: 70.0, External Decreasing")
plt.savefig("Mean_Spike_Rate.png")


plt.show()
