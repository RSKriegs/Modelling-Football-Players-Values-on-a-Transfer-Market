# Modelling Football Players Values on a Transfer Market

This is a repository for my bachelor's thesis on a related topic. 

Folder <code>/code</code> contains the whole code created for data wrangling, analysis, modelling and visualization. 
**The code is a mess of poor quality.** I was writing it in 2019/2020 when I was a complete newbie and used it mainly for final analytics that are included in a bachelor's thesis. 
Anyway:
- Licencjat_DataViz.ipynb contains script that creates analysis and dashboards for I chapter of my bachelor's thesis and significant variables for team performance described in II chapter,
- Licencjat_Fifa21Analysis.ipynb consists of compact analysis of distribution of chosen players' in-game attributes in their relation to age, what is a part of a I chapter.
- Licencjat_Modelling_Goalkeepers.ipynb, Licencjat_Modelling_Defenders.ipynb, Licencjat_Modelling_Midfielders.ipynb, Licencjat_Modelling_Forwards.ipynb are the files where models for each position are created and properly diagnosed, including cross-validation for each.
- Licencjat_Modelling_Gathered gathers the analysis from all above files and models validation, including out-of-sample validation basing on real-life transfers.
- Note that several lines of code have been modified throughout the process of writing the thesis - in order to replicate results in 100%, one would need to change several parameters accordingly (for example - MAE for each league)
- In the end, folder contains subfolder "demo scikit-learn", which consists of Licencjat_NeuralNet_GKExample.ipynb and Licencjat_RegressionsSKLearn_ExampleGK.ipynb files. Those are the files consisting of certain lines of code, with first one creating neural network basing on MLPClassifier algorithm checking if player on a transfermarkt.de is overvalued or undervalued, whereas the second one replicates the linear regression originally created in StatsModels. Each of them has been created for goalkeepers only. These have not been developed further as I have not used them in a final thesis.

Folder <code>/scrapers<code> contains... well, web scrapers, that were used to download data from transfermarkt.de and fbref.com.
Source code for scrapers which I modified accordingly:
https://github.com/vnherdeiro/transfermarkt-scraping (my modifications contained in a folder transfermarkt-scraping-master)
https://github.com/parth1902/Scrape-FBref-data (my modifications contained in a file FBRef_scrap_modified.ipynb)

The main dataset used that I've created for analytics: https://www.kaggle.com/datasets/kriegsmaschine/soccer-players-values-and-their-statistics
I have also used this one - https://www.kaggle.com/stefanoleone992/fifa-21-complete-player-dataset

The code from scrapers itself does not suffice to recreate the whole dataset. Due to the reasons described in a thesis - certain players just didn't match due to differences in name & surname coding from websites, yet I wanted some to be included - I had to edit data manually in some cases.

TODO: update code




