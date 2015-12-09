import csv
import plotly.plotly as py
import plotly.graph_objs as go
with open('dataupdate.csv', newline="", encoding='utf-8') as aaa:
    a = csv.reader(aaa)
    adm58 = list(a)
with open('adm56.csv', newline="", encoding='utf-8') as aaa:
    a = csv.reader(aaa)
    adm56 = list(a)
with open('adm55.csv', newline="", encoding='utf-8') as aaa:
    a = csv.reader(aaa)
    adm55 = list(a)
with open('adm54.csv', newline="", encoding='utf-8') as aaa:
    a = csv.reader(aaa)
    adm54 = list(a)
at58, at57, at56, at55, at54 = [0,0],[0,0],[0,0],[0,0],[0,0]
for i in adm58:
    at58[0] += int(i[1])
    at58[1] += int(i[2])
for i in adm56:
    at56[0] += int(i[1])
    at56[1] += int(i[2])
for i in adm55:
    at55[0] += int(i[1])
    at55[1] += int(i[2])
for i in adm54:
    at54[0] += int(i[1])
    at54[1] += int(i[2])
atreg = [at54[0], at55[0], at56[0], at58[0]]
atget = [at54[1], at55[1], at56[1], at58[1]]
trace1 = go.Bar(
    x=['54', '55', '56', '58'],
    y=atreg,
    name='จำนวนผู้สมัคร'
)
trace2 = go.Bar(
    x=['54', '55', '56', '58'],
    y=atget,
    name='จำนวนที่รับ'
)
data = [trace1, trace2]
layout = go.Layout(
    barmode='group'
)
fig = go.Figure(data=data, layout=layout)
plot_url = py.plot(fig, filename='grouped-bar')
