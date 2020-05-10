import plotly.offline as pyo
import plotly.graph_objs as go

snodgrass = [.209,.205,.196,.210,.202,.207,.224,.223,.220,.201]
twain = [.225,.262,.217,.240,.230,.229,.235,.217]

trace0 =go.Box(y=snodgrass,
               boxpoints = 'all',
               jitter = 0.3,
               pointpos = 0,
               name = 'snodgrass')

trace1 =go.Box(y=twain,
               boxpoints = 'all',
               jitter = 0.3,
               pointpos = 0,
               name = 'twain')



data = [trace0,trace1]
layout= go.Layout(title = 'snodgrass vs twain')
fig = go.Figure(data = data, layout = layout)
pyo.plot(fig,filename = 'plots/boxplot2.html')
