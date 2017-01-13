import simplejson
import numpy
import matplotlib.pyplot as plt

UP_mean = []
DOWN_mean = []
UP_std = []
DOWN_std = []

for I in range(500, -10, -10):

    D_M = []
    U_M = []
    D_S = []
    U_S = []

    for J in range(100, -10, -10):

        open_file = open(str(I) + " : " + str(J) + "_times.json", "r")
        data = simplejson.load(open_file)
        open_file.close()

        time_data = []
        for t_0 in data:
            if t_0 < 4000.0:
                time_data.append(t_0)

        mean = numpy.mean(time_data)
        std = numpy.std(time_data)

        DOWN = []
        UP = []

        up_time = 0.0

        print(mean * std)

        for t in time_data:
            if t > mean * std:
                DOWN.append(t)

        down_mean = numpy.mean(DOWN)

        for t_2 in time_data:
            if t_2 < down_mean:
                up_time += t_2
            else:
                UP.append(t_2)
                up_time = 0.0

        plt.figure("UP_State, External Current: " + str(I) + " Internal Current: " + str(J))
        plt.title("State Analysis")

        n, bins, patches = plt.hist(UP, 50, lw=3, fc=(0, 0, 0, 0.5))

        plt.xlabel("Time, ms")
        plt.ylabel("Number of DOWN states that last for t ms")

        plt.savefig("DOWN State Analysis I: " + str(I) + " J: " + str(J) + ".png")


        plt.figure("DOWN_State, External Current: " + str(I) + " Internal Current: " + str(J))
        plt.title("State Analysis")

        n, bins, patches = plt.hist(DOWN, 50, lw=3, fc=(0, 0, 0, 0.5))

        plt.xlabel("Time, ms")
        plt.ylabel("Number of DOWN states that last for t ms")

        plt.savefig("UP State Analysis I: " + str(I) + " J: " + str(J) + ".png")

"""        down_m = numpy.mean(UP)
        up_m = numpy.mean(DOWN)
        down_s = numpy.std(UP)
        up_s = numpy.std(DOWN)

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

open_file = open("UP_mean_numerical_values.json", "w")
simplejson.dump(UP_mean, open_file)
open_file.close()

open_file = open("DOWN_mean_numerical_values.json", "w")
simplejson.dump(DOWN_mean, open_file)
open_file.close()

open_file = open("UP_std_numerical_values.json", "w")
simplejson.dump(UP_std, open_file)
open_file.close()

open_file = open("DOWN_std_numerical_values.json", "w")
simplejson.dump(DOWN_std, open_file)
open_file.close()"""
