import numpy as np
open_file = open("automate_data.sh", "w")

Je_parameters = np.arange(0,10,0.2)

for j in Je_parameters:

    open_file.write("python heat_map_I_e_Je.py " +  str(j) + "\n" +  "wait" + "\n")
    open_file.write("python decreasing_heat_map_I_e_Je.py " +  str(j) + "\n" +  "wait" + "\n")

for k in range(1,21):

    open_file.write("python heat_map_I_e_Ke.py " +  str(k) + "\n" +  "wait" + "\n")
    open_file.write("python decreasing_heat_map_I_e_Ke.py " +  str(k) + "\n" +  "wait" + "\n")

open_file.close()
