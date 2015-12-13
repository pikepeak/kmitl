import csv
import plotly.plotly as py
import plotly.graph_objs as go
def datainput():
    """csvdata input to list"""
    with open('สมุดงาน1.csv', newline="", encoding = 'utf-8') as data:
        list1 = csv.reader(data)
        listdata = list(list1)
    list_var(listdata)

def list_var(listdata):
    """list to var"""
    adm = 0
    noadm = 0
    lis_data = []
    for i in listdata:
        adm += int(i[2])
        noadm += int(i[3])
        lis_data.append(int(i[2]))
        lis_data.append(int(i[3]))
    graph(adm, noadm, lis_data)

def graph(adm, noadm, lis_data):
    """printgraph"""
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
          "domain": {"x": [.50, 0.98]},
          "type": "pie",
          'textinfo':'value+percent',
          'sort':False,
          'pull':.08,
          'marker': {'colors': ['rgb(0, 255, 0)', 'rgb(0, 220, 0)',
                            'rgb(255, 0, 0)', 'rgb(220, 0 ,0)',
                            'rgb(255, 128, 0)', 'rgb(220 , 128, 0)',
                            'rgb(255, 255, 0)', 'rgb(220, 220, 0)',
                            'rgb(128, 255, 0)', 'rgb(128, 220, 0)',
                            'rgb(0, 255, 255)', 'rgb(0, 220, 220)',
                            'rgb(255, 0, 255)', 'rgb(220, 0, 220)']}
        },
      ],
      "layout": {"title":'จำนวนที่เเอดมิชชั่นเเละไม่เเอดมิชชั่นของเเต่ละคณะเเละโดยรวม'}
    }

    url = py.plot(fig, filename='admission and notadmission')
datainput()
