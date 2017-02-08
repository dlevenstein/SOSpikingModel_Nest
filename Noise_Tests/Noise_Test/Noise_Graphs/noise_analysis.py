import csv
import numpy

matrix_data = []

for J in range(0,110,10):
    for N in [250]:
        csv_file = open("Spike_Raster_Increase_External_J:_" + str(J) + "_N:_" + str(N) + "_simulated_noise_data.csv", "rb")
        #csv_file = open("Spike_Raster_Decrease_External_J:_" + str(J) + "_N:_" + str(N) + "_simulated_noise_data.csv", "rb")
        data = csv.reader(csv_file, delimiter=',')

        for line in data:

            line_data = []

            for number in line:

                line_data.append(numpy.float64(number))

            matrix_data.append(line_data)

matrix_data = numpy.asarray(matrix_data)

#print(matrix_data)
noise_data = []

print(len(matrix_data), len(matrix_data[0]), matrix_data[0][-1], matrix_data[-1][-1])

for vector in matrix_data:

    vector = numpy.asarray(vector)
    vector_data = []

    print(vector[-1])
    for time_zone in range(0,int(vector[-1]) + 1,500):

        count = len(vector[(numpy.float64(vector) > numpy.float64(time_zone)) & (numpy.float64(vector) <= numpy.float64(time_zone) + 500.0)])

        #print(count)

        average = numpy.multiply(numpy.divide(count,numpy.float64(500000.0)),numpy.float64(1000.0))

        vector_data.append(average)

    print(len(vector_data))
    noise_data.append(vector_data)

noise_data = numpy.asarray(noise_data)
#print(noise_data)
