This is the folder that is going to contain the code and resources that I have used for my bachelor thesis "Modelling thte Footbalers Prices on a Transfer Market".
The work is in a progress so I will be updating this folder throughout the time.
So far,it contains a small scraper that scraps names and values of football players from teams taken from "teams.txt" which contains the links to the top 5 leagues clubs from 2019/20 season.
The data that I have scraped - Footballersdata_FBRef_Transfermarkt_2019.csv - is the combination of datasets that I have scraped with the usage of this open source tools:

https://github.com/vnherdeiro/transfermarkt-scraping (my modificiations contained in a folder transfermarkt-scraping-master modified)
https://github.com/parth1902/Scrape-FBref-data (my modifications contained in a file FBRef_scrap_modified.ipynb)

and my small Transfermarkt scraper as well (although to be honest I could have easily modified the first scraper to give players values as well - however, I have not wanted to extend the long scraping time even further within the first module)
I have slightly modified the code within the projects for my own purposes:
1. I deleted/markdowned the lines of code that filtered only offensive players and have modified some parts to omit some problems with the file (for example taking the leagues data from previous seasons - in this example, 2017/18) and to add parameters like Height as well
2. I have modified some parts to take data from previous seasons
There is an issue with the first one that Bundesliga is for some reason skipped during the process of scraping. The issue can be solved with simply inserting the link in LEAGUES_URL that heads directly to Bundesliga league site and properly modifying LeaguesUrlDic variable.
In my modifications you can see that the code was used for 2017/18 season but I am focusing data only for 2019/20 throughout the later work.
I have managed to bind three datasets that were created from the files into a single one Footballersdata_FBRef_Transfermarkt_2019.csv making some data wrangling.
It contains both the data from transfermarkt and fbref including transfermarkt values for players.
To polish the dataset I needed to modify some entries by my own hand. Some entries from Transfermarkt failed to be binded with fbref entries due to different player names in both environments including the special marks for specific languages.
For example - in Transfermarkt one of the most renowned keepers in the world, Wojciech Szczęsny is called "Wojciech Szczesny", whereas in fbref - Wojciech Szczęsny, containing "ę" letter which exists in Polish alphabet. Due to that, the data from fbref failed to match with data from transfermarkt.
Those were however approximately 10% of the entries. Possibly there is the method to solve this issue with code, but at the time of creating this document I am not aware of such a solution.

The folder "other various data" contains other data that I have managed to scrap but that are not really relevant for the purpose of my further work.

Licencjat.ipynb is a file with the actual code used for further work which will be updated


