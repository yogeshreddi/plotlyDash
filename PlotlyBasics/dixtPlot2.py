import pandas as pd
import plotly.offline as pyo
import plotly.figure_factory as ff

df = pd.read_csv('C:/Users/3780183/Projects/PersonalDevelopment/pythonDash/Data/iris.csv')

#print(df['class'].unique())

dist_plot = [df[df['class'] == i]['petal_length'] for i in df['class'].unique()]
group_lables = df['class'].unique()

fig = ff.create_distplot(dist_plot,group_lables)
pyo.plot(fig,'plots/distPlot3.html')
