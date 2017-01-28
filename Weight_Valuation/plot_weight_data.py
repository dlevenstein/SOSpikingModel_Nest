import csv
import matplotlib.pyplot as plt
import numpy

csv_file = open("weight_data_decrease.csv", "rb")
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


plt.figure("Internal Weight Analysis External Decreasing")
heatmap = plt.imshow(analysis_list, cmap='plasma', interpolation='nearest', aspect='auto')
plt.xticks(range(0,60,10),range(0,600,100))
plt.yticks(range(0,11,1),range(0,110,10))
plt.ylabel("External Current: I (pA)")
plt.xlabel("Internal Current: J")
cbr = plt.colorbar(heatmap)
cbr.set_label("Mean Spike Rate (Neurons Spiking per sec)")
plt.title("Internal Weight Analysis External Decreasing")
#plt.gca().invert_xaxis()
plt.savefig("weight_analysis_external_decrease.png")


plt.show()
