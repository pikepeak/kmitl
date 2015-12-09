import csv
import plotly.plotly as py
import plotly.graph_objs as go
with open('dataupdate.csv', newline="", encoding='utf-8') as aaa:
    a = csv.reader(aaa)
    adm58 = list(a)
with open('adm57.csv', newline="", encoding='utf-8') as aaa:
    a = csv.reader(aaa)
    adm57 = list(a)
with open('adm56.csv', newline="", encoding='utf-8') as aaa:
    a = csv.reader(aaa)
    adm56 = list(a)
with open('adm55.csv', newline="", encoding='utf-8') as aaa:
    a = csv.reader(aaa)
    adm55 = list(a)
with open('adm54.csv', newline="", encoding='utf-8') as aaa:
    a = csv.reader(aaa)
    adm54 = list(a)
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
