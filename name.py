import csv
with open('dataupdate.csv', newline = "", encoding='utf-8') as aaa:
    a = csv.reader(aaa)
    lst = list(a)
with open('สมุดงาน2.csv', newline = "", encoding='utf-8') as bbb:
    b = csv.reader(bbb)
    lst2 = list(b)
lstname = []
lstget = [0, 0, 0, 0, 0, 0]
for i in lst2:
    lstname.append(i)
for i in range(len(lst)):
    if i <= 18:
        lstget[0] += int(lst[i][2])
    elif i <= 25:
        lstget[1] += int(lst[i][2])
    elif i <= 30:
        lstget[2] += int(lst[i][2])
    elif i <= 38:
        lstget[3] += int(lst[i][2])
    elif i <= 41:
        lstget[4] += int(lst[i][2])
    else:
        lstget[5] += int(lst[i][2])
import plotly.plotly as py
import plotly.graph_objs as go

fig = {
    'data': [{'labels': lstname,
              'values': lstget,
              'type': 'pie',
              'marker': {'colors': ['rgb(56, 75, 126)',
                                  'rgb(18, 36, 37)',
                                  'rgb(34, 53, 101)',
                                  'rgb(36, 55, 57)',
                                  'rgb(6, 4, 4)']}}],  
    'layout': {'title': 'how many get'}
}

url = py.plot(fig, filename='Pie Chart Example')
        
    
