import numpy as np
import pandas as pd
import plotly
import plotly.express as px
import folium
# позволяет строить несколько графиков на 1 странице
import plotly.graph_objs as go

dx = [1, 2, 3, 4]
dy = [1, 4, 9, 16]
fig = px.line(x=dx, y=dy, title='Plot')
fig.show()

# from plotly.graph_objs import Scatter, Layout
# plotly.offline.plot({ "data": [Scatter(x=[1, 2, 3, 4], y=[4, 3, 2, 1])], "layout": Layout(title="hello world") })

dx = np.arange(0, 10, 0.5)

# def f1(x):
#     return x * x

dy = list(map(lambda x: x * x, dx))

fig2 = px.area(x=dx, y=dy, title='Plot2')
fig2.show()
# line, scatter,area,bar,pie

df = px.data.carshare()
print(df)
# fig3 = px.bar(df,x='peak_hour',y='car_hours')
# fig3.show()
df1 = df.groupby(df.peak_hour).sum()
print(df1)
fig4 = px.bar(df1, x=df1.index, y='car_hours', color='car_hours',
              color_continuous_scale=['red', 'orange', 'green', 'blue', 'violet'])
fig4.show()

df2 = pd.read_excel('exel.xlsx')
print(df2)
fig5 = px.scatter(df2, x=df2.index, y=df2.Средний)
fig5.show()

# russia_map = folium.Map(location = [64.6863136, 97.7453061], zoom_start = 4)

df3 = px.data.election()
print(df3)
dsum = df3.groupby(df3.winner).count()
print(dsum)
fig6 = px.pie(dsum, names=dsum.index, values=dsum.result)
fig6.show()

data2 = [100000, 120000, 150000, 80000, 200000, 250000, 180000, 300000, 280000, 320000, 350000, 400000,
         180000, 200000, 220000, 240000, 260000, 280000, 300000, 320000, 340000, 360000, 380000, 400000,
         150000, 300000, 250000, 280000, 320000, 350000, 380000, 400000, 420000, 440000, 470000, 500000,
         200000, 220000, 240000, 260000, 280000, 300000, 320000, 340000, 360000, 380000, 400000, 420000,
         150000, 160000, 180000, 200000, 220000, 240000, 260000, 280000, 300000, 320000, 340000, 360000]
ser2 = pd.Series(data2, index=pd.date_range(start='2019-01-01', periods=len(data2), freq='D'))

fig7 = px.line(ser2, x=ser2.index, y=data2)
fig7.show()

dx = np.arange(1, 100)
dy1 = np.random.randint(1, 10, size=100)
dy2 = np.random.randint(20, 50, size=100)
dy3 = np.random.randint(60, 100, size=100)

fig8 = go.Figure()
g1 = go.Scatter(x=dx, y=dy1, name='plot1', mode='markers')
g2 = go.Scatter(x=dx, y=dy2, name='plot2', mode='lines')
g3 = go.Scatter(x=dx, y=dy3, name='plot3', mode='markers+lines')
fig8.add_trace(g1)
fig8.add_trace(g2)
fig8.add_trace(g3)
fig8.update_yaxes(title='points')
fig8.update_xaxes(title='from 0 to 100')
fig8.update_layout(title='Plot')
fig8.show()
