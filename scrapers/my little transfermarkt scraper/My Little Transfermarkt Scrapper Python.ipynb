#multiple ones, it works but needs improvement

import requests
from bs4 import BeautifulSoup
import pandas as pd

teams=pd.read_csv('teams\teams2020.txt', header=None)
teams=pd.Series((teams[0]))
length1=len(teams)

df=pd.DataFrame()

for i in range(length1):

    page = "https://www.transfermarkt.de" + teams[i]
    pageTree = requests.get(page, headers=headers)
    pageSoup = BeautifulSoup(pageTree.content, 'html.parser')

    Players = pageSoup.find_all("a", {"class": "spielprofil_tooltip"})[::2]
    Values = pageSoup.find_all("td", {"class": "rechts hauptlink"})
    PlayersList = []
    ValuesList = []
     
    length = len(Values)

    for j in range(0,length):
        PlayersList.append(Players[j].text)
        ValuesList.append(Values[j].text)
        
    df1=pd.DataFrame({"Players":PlayersList,"Values":ValuesList})
    df=df.append(df1)
    
#cleaning players not valued in millions - these won't be considered in modelling
df = df[df['Values'].str.contains('Mio', na=False)]
df['Values']=((df['Values'].str.split(' ').str[0]).replace(',','.',regex=True).astype(float))*1000000
#df.to_csv('bazatest.csv',sep=';')
df