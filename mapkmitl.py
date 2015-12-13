import folium
import csv
def data_lst():
    """csv to list and colorlist"""
    with open('overall.csv', newline="", encoding='utf-8') as data:
        lst = csv.reader(data)
        total = list(lst)
    color = ['#769d96', '#F72929', '#ED19D4', '#5008F9', '#F3FA36', '#FA3D36'
             '#52FAFF', '#7B4C7F', '#34FD48', '#FDCE34', '#FF0000', '#DA5000']
    return total, color

def plotmap():
    """set map"""
    imap = folium.Map(location=[float(13.7282), float(100.7777)], zoom_start=16)
    return imap

def plotpointdata():
    """mydata to mymap"""
    imap = plotmap()
    total, color = data_lst()
    cnt = 0
    while cnt < len(total):
        at = total[cnt]
        fac = str(at[0])
        get = str(at[1])
        lat = float(at[2])
        lon = float(at[3])
        popup1 = """คณะ : %s <br>
        จำนวนนักศึกษาใหม่ : %s <br>
        """ % (fac, get)
        imap.polygon_marker(location=[lat,lon] ,popup=popup1, fill_color= color[cnt], num_sides=8, radius=15)
        cnt += 1
    imap.create_map(path='kmitl.html')

plotpointdata()
