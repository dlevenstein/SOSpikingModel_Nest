import pylab

"""open_file = open("adaptive_increase.txt", "r")
string_inc = open_file.read()
open_file.close()

open_file = open("adaptive_decrease.txt", "r")
string_dec = open_file.read()
open_file.close()

list_inc = string_inc.split(", ")
list_dec = string_dec.split(", ")

list_inc.remove('')
list_dec.remove('')

list_inc = [float(i) / 10.0 for i in list_inc]

list_dec = [(10200.0 - float(i)) / 10.0 for i in list_dec]
"""

open_file = open("b_adaptation_increase.txt", "r")
string_inc = open_file.read()
open_file.close()

open_file = open("b_adaptation_decrease.txt", "r")
string_dec = open_file.read()
open_file.close()

list_inc_a = string_inc.split(", ")
list_dec_a = string_dec.split(", ")

list_inc_a.remove('')
list_dec_a.remove('')


list_inc_a = [float(i) / 10.0 for i in list_inc_a]
list_dec_a = [(10200.0 - float(i)) / 10.0 for i in list_dec_a]

J_list = []


for i in range(0,110,10):

    J_list.append(i)

#print(len(list_inc), len(list_dec), len(J_list))

pylab.figure("Adaptation Threshold vs. External Current, Weight: 70.0")
#pylab.plot(list_inc, J_list, "r", label="Inc_Nonadapting", linewidth=4)
#pylab.plot(list_dec, J_list, "b", label="Dec_Nonadapting", linewidth=4)
pylab.plot(list_inc_a, J_list, "r", label="Inc_Adapting", linewidth=4)
pylab.plot(list_dec_a, J_list, "b", label="Dec_Adapting", linewidth=4)
pylab.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)


pylab.title("Adaptation Threshold vs. External Current")
pylab.xlabel("External Current")
pylab.ylabel("Adaptation Threshold")
pylab.xlim(0,510)

#pylab.gca().invert_xaxis()

pylab.show()
