import csv
import plotly.plotly as py
import plotly.graph_objs as go
def datalst():
    """csvdata to lst"""
    with open('dataupdate.csv', newline="", encoding='utf-8') as aaa:
        a = csv.reader(aaa)
        adm58 = list(a)
    with open('adm54.csv', newline="", encoding='utf-8') as aaa:
        a = csv.reader(aaa)
        adm54 = list(a)
    with open('adm55.csv', newline="", encoding='utf-8') as aaa:
        a = csv.reader(aaa)
        adm55 = list(a)
    with open('adm56.csv', newline="", encoding='utf-8') as aaa:
        a = csv.reader(aaa)
        adm56 = list(a)
    with open('adm57.csv', newline="", encoding='utf-8') as aaa:
        a = csv.reader(aaa)
        adm57 = list(a)
    return adm54, adm55, adm56, adm57, adm58

def meanmin():
    """mean of min score adm54-48"""
    adm54, adm55, adm56, adm57, adm58 = datalst()
    all_min = 0
    for i in adm54:
        all_min += float(i[5])
    min_54 = all_min/len(adm54)
    all_min = 0
    for i in adm55:
        all_min += float(i[5])
    min_55 = all_min/len(adm55)
    all_min = 0
    for i in adm56:
        all_min += float(i[5])
    min_56 = all_min/len(adm56)
    all_min = 0
    for i in adm57:
        all_min += float(i[5])
    min_57 = all_min/len(adm57)
    all_min = 0
    for i in adm58:
        all_min += float(i[5])
    min_58 = all_min/len(adm58)
    trace2 = go.Bar(
        x=['2554', '2555', '2556', '2557', '2558'],
        y=[min_54, min_55, min_56, min_57, min_58],
        name='mean of min'
    )
    return trace2

def meanmax():
    """mean of max score adm24-58"""
    adm54, adm55, adm56, adm57, adm58 = datalst()
    all_max = 0
    for i in adm54:
        all_max += float(i[4])
    max_54 = all_max/len(adm54)
    all_max = 0
    for i in adm55:
        all_max += float(i[4])
    max_55 = all_max/len(adm55)
    all_max = 0
    for i in adm56:
        all_max += float(i[4])
    max_56 = all_max/len(adm56)
    all_max = 0
    for i in adm57:
        all_max += float(i[4])
    max_57 = all_max/len(adm57)
    all_max = 0
    for i in adm58:
        all_max += float(i[4])
    max_58 = all_max/len(adm58)
    trace1 = go.Bar(
        x=['2554', '2555', '2556', '2557', '2558'],
        y=[max_54, max_55, max_56, max_57, max_58],
        name='mean of max'
    )
    return trace1

def graph():
    """printgraph"""
    data = [meanmax(), meanmin()]
    layout = go.Layout(
        barmode='group'
    )
    fig = go.Figure(data=data, layout=layout)
    plot_url = py.plot(fig, filename='grouped-bar')
graph()
