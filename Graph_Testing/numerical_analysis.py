import simplejson
import numpy
import matplotlib.pyplot as plt

open_file = open("distribution_data.json", "r")
data = simplejson.load(open_file)
open_file.close()

numerical_tensor = []
analysis_tensor = []

count = 0

for matrix in data:
    numerical_matrix = []
    analysis_matrix = []

    for line in matrix:
        numerical_list = []
        analysis_list = []

        count += 1

        for i in range(1,len(line)):
            numerical_value = line[i] - line[i-1]
            numerical_list.append(numerical_value)

        numerical_list.sort()
        #print(numerical_list[-10:])
        #print(numerical_list[-10:])
        line = numpy.asarray(line)
        #print()
        if len(line[(line >= numpy.std(numerical_list))]) == 0:
            line.sort()
            analysis_list.append(line[-10:])
        else:
            #print(line[(line >= numpy.std(numerical_list))])
            analysis_list.append(line[(line >= numpy.std(numerical_list))])

            plt.figure(str(count))
            plt.title("State Analysis")

            n, bins, patches = plt.hist(analysis_list, 50, lw=3, fc=(0, 0, 0, 0.5))

            plt.xlabel("Time, ms")
            plt.ylabel("Number of DOWN states that last for t ms")

            plt.show()

        numerical_matrix.append(numerical_list)
        analysis_matrix.append(numerical_list)

    numerical_tensor.append(numerical_matrix)
    analysis_tensor.append(analysis_matrix)
#print(analysis_tensor)
#plt.show
