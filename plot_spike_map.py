import nest
import numpy as np
import simplejson

open_file = open("spike_averages.json", "r")
rate_list = simplejson.load(open_file)
open_file.close()

x_list = range(0, 5010, 10)
y_list = range(0, 105, 5)


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
layout = go.Layout(
    title='Time vs. Adaptation: Mean Spike Rate',
    xaxis=dict(
        title='Adaptative b',
        titlefont=dict(
            family='Courier New, monospace',
            size=18,
            color='#7f7f7f'
        )
    ),
    yaxis=dict(
        title='Time: ms',
        titlefont=dict(
            family='Courier New, monospace',
            size=18,
            color='#7f7f7f'
        )
    )
)
py.iplot(data, filename='Time vs. Adaptation: Mean Spike Rate')
