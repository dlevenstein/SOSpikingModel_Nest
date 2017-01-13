import simplejson
import matplotlib.pyplot as plt
import numpy

open_file = open("UP_mean_numerical_values.json", "r")
UP_mean = simplejson.load(open_file)
open_file.close()

open_file = open("DOWN_mean_numerical_values.json", "r")
DOWN_mean = simplejson.load(open_file)
open_file.close()

open_file = open("UP_std_numerical_values.json", "r")
UP_std = simplejson.load(open_file)
open_file.close()

open_file = open("DOWN_std_numerical_values.json", "r")
DOWN_std = simplejson.load(open_file)
open_file.close()

UP_mean = numpy.asarray(UP_mean)
DOWN_mean = numpy.asarray(DOWN_mean)
UP_std = numpy.asarray(UP_std)
DOWN_std = numpy.asarray(DOWN_std)

print(UP_mean)
print(DOWN_mean)
print(UP_std)
print(DOWN_std)


plt.figure("DOWN Mean")
heatmap = plt.imshow(DOWN_mean, cmap='plasma', interpolation='nearest', aspect='auto')
plt.xticks(range(0,11,1),range(100, -10, -10))
plt.yticks(range(500,-100, -100),range(0,600,100))
plt.xlabel("Synaptic Weight: J")
plt.ylabel("External Current: I")
cbr = plt.colorbar(heatmap)
cbr.set_label("Mean Time Length, ms")
plt.title("DOWN State Mean Heatmap")

plt.figure("UP Mean")
plt.imshow(UP_mean, cmap='plasma', interpolation='nearest', aspect='auto')
plt.xticks(range(0,11,1),range(100, -10, -10))
plt.yticks(range(500,-100, -100),range(0,600,100))
plt.xlabel("Synaptic Weight: J")
plt.ylabel("External Current: I")
cbr = plt.colorbar(heatmap)
cbr.set_label("Mean Time Length, ms")
plt.title("UP State Mean Heatmap")



plt.figure("DOWN Std")
plt.imshow(DOWN_std, cmap='plasma', interpolation='nearest', aspect='auto')
plt.xticks(range(0,11,1),range(100, -10, -10))
plt.yticks(range(500,-100, -100),range(0,600,100))
plt.xlabel("Synaptic Weight: J")
plt.ylabel("External Current: I")
cbr = plt.colorbar(heatmap)
cbr.set_label("Std Time Length, ms")
plt.title("DOWN State Std Heatmap")



plt.figure("UP std")
plt.imshow(UP_std, cmap='plasma', interpolation='nearest', aspect='auto')
plt.xticks(range(0,11,1),range(100, -10, -10))
plt.yticks(range(500,-100, -100),range(0,600,100))
plt.xlabel("Synaptic Weight: J")
plt.ylabel("External Current: I")
cbr = plt.colorbar(heatmap)
cbr.set_label("Std Time Length, ms")
plt.title("UP State Std Heatmap")


plt.show()
