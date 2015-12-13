import csv
import plotly.plotly as py
import plotly.graph_objs as go
def datalist():
    """data to list""" 
    with open('dataupdate.csv', newline = "", encoding='utf-8') as data:
        datalst = csv.reader(data)
        lst = list(datalst)
    with open('สมุดงาน2.csv', newline = "", encoding='utf-8') as data:
        datalst = csv.reader(data)
        lst2 = list(datalst)
    lstsublst(lst2, lst)

def lstsublst(lst2, lst):
    """list to sublist"""
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
    graph(lstname, lstget, lstreg)

def graph(lstname, lstget, lstreg):
    """printgraph"""
    fig = {
      "data": [
        {
          "values": lstget,
          "labels": lstname,
          "domain": {"x": [0, .50]},
          "name": "จำนวนที่รับ",
          "hole": .2,
          'textinfo':'value+percent',
          "type": "pie"
        },
        {
      "values": lstreg,
      "labels": lstname,
      "domain": {"x": [.50, 1]},
      "name": "จำนวนที่สมัคร",
      "hole": .2,
      'textinfo':'value+percent',
      "type": "pie"
        },
      ],
      "layout": {
            "title":"จำนวนที่รับ เเละ จำนวนที่สมัคร",
            "annotations": [
                {
                    "font": {
                        "size": 20
                    },
                "showarrow": False,
                "text": "รับ",
                "x": 0.22,
                "y": 0.5
            },
            {
                "font": {
                    "size": 20
                },
                "showarrow": False,
                "text": "สมัคร",
                "x": 0.8,
                "y": 0.5
            }
            ]
        }
    }

    url = py.plot(fig, filename='GET and REG')
datalist()
