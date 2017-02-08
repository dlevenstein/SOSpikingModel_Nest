import csv
import numpy

csv_file = open("noise_data_" + str(N) + ".csv", "rb")
data = csv.reader(csv_file, delimiter=",")

matrix_data = []

for line in data:

    line_data = []

    for number in line:

        line_data.append(numpy.float64(number))

    matrix_data.append(line_data)

noise_data = []

for vector in matrix_data:

    vector_data = []

    for time_zone in range(0,25000,500):

        count = len(vector[(numpy.float64(vector) > numpy.float64(time_zone)) & (numpy.float64(vector) <= numpy.add(numpy.float64(time_zone), numpy.float64(500.0)))])

        average = numpy.multiply(numpy.divide(count,numpy.float64(500000.0)),numpy.float64(1000.0))

        vector_data.append(average)

    noise_data.append(vector_data)
