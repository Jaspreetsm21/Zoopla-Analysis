import requests
import pandas as pd
from bs4 import BeautifulSoup
title = []
Bed = []
Bath = []
Type = []
Bedroom = []
Bathroom = []
TypeofHome = []
Reception = []
LastsaleDate = []
Lastsalevalue = []
for x in range(1,2500):
    url = 'https://www.zoopla.co.uk/house-prices/berkshire/?num_months=120&property_type_code=F&pn='+str(x)
    soup = BeautifulSoup(requests.get(url).content, 'html.parser')
    Soup = BeautifulSoup(requests.get(url).text,'html.parser')
    for a in soup.find_all("section",{'class':'hp-card'}):
#         print(a)
        for titlex in a.findAll( 'h3',{'class':'hp-card__title'}):
            title1 = titlex.text.strip()
        Bed1= a.find_all('li', {'class': 'hp-card-room hp-card-room--bed'})
        Bath1= a.find_all('li', {'class': 'hp-card-room hp-card-room--bath'})      
        Recept1= a.find_all('li', {'class': 'hp-card-room hp-card-room--recept'})         
        Type1 = a.find_all('ul',{'class':'hp-card__tags'})
        Bedroom1 = [li.text.strip().replace(" \n           ","") for li in Bed1]            
        Bathroom1 = [li.text.strip().replace(" \n           ","") for li in Bath1]
        Reception1 = [li.text.strip().replace(" \n           ","") for li in Recept1]
#         TypeofHome1 = [li.text.strip().replace("\n",",") for li in Type1]
#         for Bedx in a.find_all('li', {'class': 'hp-card-room hp-card-room--bed'}):
#             try:
#                 Bed1 = Bedx.text.strip().replace(" \n          ","")     
#             except:
#                 Bed1 = None
#         for Bathx in a.find_all('li', {'class': 'hp-card-room hp-card-room--bath'}):
#             Bath1 = Bathx.text.strip().replace(" \n          ","")   
#         for Receptx in a.find_all('li', {'class': 'hp-card-room hp-card-room--recept'}):
#             Recept1 = Receptx.text.strip().replace(" \n          ","")               
        for TypeofHomex in a.find_all('ul',{'class':'hp-card__tags'}):
            TypeofHome1 = TypeofHomex.text.strip().replace("\n",",")   
        for lastsaledatex in a.find_all('h4',{'class':'hp-datum__label'}): 
            Lastsaledate1 = lastsaledatex.text.strip().replace("\n",",")
        for lastsalevaluex in a.find_all('span',{'class':'hp-datum__value'}): 
            Lastsalevalue1 = lastsalevaluex.text.strip().replace("\n",",")            
        title.append(title1)
        Bedroom.append(Bedroom1)
        Bathroom.append(Bathroom1)
        Reception.append(Reception1)
        TypeofHome.append(TypeofHome1)
        LastsaleDate.append(Lastsaledate1)
        Lastsalevalue.append(Lastsalevalue1)
    df = pd.DataFrame({'title':title,'Bedroom':Bedroom,'Bathroom':Bathroom,'Reception':Reception,'TypeofHome':TypeofHome,'LastsaleDate':LastsaleDate,'Lastsalevalue':Lastsalevalue})
    df.to_csv('Zoopla_Flat.csv')