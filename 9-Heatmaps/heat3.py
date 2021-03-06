#######
# Heatmap of temperatures for Sitka, Alaska
######
import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('D:/Pycharm_files/dashboard_ Plotly_Dash/Data/2010SitkaAK.csv')

data = [go.Heatmap(
    x=df['DAY'],
    y=df['LST_TIME'],
    z=df['T_HR_AVG'],
    colorscale='Jet'
)]

layout = go.Layout(
    title='Hourly Temperatures, June 1-7, 2010 in<br>\
    Sitka, AK USA'
)
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='Sitka.html')
