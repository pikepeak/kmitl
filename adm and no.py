import csv

with open('สมุดงาน1.csv', newline="", encoding='utf-8') as aaa:
    a = csv.reader(aaa)
    total = list(a)

adm = 0
noadm = 0
lis_data = []
for i in total:
    adm += int(i[2])
    noadm += int(i[3])
    lis_data.append(int(i[2]))
    lis_data.append(int(i[3]))

import plotly.plotly as py
import plotly.graph_objs as go
fig = {
  "data": [
    {
      "values": [adm, noadm],
      "labels": [
        "Admission",
        "No Admission",
      ],
      "domain": {"x": [0, .48]},
      "type": "pie",
      'textinfo':'value+percent'
    },     
    {
      "values": lis_data,
      "labels": [
        "แอดคณะวิศวกรรมศาสตร์",
        "ไม่แอดคณะวิศวกรรมศาสตร์",
        "แอดสถาปัตยกรรมศาสตร์",
        "ไม่แอดสถาปัตยกรรมศาสตร์",
        "แอดคณะครุศาสตร์อุตสาหกรรม",
        "ไม่แอดคณะครุศาสตร์อุตสาหกรรม",
        "แอดคณะเทคโนโลยีการเกษตร",
        "ไม่แอดคณะเทคโนโลยีการเกษตร",
        "แอดคณะวิทยาศาสตร์",
        "ไม่แอดคณะวิทยาศาสตร์",
        "แอดคณะอุตสาหกรรมเกษตร",
        "ไม่แอดคณะอุตสาหกรรมเกษตร",
        "แอดอื่นๆ",
        "ไม่แอดอื่นๆ"
      ],
      "text":"แอดและไม่แอดของแต่ละคณะ",
      "domain": {"x": [.50, 0.98]},
      "type": "pie",
      'textinfo':'value+percent'
    },     
  ],
  "layout": {
        "title":'จำนวนทั้งหมดของแอดมิชชั่นและของแต่ละคณะ',
        }
}

url = py.plot(fig, filename='จำนวนทั้งหมดของแอดมิชชั่นและของแต่ละคณะ')
