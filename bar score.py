import csv
import plotly.plotly as py
import plotly.graph_objs as go
with open('dataupdate.csv', newline="", encoding='utf-8') as aaa:
    a = csv.reader(aaa)
    lst = list(a)
    minofmax = []
for i in lst:
    minofmax += [i[5]]
minofmax = sorted(minofmax)
minofmax = minofmax[::-1]
area = {}
for i in minofmax:
    for j in lst:
        if i == j[5]:
            area[i] = j
lst1 = []
for i in minofmax:
    lst1 += [area[i]]
lstmin = []
lstmax = []
lstmean = []
lstname = []

for i in lst1:
    lstmin += [float(i[5])]
    lstmax += [float(i[4])]
    lstmean += [float(i[6])]
    lstname += [i[0]]
trace1 = go.Bar(
    x=lstname,
    y=lstmin,
    name='min'
)
trace2 = go.Bar(
    x=lstname,
    y=lstmean,
    name='mean'
)
trace3 = go.Bar(
    x=lstname,
    y=lstmean,
    name='max'
)
data = [trace1, trace2, trace3]
layout = go.Layout(
    barmode='group',
    title='คะเเนนของเเต่ละคณะ'
)
fig = go.Figure(data=data, layout=layout)
plot_url = py.plot(fig, filename='stacked-bar')
