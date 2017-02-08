import csv
import matplotlib.pyplot as plt
import numpy

csv_file = open("noise_data_UP.csv", "rb")
data = csv.reader(csv_file, delimiter=",")

mean_spike_list = []

for line in data:

    line_data = []

    for l in line:

        line_data.append(numpy.float64(l))

    mean_spike_list.append(line_data)

print(mean_spike_list)

analysis_list = numpy.asarray(mean_spike_list)
#numpy.fliplr(analysis_list)


plt.figure("Mean Spike Rate, External Current Decrease")
heatmap = plt.imshow(analysis_list, cmap='plasma', interpolation='nearest', aspect='auto')
plt.xticks(range(0,60,10),range(0,600,100))
plt.yticks(range(0,60,10),range(0,600,100))
plt.xlabel("External Current: I (pA)")
plt.ylabel("Noise (pA)")
cbr = plt.colorbar(heatmap)
cbr.set_label("Neuron Spikes per sec")
plt.title("Mean Spike Rate, External Current Decrease")
#plt.gca().invert_xaxis()
plt.gca().invert_yaxis()
plt.savefig("noise_figure.png")

plt.rcParams.update({'font.size': 30})

plt.show()
