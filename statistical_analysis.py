import simplejson
import pylab
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.mlab as mlab
import math

plt.figure("Spike Rate Analysis")
plt.title("Spike Rate Analysis Normal Curve")

for I in range(390,470, 10):

    open_file = open("spike_analysis_" + str(I) + ".json", "r")
    final_list = simplejson.load(open_file)

    UP_mean = np.mean(final_list[0])
    UP_sd = np.std(final_list[0])

    DOWN_mean = np.mean(final_list[1])
    DOWN_sd = np.std(final_list[1])

    print(UP_mean, UP_sd, DOWN_mean, DOWN_sd)

    mu = UP_mean
    variance = UP_sd
    sigma = math.sqrt(variance)
    x = np.linspace(-10, 200, 100)
    plt.plot(x,mlab.normpdf(x, mu, sigma), label='UP ' + str(I))
    #plt.legend()

    mu = DOWN_mean
    variance = DOWN_sd
    sigma = math.sqrt(variance)
    x = np.linspace(-10, 200, 100)
    plt.plot(x,mlab.normpdf(x, mu, sigma), label='DOWN ' + str(I))
    #plt.legend()


plt.show()
