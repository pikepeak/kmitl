import csv
with open('dataupdate.csv') as aaa:
    a = csv.reader(aaa)
    lst = list(a)
import plotly.plotly as py
import plotly.graph_objs as go
fac = []
cnt = 1
for i in lst:
    fac += [cnt]
    cnt += 1
minfac = []
for i in lst:
    minfac += [i[4]]
trace0 = go.Scatter(
    x = fac,
    y = minfac,
    name = 'min of fac',
    line = dict(
        color = ('rgb(205, 12, 24)'),
        width = 4)
)
data = [trace0]
layout = dict(title = 'min of fac',
              xaxis = dict(title = 'min'),
              yaxis = dict(title = 'fac'),
              )
fig = dict(data=data, layout=layout)
py.iplot(fig, filename='styled-line')
