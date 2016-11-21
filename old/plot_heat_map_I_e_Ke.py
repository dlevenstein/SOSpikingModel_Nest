import nest
import numpy as np
import simplejson

open_file = open("heat_map_values_I_e_Ke.json", "r")
rate_list = simplejson.load(open_file)
open_file.close()

mean_rate_I_e = []
mean_rate_list = []

print(len(rate_list), len(rate_list[0]))

for i_0 in range(50):
    for i_1 in range(20):
        mean_rate_I_e.append(rate_list[i_1][i_0])
    mean_rate_list.append(mean_rate_I_e)
    mean_rate_I_e = []


import numpy as NP

#mean_rate_list.remove(mean_rate_list[0])

x_list = []
y_list = []

for i in range(0,500,10):
    I_e = float(i)
    x_list.append(I_e)

for j in range(1,21):

    y_list.append(j)

print(len(mean_rate_list), len(mean_rate_list[0]), len(x_list), len(y_list))

import plotly.tools as tls
tls.set_credentials_file(username='jmg1030', api_key='2c0f8cg9h4')

import plotly.plotly as py
import plotly.graph_objs as go

data = [
    go.Heatmap(
        z=rate_list,
        x=x_list,
        y=y_list
    )
]
"""layout = go.Layout(
    title='Increasing I_e vs. Ke',
    xaxis=dict(
        title='Je',
        titlefont=dict(
            family='Courier New, monospace',
            size=18,
            color='#7f7f7f'
        )
    ),
    yaxis=dict(
        title='I_e, pA',
        titlefont=dict(
            family='Courier New, monospace',
            size=18,
            color='#7f7f7f'
        )
    )
)"""
py.iplot(data, filename='Increasing I_e vs. Ke')
