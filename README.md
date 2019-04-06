# Information Warfare: Russia's use of Twitter during the 2016 US Presidential Election (work in progress)

On August 27, 2018, the data journalism organization FiveThirtyEight published 2,973,371 tweets from accounts identified as being part of a Russian bid to sow discord and spread misinformation online during the 2016 US presidential election. The dataset is largely the product of work done by Clemson University Professors Darren Linville and Patrick Warren who collected the data from Clemson University's Social Media Listening center. The researchers also classifed accounts according to their language and behavior: categories include Right Troll, Left Troll, News Feed, Hashtag Gamer, and Fearmonger.

In a [working paper](http://pwarren.people.clemson.edu/Linvill_Warren_TrollFactory.pdf) describing their work, Linville and Warren discuss the qualitiative procedure that they employed to label accounts.

The purpose of this project is to test whether Linville and Warren's account categorization scheme can be replicated quantitatively using unsupervised learning techniques.

#### To view the jupyter file with working Plotly visuals, click [here](https://nbviewer.jupyter.org/github/benforleo/disinformation_project/blob/master/labeled_tweets.ipynb)


Tools: Python (spaCy, gensim, Pandas, Scikit-Learn, Plotly) 

Techniques: doc2vec, t-SNE, KMeans, Gaussian Mixture Models

