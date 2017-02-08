import neuron_functions_0
import nest
import pylab

for J in [10,70]:

    nest.SetKernelStatus({"local_num_threads":8})
    UP_data = neuron_functions_0.neuron_population(range(0,510,10), J, 0, 0, 500)
    nest.ResetKernel()
    nest.SetKernelStatus({"local_num_threads":8})
    DOWN_data = neuron_functions_0.neuron_population(range(500,-10,-10), J, 0, 0, 500)
    nest.ResetKernel()

    pylab.figure("Weight " + str(J))
    pylab.subplot2grid((3,3),(0,0), colspan=3)
    pylab.plot(UP_data[0], UP_data[1], "r.")
    pylab.xlim(0,25000)
    pylab.gca().invert_xaxis()
    pylab.xticks()
    #pylab.title("Increasing Current")
    pylab.xlabel("Time ms")
    pylab.ylabel("Neuron label")

    pylab.subplot2grid((3,3),(1,0), colspan=3)
    pylab.plot(DOWN_data[0], DOWN_data[1], "b.")
    pylab.xlim(0,25000)
    #pylab.title("Decreasing Current")
    pylab.xlabel("Time ms")
    pylab.ylabel("Neuron label")

pylab.show()
