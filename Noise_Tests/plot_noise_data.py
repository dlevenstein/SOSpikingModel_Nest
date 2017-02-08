import csv
import matplotlib.pyplot as plt
import numpy

csv_file = open("noise_data.csv", "rb")
data = csv.reader(csv_file, delimiter=",")

mean_spike_list = []

for line in data:

    line_data = []

    for l in line:

        line_data.append(numpy.float64(l))

    mean_spike_list.append(line_data)

print(mean_spike_list)

analysis_list = numpy.asarray(mean_spike_list)
analysis_list = numpy.rot90(analysis_list)

plt.figure("Noise Analysis")
heatmap = plt.imshow(analysis_list, cmap='plasma', interpolation='nearest', aspect='auto')
plt.xticks(range(0,60,10),range(500,-100,-100))
plt.yticks(range(50,-10,-10),range(0,600,100))
plt.ylabel("External Current: I (pA)")
plt.xlabel("Noise: N (standard deviation: pA)")
cbr = plt.colorbar(heatmap)
cbr.set_label("Neurons Spikes per sec)")
plt.title("Noise Analysis")
plt.savefig("noise_analysis.png")
plt.rcParams.update({'font.size': 30})
plt.gca().invert_xaxis()

plt.show()
