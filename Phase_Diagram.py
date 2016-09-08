from scipy.integrate import odeint
import numpy
import matplotlib as mpl

def neuronal_equation(state,t):
    r = state[0]
    a = state[1]

    #parameters
    F = 10.0
    w = 10.0
    b = 10.0
    I = 10.0
    gamma = 10.0
    tau = 10.0
    A_infty = 10.0

    dot_r = -r + F * (w*r - b*a + I + gamma)
    dot_a = (-a + A_infty * (r)) / tau

    return [dot_r, dot_a]

state0 = [2.0,3.0]
t = numpy.arange(0.0, 30.0, 0.01)

state = odeint(neuronal_equation, state0, t)

# do some fancy 3D plotting
from mpl_toolkits.mplot3d import Axes3D
fig = mpl.figure()
ax = fig.gca(projection='3d')
ax.plot(state[:,0],state[:,1])
ax.set_xlabel('r')
ax.set_ylabel('a')
ax.set_zlabel('z')
show()
