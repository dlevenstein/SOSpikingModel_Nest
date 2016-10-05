import plotly.plotly as py
import plotly.graph_objs as go
import simplejson
import plotly.tools as tls
tls.set_credentials_file(username='jmg1030', api_key='2c0f8cg9h4')

open_file = open("heat_map_values_I_e_Je.json", "r")
values = simplejson.load(open_file)

# Create random data with numpy
import numpy as np

N = 500
random_x = np.arange(0,500,10)
random_y = np.array(values[0])

# Create a trace
trace = go.Scatter(
    x = random_x,
    y = random_y
)

data = [trace]

# Plot and embed in ipython notebook!
py.iplot(data, filename='basic-line')

# or plot with: plot_url = py.plot(data, filename='basic-line')
