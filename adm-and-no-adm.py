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
        "NotAdmission",
      ],
      "domain": {"x": [0, .45]},
      "type": "pie",
      'textinfo':'value+percent'
    },     
    {
      "values": lis_data,
      "labels": [
        "แอดมิชชั่นคณะวิศวกรรมศาสตร์",
        "ไม่แอดมิชชั่นคณะวิศวกรรมศาสตร์",
        "แอดมิชชั่นสถาปัตยกรรมศาสตร์",
        "ไม่แอดมิชชั่นสถาปัตยกรรมศาสตร์",
        "แอดมิชชั่นคณะครุศาสตร์อุตสาหกรรม",
        "ไม่แอดมิชชั่นคณะครุศาสตร์อุตสาหกรรม",
        "แอดมิชชั่นคณะเทคโนโลยีการเกษตร",
        "ไม่แอดมิชชั่นคณะเทคโนโลยีการเกษตร",
        "แอดมิชชั่นคณะวิทยาศาสตร์",
        "ไม่แอดมิชชั่นคณะวิทยาศาสตร์",
        "แอดมิชชั่นคณะอุตสาหกรรมเกษตร",
        "ไม่แอดมิชชั่นคณะอุตสาหกรรมเกษตร",
        "แอดมิชชั่นคณะอื่นๆ",
        "ไม่แอดมิชชั่นคณะอื่นๆ"
      ],
      "text":"แอดและไม่แอดของแต่ละคณะ",
      "domain": {"x": [.45, 0.90]},
      "type": "pie",
      'textinfo':'value+percent'
    },     
  ],
  "layout": {
        "title":'จำนวนที่เเอดมิชชั่นเเละไม่เเอดมิชชั่นของเเต่ละคณะเเละโดยรวม',
        }
}

url = py.plot(fig, filename='admission and notadmission')
