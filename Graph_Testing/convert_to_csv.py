import simplejson
import numpy

open_file = open("distribution_data.json", "r")
data = simplejson.load(open_file)
open_file.close()

print(len(data[0]))
data_analyze = data[0][0]
data_analyze.sort()
#print(data_analyze)

data = numpy.asarray(data)

numpy.savetxt("distribution_data.csv", data, delimiter=",")

