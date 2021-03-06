import pylab
import numpy as np

open_file = open("adaptive_decrease.txt", "r")
string = open_file.read()
data_list_decrease = string.split(",")
open_file.close()

open_file = open("adaptive_increase.txt", "r")
string = open_file.read()
data_list_increase = string.split(",")
open_file.close()

data_list_increase.remove(" ")
data_list_decrease.remove(" ")


print(data_list_decrease)
print(data_list_increase)

number_list = []
number_list_increase = []

for d in data_list_decrease:

    number = 510.0 - ((float(d) / 1000.0) * 10.0)
    number_list.append(number)

for d in data_list_increase:
    #print(d)
    number = ((float(d) / 1000.0) * 10.0)

    number_list_increase.append(number)

print(number_list_increase)
print(number_list)

J_parameters_small = np.arange(0,100,2.0)

parameter_list = []

for j in J_parameters_small:
    parameter_list.append(j)

print(len(number_list), len(number_list_increase), len(parameter_list))

#print(number_list_increase)
pylab.figure("External Current vs. Weight Value")

pylab.plot(number_list, parameter_list, "r")
pylab.plot(number_list_increase, parameter_list, "b")
pylab.title("External Current vs. Weight Value")
pylab.xlabel("External Current I_e Value (pA)")
pylab.ylabel("Weight Value J")
pylab.show()
