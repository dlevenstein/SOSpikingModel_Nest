import numpy
import simplejson
open_file = open("heat_map_values_I_e_Ke.json", "r")
values = simplejson.load(open_file)
open_file.close()


a = numpy.asarray(values)
numpy.savetxt("I_e_Ke_increase.csv", a, delimiter=",")
