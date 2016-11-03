import nest
import numpy as np
import simplejson

open_file = open("small_J_values.json", "r")
rate_list_small = open_file.split("\n")
open_file.close()

total_list_small = []
total_list_large = []

for r in rate_list_small:
    list_0 = r.split(",")
    for l in list_0:
        total_list_small.append(float(l))

open_file = open("large_J_values.json", "r")
rate_list_large = open_file.split("\n")
open_file.close()

for r in rate_list_large:
    list_0 = r.split(",")
    for l in list_0:
        total_list_large.append(float(l))


import numpy as NP

#mean_rate_list.remove(mean_rate_list[0])

x_list = [500,250,0]
y_list = []

J_parameters_small = np.arange(0,10,0.2)
J_parameters_large = np.arange(0,100,2)

for j in J_parameters_small:

    y_list.append(j)

import plotly.tools as tls
tls.set_credentials_file(username='jmg1030', api_key='2c0f8cg9h4')

import plotly.plotly as py
import plotly.graph_objs as go

data = [
    go.Heatmap(
        z=total_list_small,
        x=x_list,
        y=y_list
    )
]
py.iplot(data, filename='Test Small')

y_list = []

for j in J_parameters_large:

    y_list.append(j)

data = [
    go.Heatmap(
        z=total_list_large,
        x=x_list,
        y=y_list
    )
]
py.iplot(data, filename='Test Large')
