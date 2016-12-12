import simplejson
import pylab
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.mlab as mlab
import math
import scipy.stats as ss


for I in range(390,470, 10):

    open_file = open("spike_analysis_" + str(I) + ".json", "r")
    final_list = simplejson.load(open_file)

    #print(final_list)

    UP_state = final_list[0]
    DOWN_state = final_list[1]

    #UP_state = UP_state.sort()
    #DOWN_state = DOWN_state.sort()


    plt.figure("UP State External Current " + str(I))
    plt.title("UP State Analysis")

    """UP_mean = np.mean(final_list[0])
    UP_sd = np.std(final_list[0])
    mu = UP_mean * 1000
    variance = UP_sd * 1000
    sigma = math.sqrt(variance)"""

    """x = np.linspace(0, 250, 100)
    plt.plot(x,mlab.normpdf(x, mu, sigma), label='UP ' + str(I))
    plt.legend()"""

    n, bins, patches = plt.hist(UP_state, 50, lw=3, fc=(0, 0, 0, 0.5))
    plt.xlim(0,25)
    plt.xlabel("Time, ms")
    plt.ylabel("Number of UP states that last for x ms")

    plt.savefig("UP State External Current " + str(I))



    """UP_mean = np.mean(final_list[0])
    UP_sd = np.std(final_list[0])


    DOWN_mean = np.mean(final_list[1])
    DOWN_sd = np.std(final_list[1])




    mu = UP_mean
    variance = UP_sd
    sigma = math.sqrt(variance)
    #x = np.linspace(ss.gamma.ppf(0.01, UP_state), ss.gamma.ppf(0.99, UP_state), 100)
    #plt.plot(x,ss.gamma(x,mu,sigma), label='UP ' + str(400))
    #plt.legend()
    #print(ss.gamma(x,mu,sigma))

    mu = DOWN_mean
    variance = DOWN_sd
    sigma = math.sqrt(variance)
    x = np.linspace(-10, 200, 100)
    #plt.plot(x,mlab.normpdf(x, mu, sigma), label='DOWN ' + str(I))
    #plt.legend()"""

plt.show()
