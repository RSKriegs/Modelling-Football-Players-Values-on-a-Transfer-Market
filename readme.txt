.pdf file "RS82640(...)" contains a finished bachelor thesis. Final grade 5/5

Folder "code" contains the whole code created for data wrangling, analysis, modelling and visualization. 
- Licencjat_DataViz.ipynb contains script that creates analysis and dashboards for I chapter of my bachelor's thesis and significant variables for team performance described in II chapter,
- Licencjat_Fifa21Analysis.ipynb consists of compact analysis of distribution of chosen players' in-game attributes in their relation to age, what is a part of a I chapter.
- Licencjat_Modelling_Goalkeepers.ipynb, Licencjat_Modelling_Defenders.ipynb, Licencjat_Modelling_Midfielders.ipynb, Licencjat_Modelling_Forwards.ipynb are the files where models for each position are created and properly diagnosed, including cross-validation for each.
- Licencjat_Modelling_Gathered gathers the analysis from all above files and models validation, including out-of-sample validation basing on real-life transfers.
- Note that several lines of code have been modified throughout the process of writing the thesis - in order to replicate results in 100%, one would need to change several parameters accordingly (for example - MAE for each league)
- In the end, folder contains subfolder "demo scikit-learn", which consists of Licencjat_NeuralNet_GKExample.ipynb and Licencjat_RegressionsSKLearn_ExampleGK.ipynb files. Those are the files consisting of certain lines of code, with first one creating neural network basing on MLPClassifier algorithm checking if player on a transfermarkt.de is overvalued or undervalued, whereas the second one replicates the linear regression originally created in StatsModels. Each of them has been created for goalkeepers only. These have not been developed further as I have not used them in a final thesis.

Folder "scrapers" contains... well, web scrapers, that were used to download data from transfermarkt.de and fbref.com.
Source code for scrapers which I modified accordingly:
https://github.com/vnherdeiro/transfermarkt-scraping (my modificiations contained in a folder transfermarkt-scraping-master modified)
https://github.com/parth1902/Scrape-FBref-data (my modifications contained in a file FBRef_scrap_modified.ipynb)
Includes my own scraper for players values on Transfermarkt (my_little_transfermarkt_scraper.py).
Folder "teams" within "my little transfermarkt scraper" subfolder contains .txt files used for my own scraper.

Folder "data" contains scraped and merged data for 2017/18-2019/20 seasons, transfers.csv file with data for out-of-sample evaluation, and players_21.csv for players in FIFA 21 analysis.
FIFA 21 dataset comes from https://www.kaggle.com/stefanoleone992/fifa-21-complete-player-dataset


---
You might want to ask me how the final data was prepared?

The code from scrapers itself does not suffice to recreate the whole dataset, although it is undoubtedly a key factor. 
Due to the reasons described in a thesis - certain players just didn't match due to differences in name & surname coding from websites, yet I wanted some to be included - I had to edit data manually.
Manual editing with programming is just uncomfortable compared to Excel, which I decide to use. 
So, I have edited some of names & surnames manually in Excel, and joined the data accordingly using vlookups, instead of merging these with Pandas.

To summarize - my logic was to:
1. Construct data from web scrapers
2. Download data through web scrapers
- my little scraper - data for players values from transfermarkt
- transfermarkt-scraping-master - for data from transfermarkt
- FBRef Scrap Modified - for data from FBRef 
3. Modify several records by hand in Excel
4. Implement vlookups in Excel and join three datasets accordingly
5. Utilize data for further analysis - again in Python

That means that there is no final solution for that case within repository - as it relies on manual work in Excel as well.
Nevertheless, I wanted to deploy web scrapers as these were crucial for my dataset construction.

---
You might want to ask me why I didn't implement scraping player's value functionality in transfermarkt scraping master but created my own scraper instead?

Well... it was quite problematic and I needed to spend my time on other problems. And it worked. Although, having done this project once again I would attempt to implement it.

---
You might want to ask me something more about the project structure?

First of all, this project and a whole code behind it was intended to serve a sole purpose, which is an analysis in my bachelor's thesis. It wasn't intended to be an application itself.
This is why it consists of Notebooks in 99%... :)
If you want to refactor the project into some kind of an application or whatever - feel free to do so.

---
You might want to ask me if I would want to change anything in this project?

I would put a much stronger emphasis on a clean code principles in my Jupyter Notebooks. It does not hold to my current standards. But it worked :)






