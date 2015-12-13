import csv
import plotly.plotly as py
import plotly.graph_objs as go
def datalst():
    """csvdata to list"""
    with open('dataupdate.csv', newline="", encoding='utf-8') as data:
        readdata = csv.reader(data)
        adm58 = list(readdata)
    with open('adm57.csv', newline="", encoding='utf-8') as data:
        readdata = csv.reader(data)
        adm57 = list(readdata)
    with open('adm56.csv', newline="", encoding='utf-8') as data:
        readdata = csv.reader(data)
        adm56 = list(readdata)
    with open('adm55.csv', newline="", encoding='utf-8') as data:
        readdata = csv.reader(data)
        adm55 = list(readdata)
    with open('adm54.csv', newline="", encoding='utf-8') as data:
        readdata = csv.reader(data)
        adm54 = list(readdata)
    lstsublst(adm54, adm55, adm56, adm57, adm58)

def lstsublst(adm54, adm55, adm56, adm57, adm58):
    """lsttosublst"""
    atreg = [0,0,0,0,0]
    atget = [0,0,0,0,0]
    atreg1 = [0,0,0,0,0]
    atget1 = [0,0,0,0,0]
    atreg2 = [0,0,0,0,0]
    atget2 = [0,0,0,0,0]
    atreg3 = [0,0,0,0,0]
    atget3 = [0,0,0,0,0]
    atreg4 = [0,0,0,0,0]
    atget4 = [0,0,0,0,0]
    atreg5 = [0,0,0,0,0]
    atget5 = [0,0,0,0,0]
    cot = 0
    for i in (adm54, adm55, adm56, adm57, adm58):
        cnt = 0
        while cnt+1 <= len(i):
            if 'คณะวิศวก' in i[cnt][0]:
                atget[cot] += int(i[cnt][2])
                atreg[cot] += int(i[cnt][1])
            elif 'คณะครุศา' in i[cnt][0]:
                atget1[cot] += int(i[cnt][2])
                atreg1[cot] += int(i[cnt][1])
            elif 'คณะเทคโนโลยีการเกษตร' in i[cnt][0]:
                atget2[cot] += int(i[cnt][2])
                atreg2[cot] += int(i[cnt][1])
            elif 'คณะวิทยาศาสตร์' in i[cnt][0]:
                atget3[cot] += int(i[cnt][2])
                atreg3[cot] += int(i[cnt][1])
            elif 'คณะอุตสาหกรรมเกษตร' in i[cnt][0]:
                atget4[cot] += int(i[cnt][2])
                atreg4[cot] += int(i[cnt][1])
            else:
                atget5[cot] += int(i[cnt][2])
                atreg5[cot] += int(i[cnt][1])
            cnt += 1
        cot += 1
    aitget(atget, atget1, atget2, atget3, atget4, atget5)
    aitreg(atreg, atreg1, atreg2, atreg3, atreg4, atreg5)

def aitget(atget, atget1, atget2, atget3, atget4, atget5):
    """printgraphofget"""
    trace1 = go.Bar(
        x=['54', '55', '56', '57', '58'],
        y=atget,
        name='คณะวิศวก'
    )
    trace2 = go.Bar(
        x=['54', '55', '56', '57', '58'],
        y=atget1,
        name='คณะครุศา'
    )
    trace3 = go.Bar(
        x=['54', '55', '56', '57', '58'],
        y=atget2,
        name='คณะเทคโนโลยีการเกษตร'
    )
    trace4 = go.Bar(
        x=['54', '55', '56', '57', '58'],
        y=atget3,
        name='คณะวิทยาศาสตร์'
    )
    trace5 = go.Bar(
        x=['54', '55', '56', '57', '58'],
        y=atget4,
        name='คณะอุตสาหกรรมเกษตร'
    )
    trace6 = go.Bar(
        x=['54', '55', '56', '57', '58'],
        y=atget5,
        name='อื่นๆ'
    )
    data = [trace1, trace2, trace3, trace4, trace5, trace6]
    layout = go.Layout(
        barmode='stack'
    )
    fig = go.Figure(data=data, layout=layout)
    plot_url = py.plot(fig, filename='จำนวนรับ')
def aitreg(atreg, atreg1, atreg2, atreg3, atreg4, atreg5):
    """printgraphofget"""
    trace1 = go.Bar(
        x=['54', '55', '56', '57', '58'],
        y=atreg,
        name='คณะวิศวก'
    )
    trace2 = go.Bar(
        x=['54', '55', '56', '57', '58'],
        y=atreg1,
        name='คณะครุศา'
    )
    trace3 = go.Bar(
        x=['54', '55', '56', '57', '58'],
        y=atreg2,
        name='คณะเทคโนโลยีการเกษตร'
    )
    trace4 = go.Bar(
        x=['54', '55', '56', '57', '58'],
        y=atreg3,
        name='คณะวิทยาศาสตร์'
    )
    trace5 = go.Bar(
        x=['54', '55', '56', '57', '58'],
        y=atreg4,
        name='คณะอุตสาหกรรมเกษตร'
    )
    trace6 = go.Bar(
        x=['54', '55', '56', '57', '58'],
        y=atreg5,
        name='อื่นๆ'
    )
    data = [trace1, trace2, trace3, trace4, trace5, trace6]
    layout = go.Layout(
        barmode='stack'
    )
    fig = go.Figure(data=data, layout=layout)
    plot_url = py.plot(fig, filename='จำนวนสมัคร')
datalst()
