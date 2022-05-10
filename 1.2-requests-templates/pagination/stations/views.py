from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
import csv


def index(request):
    return redirect(reverse('bus_stations'))


#  CONTENT = pd.read_csv(csvfile, usecols=['Name','Street', 'District'], error_bad_lines=False)#теперь можем читать только нужные поля, сэкономив память
#  # получите текущую страницу и передайте ее в контекст
#  paginator = Paginator(CONTENT, 10)
#  page = paginator.get_page(1)
#  # также передайте в контекст список станций на странице
# # CONTENT2 = pd.read_csv(csvfile, usecols=['Name','Street'], error_bad_lines=False)
#  #paginator = Paginator(CONTENT2, 10)
#  bus_stations = page.object_list.Name

def bus_stations(request):
    with open('data-398-2018-08-30.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)#, fieldnames=('Name', 'Street', 'District')
        reader2, bus_stations = {},{}
        list_Name, list_Street, list_District = [], [], []
        page=1
        # получите текущую страницу и передайте ее в контекст
        numb_str=0
        for row in reader:
            reader2.update(row)
            list_Name.append(str(reader2['Name']))
            list_Street.append(str(reader2['Street']))
            list_District.append(str(reader2['District']))
            numb_str+=1
        # for key, value in reader.items():  # use .items() if you use Python 3
        #     if key == "Name" or "Street" or 'District':
        #         CONTENT[key] = value
        #     if key == "Name":
        #         bus_stations[key] = value
        # также передайте в контекст список станций на странице
        CONTENT = list(zip(list_Name, list_Street, list_District))
        paginator_bus = Paginator(CONTENT, 10)
        bus_stations = paginator_bus.get_page(page).object_list
        context = {
            'bus_stations': bus_stations,
            'page': page,
        }
    return render(request, 'stations/index.html', context)
