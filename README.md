# Information Warfare: Russia's use of Twitter during the 2016 US Presidential Election (work in progress)

On July 31, 2018, the website FiveThirtyEight [published nearly 3 million tweets](https://fivethirtyeight.com/features/why-were-sharing-3-million-russian-troll-tweets/) sent from Twitter handles connected to the Internet Research Agency(IRA), a Russian "troll factory" and a defendant in an indictment filed by the Justice Department in February 2018, as part of special counsel Robert Mueller's Russia investigation. 

The [data](https://github.com/fivethirtyeight/russian-troll-tweets/) is the work of Clemson University researchers [Darren Linvill](https://www.clemson.edu/cbshs/faculty-staff/profiles/darrenl) and [Patrick Warren](http://pwarren.people.clemson.edu/) who, using advanced social media tracking software and the assistance of the Clemson University Social Media Listening Center, pulled the tweets from thousands of accounts that Twitter has acknowledged as being associated with the IRA - sent between February 2012 and May 2018, with the vast majority posted from 2015 through 2017.

In a working paper, [Troll Factories: The Internet Research Agency and State-Sponsored Agenda Building](http://pwarren.people.clemson.edu/Linvill_Warren_TrollFactory.pdf), the Clemson researchers discuss the qualitative procedure employed to divide the IRA’s trolling into five distinct categories, or roles, according to language and behavior: Right Troll, Left Troll, News Feed, Hashtag Gamer and Fearmonger. (These category codes are included in the data.)

**Using the [data](https://github.com/fivethirtyeight/russian-troll-tweets/), this project aims to:**

* test whether the Clemseon researchers' categorization scheme can be replicated using unsupervised learning; and
* investigate whether multi-class classifcation models can be trained to label Twitter handles in an unlabeled data set of Russian troll tweets. 

**The Jupyter Notebook associated with this project can be viewed as rendered by [Jupyter nbviewer](https://nbviewer.jupyter.org/github/benforleo/disinformation_project/blob/master/labeled_tweets.ipynb).**

**Tools:** Python (spaCy, gensim, Pandas, Scikit-Learn, Imblearn, Plotly) 
**Techniques:** doc2vec, t-SNE, KMeans, Gaussian Mixture Models, SMOTE, Logistic Regression, SVM, Random Forrest, XGboost

## Authors and contributors
* [Benjamin R. Forleo](https://github.com/benforleo)
