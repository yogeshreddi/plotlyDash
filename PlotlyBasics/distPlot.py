import numpy as np
import plotly.offline as pyo
import plotly.figure_factory as ff

x = np.random.randn(1000)
y = np.random.randn(1000)
z = np.random.randn(1000)

fig = ff.create_distplot([x,y-5,z+5],['distplotX','distplotY','distplotZ'])
pyo.plot(fig,filename = 'plots/distplot.html')

snodgrass = [.209,.205,.196,.210,.202,.207,.224,.223,.220,.201]
twain = [.225,.262,.217,.240,.230,.229,.235,.217]

fig = ff.create_distplot([snodgrass,twain],['snodgrass','twain'],bin_size = [0.005,0.005])
pyo.plot(fig,filename = 'plots/distplot2.html')
