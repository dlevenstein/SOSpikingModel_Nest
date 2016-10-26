import simplejson

file_1 = open("decreasing_heat_map_values_I_e_Ke.json", "r")
file_2 = open("decreasing_heat_map_values_I_e_Je.json", "r")
file_3 = open("heat_map_values_I_e_Je.json", "r")
file_4 = open("heat_map_values_I_e_Ke.json", "r")

decreasing_heat_map_values_I_e_Ke = simplejson.load(file_1)
decreasing_heat_map_values_I_e_Je = simplejson.load(file_2)
heat_map_values_I_e_Je = simplejson.load(file_3)
heat_map_values_I_e_Ke = simplejson.load(file_4)

import numpy as np

a = np.asarray(decreasing_heat_map_values_I_e_Ke)
b = np.asarray(decreasing_heat_map_values_I_e_Je)
c = np.asarray(heat_map_values_I_e_Je)
d = np.asarray(heat_map_values_I_e_Ke)

np.savetxt("decreasing_heat_map_values_I_e_Ke.csv", a, delimiter=",")
np.savetxt("decreasing_heat_map_values_I_e_Je.csv", b, delimiter=",")
np.savetxt("heat_map_values_I_e_Je.csv", c, delimiter=",")
np.savetxt("heat_map_values_I_e_Ke.csv", d, delimiter=",")
