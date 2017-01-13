import simplejson
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

numpy.savetxt("UP_mean_numerical_values.csv", UP_mean, delimiter=",")
numpy.savetxt("DOWN_mean_numerical_values.csv", DOWN_mean, delimiter=",")
numpy.savetxt("UP_std_numerical_values.csv", UP_std, delimiter=",")
numpy.savetxt("DOWN_std_numerical_values.csv", DOWN_std, delimiter=",")
