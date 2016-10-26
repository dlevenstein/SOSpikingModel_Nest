import nest
import numpy as np
import simplejson

open_file = open("decreasing_heat_map_values_I_e_Je.json", "r")
rate_list = simplejson.load(open_file)
open_file.close()

mean_rate_I_e = []
mean_rate_list = []





import numpy as NP

#mean_rate_list.remove(mean_rate_list[0])

x_list = []
y_list = []

for i in range(500,0,-10):
    I_e = float(i)
    x_list.append(I_e)

Je_parameters = np.arange(0,10,0.2)

for j in Je_parameters:

    y_list.append(j)

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
    title='Increasing I_e vs. Je',
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
py.iplot(data, filename='Decreasing I_e vs. Je')
