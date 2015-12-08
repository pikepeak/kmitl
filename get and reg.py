import csv
with open('dataupdate.csv', newline = "", encoding='utf-8') as aaa:
    a = csv.reader(aaa)
    lst = list(a)
with open('สมุดงาน2.csv', newline = "", encoding='utf-8') as bbb:
    b = csv.reader(bbb)
    lst2 = list(b)
lstname = []
lstget = [0, 0, 0, 0, 0, 0]
lstreg = [0, 0, 0, 0, 0, 0]
for i in lst2:
    lstname.append(i)
for i in range(len(lst)):
    if i <= 18:
        lstget[0] += int(lst[i][2])
        lstreg[0] += int(lst[i][1])
    elif i <= 25:
        lstget[1] += int(lst[i][2])
        lstreg[1] += int(lst[i][1])
    elif i <= 30:
        lstget[2] += int(lst[i][2])
        lstreg[2] += int(lst[i][1])
    elif i <= 38:
        lstget[3] += int(lst[i][2])
        lstreg[3] += int(lst[i][1])
    elif i <= 41:
        lstget[4] += int(lst[i][2])
        lstreg[4] += int(lst[i][1])
    else:
        lstget[5] += int(lst[i][2])
        lstreg[5] += int(lst[i][1])
import plotly.plotly as py
import plotly.graph_objs as go

fig = {
  "data": [
    {
      "values": lstget,
      "labels": lstname,
      "domain": {"x": [0, .48]},
      "name": "get",
      "hole": .4,
      "type": "pie"
    },     
    {
      "values": lstreg,
      "labels": lstname,
      "text":"CO2",
      "textposition":"inside",
      "domain": {"x": [.52, 1]},
      "name": "reg",
      "hole": .4,
      "type": "pie"
    },     
  ],
  "layout": {
        "title":"get and reg",
        "annotations": [
            {
                "font": {
                    "size": 20
                },
                "showarrow": False,
                "text": "GET",
                "x": 0.20,
                "y": 0.5
            },
            {
                "font": {
                    "size": 20
                },
                "showarrow": False,
                "text": "REG",
                "x": 0.8,
                "y": 0.5
            }
        ]
    }
}

url = py.plot(fig, filename='GET and REG')
