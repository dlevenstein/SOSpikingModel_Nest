import numpy
import csv

spike_rate = []

noise_data = []
for N in range(0,520,20):

    csv_file = open("noise_data_" + str(N) + ".csv", "rb")
    data = csv.reader(csv_file, delimiter=",")

    noise_line = []
    for d in data:
        noise_line.append(d)

    noise_data.append(noise_line)

print(noise_data)
spike_line = []

for t_zone in range(start, end, 5):

    spikes = data[(data >= t_zone) & (data < t_zone + 5)]

    spike_line.append(spikes)

spike_rate.append(spikes)

print(spike_rate)

spike_rate = numpy.asarray(spike_rate)

"""plt.figure("Noise and Mean Spike Rate")
heatmap = plt.imshow(spike_rate, cmap='plasma', interpolation='nearest', aspect='auto')
#plt.xticks(range(0,60,10),range(500,-100,-100))
#plt.yticks(range(0,25,5),range(0,125,25))
#plt.ylabel("Synaptic Weight: J")
#plt.xlabel("External Current: I")
cbr = plt.colorbar(heatmap)
cbr.set_label("Mean Spike Rate")
plt.title("Mean Spike Rate, Adaptation: 70.0, External Decreasing")
plt.savefig("Mean_Spike_Rate.png")


plt.show()"""
