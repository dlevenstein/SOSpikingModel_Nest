import csv
import matplotlib.pyplot as plt
import numpy
import pylab

csv_file = open("red_line_data.csv", "rb")
red_data = csv.reader(csv_file, delimiter=",")

csv_file = open("blue_line_data.csv", "rb")
blue_data = csv.reader(csv_file, delimiter=",")

red_list = []
blue_list = []

for r_line in red_data:

    r_line_data = []

    for r_l in r_line:

        r_line_data.append(numpy.float64(r_l))

    red_list.append(r_line_data)

for b_line in blue_data:

    b_line_data = []

    for b_l in b_line:

        b_line_data.append(25500.0-numpy.float64(b_l))

    blue_list.append(b_line_data)

blue_list = numpy.asarray(blue_list)
red_list = numpy.asarray(red_list)
#blue_list = numpy.fliplr(blue_list)


pylab.figure("Bistable Plot")
pylab.title("Bistable Plot")
pylab.plot(red_list, range(0,110,10), "r")
pylab.plot(blue_list, range(0,110,10), "b")
pylab.xlabel("External Current (pA)")
pylab.ylabel("Synaptic Weight")
pylab.xticks(range(0,30000,5000), range(0,600,100))
pylab.savefig("bistable_plot.png")

pylab.rcParams.update({'font.size': 30})
pylab.show()
