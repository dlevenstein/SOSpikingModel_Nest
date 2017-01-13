import numpy
import simplejson
import pylab
import matplotlib.pyplot as plt

UP_mean = []
DOWN_mean = []
UP_std = []
DOWN_std = []

for i in range(500,-10,-10):

    D_M = []
    U_M = []
    D_S = []
    U_S = []

    for j in range(100,-10,-10):
        open_file = open("spike_times_I_" + str(i) + "_J_" + str(j) + ".json", "r")
        spike_list = simplejson.load(open_file)
        open_file.close()

        UP_list = []
        DOWN_list = []

        for adaptation in spike_list:
            UP_time = 0.0
            DOWN_time = 0.0
            for spikes in adaptation:
                if float(spikes) > 0.0:
                    UP_time += 5.0
                    if DOWN_time > 5.0:
                        DOWN_list.append(DOWN_time)
                        DOWN_time = 0.0
                else:
                    DOWN_time += 5.0
                    if UP_time > 5.0:
                        UP_list.append(UP_time)
                        UP_time = 0.0

        UP_list_0 = []
        DOWN_list_0 = []

        for down in DOWN_list:

            if DOWN_list.count(down) > 10:
                DOWN_list_0.append(down)

        for up in UP_list:
            if UP_list.count(up) > 10:
                UP_list_0.append(up)

        down_m = numpy.mean(UP_list)
        up_m = numpy.mean(DOWN_list)
        down_s = numpy.std(UP_list)
        up_s = numpy.std(DOWN_list)

        if numpy.isnan(down_m) == True:
            D_M.append(0.0)
        else:
            D_M.append(down_m)

        if numpy.isnan(up_m) == True:
            U_M.append(0.0)

        else:
            U_M.append(up_m)

        if numpy.isnan(down_s) == True:
            D_S.append(0.0)

        else:
            D_S.append(down_s)

        if numpy.isnan(up_s) == True:
            U_S.append(0.0)

        else:
            U_S.append(up_s)

        UP_mean.append(D_M)
        DOWN_mean.append(U_M)
        UP_std.append(D_S)
        DOWN_std.append(U_S)

        plt.figure("UP_State, External Current: " + str(i) + " Internal Current: " + str(j))
        plt.title("State Analysis")

        n, bins, patches = plt.hist(UP_list_0, 50, lw=3, fc=(0, 0, 0, 0.5))

        plt.xlabel("Time, ms")
        plt.ylabel("Number of DOWN states that last for t ms")
        #plt.savefig("UP_State, External Current: " + str(i) + " Internal Current: " + str(j) + ".png")

        plt.figure("DOWN_State, External Current: " + str(i) + " Internal Current: " + str(j))
        plt.title("State Analysis")

        n, bins, patches = plt.hist(DOWN_list_0, 50, lw=3, fc=(0, 0, 0, 0.5))

        plt.xlabel("Time, ms")
        plt.ylabel("Number of DOWN states that last for t ms")
        #plt.savefig("DOWN_State, External Current: " + str(i) + " Internal Current: " + str(j) + ".png")


#open_file = open("UP_mean_numerical_values.json", "w")
#simplejson.dump(UP_mean, open_file)
#open_file.close()

#open_file = open("DOWN_mean_numerical_values.json", "w")
#simplejson.dump(DOWN_mean, open_file)
#open_file.close()

#open_file = open("UP_std_numerical_values.json", "w")
#simplejson.dump(UP_std, open_file)
#open_file.close()

#open_file = open("DOWN_std_numerical_values.json", "w")
#simplejson.dump(DOWN_std, open_file)
#open_file.close()
