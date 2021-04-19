Folder "scrapers" contains... well, web scrapers, that were used to download data from transfermarkt.de and fbref.com.
Source code for scrapers which I modified accordingly:
https://github.com/vnherdeiro/transfermarkt-scraping (my modificiations contained in a folder transfermarkt-scraping-master modified)
https://github.com/parth1902/Scrape-FBref-data (my modifications contained in a file FBRef_scrap_modified.ipynb)
Inclues my own scraper for players values on Transfermarkt (My Little Transfermarkt Scrapper Python.ipynb).

Folder "data" contains scraped and merged data for 2017/18-2019/20 seasons, transfers.csv file with data for out-of-sample evaluation, and players_21.csv for players in FIFA 21 analysis.
FIFA 21 dataset comes from https://www.kaggle.com/stefanoleone992/fifa-21-complete-player-dataset

Folder "teams" contains .txt files used for my own scraper.

Folder "code" contains the whole code created for data wrangling, analysis, modelling and visualization. 
- Licencjat_DataViz.ipynb contains script that creates analysis and dashboards for I chapter of my bachelor's thesis and significant variables for team performance described in II chapter,
- Licencjat_Fifa21Analysis.ipynb consists of compact analysis of distribution of chosen players' in-game attributes in their relation to age, what is a part of a I chapter.
- Licencjat_Modelling_Goalkeepers.ipynb, Licencjat_Modelling_Defenders.ipynb, Licencjat_Modelling_Midfielders.ipynb, Licencjat_Modelling_Forwards.ipynb are the files where models for each position are created and properly diagnosed, including cross-validation for each.
- Licencjat_Modelling_Gathered gathers the analysis from all above files and models validation, including out-of-sample validation basing on real-life transfers.
- Note that several lines of code have been modified throughout the process of writing the thesis - in order to replicate results in 100%, one would need to change several parameters accordingly (for example - MAE for each league)
- In the end, folder contains subfolder "demo scikit-learn", which consists of Licencjat_NeuralNet_GKExample.ipynb and Licencjat_RegressionsSKLearn_ExampleGK.ipynb files. Those are the files consisting of certain lines of code, with first one creating neural network basing on MLPClassifier algorithm checking if player on a transfermarkt.de is overvalued or undervalued, whereas the second one replicates the linear regression originally created in StatsModels. Each of them has been created for goalkeepers only. These have not been developed further as I have not used them in a final thesis.

The work is finished, although I intend to update the models after the end of 2020/21 season. 
Bachelor's thesis itself will be included in a repository after I defend it.
