import csv
import plotly.plotly as py
import plotly.graph_objs as go
def datalist():
    """csvdata to list"""
    with open('dataupdate.csv', newline="", encoding='utf-8') as data:
        readdata = csv.reader(data)
        lst = list(readdata)
        processlist(lst)

def processlist(lst):
    """processdata to use"""
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
        lstmin += [i[5]]
        lstmax += [i[4]]
        lstmean += [i[6]]
        lstname += [i[0]]
    graph(lstmin, lstmax, lstmean, lstname)

def graph(lstmin, lstmax, lstmean, lstname):
    """printgraph"""
    trace0 = go.Scatter(
        x = lstname,
        y = lstmin,
        name = 'คะเเนนน้อยสุด',
        mode = 'lines+markers',
        line = dict(
        color = ('rgb(255, 0, 0)'),
        width = 2)
    )
    trace1 = go.Scatter(
        x = lstname,
        y = lstmax,
        name = 'คะเเนนมากสุด',
        mode = 'lines+markers',
        line = dict(
            color = ('rgb(255, 255, 0)'),
            width = 2)
    )
    trace2 = go.Scatter(
        x = lstname,
        y = lstmean,
        name = 'คะเเนนเฉลี่ย',
        mode = 'lines+markers',
        line = dict(
        color = ('rgb(51, 255, 51)'),
        width = 2)
    )
    data = [trace0, trace1, trace2]
    layout = dict(title = 'คะเเนนของเเต่ละคณะ',
                  yaxis = dict(title = 'คะเเนน'),
                  )
    fig = dict(data=data, layout=layout)
    py.iplot(fig, filename='styled-line')
datalist()
