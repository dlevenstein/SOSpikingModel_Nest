import nest
import numpy as np
import simplejson

open_file = open("heat_map_values_I_e_Ke.json", "r")
mean_rate_list = simplejson.load(open_file)
open_file.close()

import numpy as NP

mean_rate_list.remove(mean_rate_list[0])

x_0 = np.arange(0,500,10)
y_0 = np.arange(0,10,0.2)

x_list = []
y_list = []

for i in range(0,500,10):
    y_list.append(i)

number = 0
for j in range(20):
    number += 1
    x_list.append(number)

import plotly.tools as tls
tls.set_credentials_file(username='jmg1030', api_key='2c0f8cg9h4')

import plotly.plotly as py
import plotly.graph_objs as go

print(len(x_list))
print(len(y_list))
print(len(mean_rate_list))
print(len(mean_rate_list[0]))

data = [
    go.Heatmap(
        z=mean_rate_list,
        x=x_list,
        y=y_list
    )
]
layout = go.Layout(
    title='Plot Title',
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
)
py.iplot(data, filename='labelled-heatmap')
