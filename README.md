# Information Warfare: Russia's use of Twitter during the 2016 US Presidential Election

On July 31, 2018, the website
FiveThirtyEight [published nearly 3 million tweets](https://fivethirtyeight.com/features/why-were-sharing-3-million-russian-troll-tweets/)
sent from Twitter handles connected to the Internet Research Agency(IRA), a Russian "troll factory" and a defendant in
an indictment filed by the Justice Department in February 2018, as part of special counsel Robert Mueller's Russia
investigation.

The [data](https://github.com/fivethirtyeight/russian-troll-tweets/) is the work of Clemson University
researchers [Darren Linvill](https://www.clemson.edu/cbshs/faculty-staff/profiles/darrenl)
and [Patrick Warren](http://pwarren.people.clemson.edu/) who, using advanced social media tracking software and the
assistance of the Clemson University Social Media Listening Center, pulled the tweets from thousands of accounts that
Twitter has acknowledged as being associated with the IRA - sent between February 2012 and May 2018, with the vast
majority posted from 2015 through 2017.

In a working
paper, [Troll Factories: The Internet Research Agency and State-Sponsored Agenda Building](http://pwarren.people.clemson.edu/Linvill_Warren_TrollFactory.pdf)
, the Clemson researchers discuss the qualitative procedure employed to divide the IRA’s trolling into five distinct
categories, or roles, according to language and behavior: Right Troll, Left Troll, News Feed, Hashtag Gamer and
Fearmonger. (These category codes are included in the data.)

**Using the [data](https://github.com/fivethirtyeight/russian-troll-tweets/), this project aims to:**

* test whether the Clemseon researchers' categorization scheme can be replicated using unsupervised learning; and
* investigate whether multi-class classifcation models can be trained to label Twitter handles in an unlabeled data set
  of Russian troll tweets.

**Tools:** Python (spaCy, gensim, Pandas, Scikit-Learn, Plotly)
<br>**Techniques:** doc2vec, t-SNE, Logistic Regression

## Authors and contributors

* [Benjamin R. Forleo](https://github.com/benforleo)
* [Anna M. Kot](https://github.com/kotanna)

## Project Background

This project was initially conceived as part of Benjamin Forleo’s *Big Data, Analytics, and Political Science*
self-designed course during the Spring 2019 semester at the University of New Hampshire.

**The Jupyter Notebook associated with Benjamin's submission for this course can be viewed as rendered
by [Jupyter nbviewer](https://nbviewer.jupyter.org/github/benforleo/disinformation_project/blob/master/archive/labeled_tweets.ipynb)
.**

## Procedure

The procedure employed in this analysis involves cleaning the text associated with each tweet, aggregating tweets by
account, creating document embeddings and analyzing the results.

<p align="center">
  <img width="800" height="1277.6" src="https://github.com/benforleo/disinformation_project/blob/master/img/disinformation-project-procedure.png?raw=true">
</p>

## Results

|author      |account_category|0          |1          |2          |......      |302        |
|------------|----------------|-----------|-----------|-----------|-----------|-----------|
|10_GOP      |RightTroll      |-0.03119075|0.07216399 |0.002935304|......      |-0.12273663|
|4MYSQUAD    |LeftTroll       |-1.8998734 |-0.6640599 |-0.21586983|......      |-0.43668124|
|AANTIRACIST |LeftTroll       |-0.19144773|-0.3095436 |-0.15882353|......      |-0.2856187 |
|ABIGAILSSILK|HashtagGamer    |-0.4766572 |-0.8711019 |0.7585614  |......      |-0.8887055 |
|ABIISSROSB  |RightTroll      |-0.30114922|-0.6279655 |0.24099341 |......      |-0.40076506|

<p align="center">
  <img width="700" height="500" src="https://github.com/benforleo/disinformation_project/blob/master/img/tsne-docvecs.png?raw=true">
</p>


