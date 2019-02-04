
#### Hello everyone, and welcome to my first blog post! 

The purpose of this blog is to document my progress on a self-designed school project at the University of New Hampshire where I will examining [tweets](https://about.twitter.com/en_us/values/elections-integrity.html#data) identified as being part of the Russian disinformation campaign during the 2016 US presidential election. This data was released in October 2018 by Twitter and includes 1.24 GB of tweet information and 296 GB of image, GIF, video, and periscope broadcast data. 

Since this data was released, a number of reports have been published examining the methods of the Internet Research Agency, an organization run by a close Putin ally which is believed to be behind the  aforementioned disinformation campaign on various social media platforms, including Twitter. These reports include two commissioned by the Senate Intelligence Committee: [*The IRA Social Media and Political Polarization in the United States, 2012-2018*](https://int.nyt.com/data/documenthelper/534-oxford-russia-internet-research-agency/c6588b4a7b940c551c38/optimized/full.pdf#page=1) by the Computational Propaganda Research Project at the Oxford Internet Institute, and [*The Tactics and Tropes of the Internet Research Agency*](https://int.nyt.com/data/documenthelper/533-read-report-internet-research-agency/7871ea6d5b7bedafbf19/optimized/full.pdf#page=1) by New Knowledge. For the most part, I will be attempting to replicate the findings of these and other reports as I learn more about different data science techniques including Natural Language Processing, Network Analysis, and Image Processing. 

With that being said, let's get started with some EDA!


```python
import numpy as np
import pandas as pd
import re
pd.set_option('display.max_columns', None)

import os
os.chdir('/Users/benjaminforleo/Box/spring_project/')
```


```python
df = pd.read_csv('ira_tweets_csv_hashed.csv', low_memory = False)
```


```python
print(df.shape)
print("")
print(df.columns)
```

    (9041308, 31)
    
    Index(['tweetid', 'userid', 'user_display_name', 'user_screen_name',
           'user_reported_location', 'user_profile_description',
           'user_profile_url', 'follower_count', 'following_count',
           'account_creation_date', 'account_language', 'tweet_language',
           'tweet_text', 'tweet_time', 'tweet_client_name', 'in_reply_to_tweetid',
           'in_reply_to_userid', 'quoted_tweet_tweetid', 'is_retweet',
           'retweet_userid', 'retweet_tweetid', 'latitude', 'longitude',
           'quote_count', 'reply_count', 'like_count', 'retweet_count', 'hashtags',
           'urls', 'user_mentions', 'poll_choices'],
          dtype='object')



```python
df.iloc[:,7:].head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>follower_count</th>
      <th>following_count</th>
      <th>account_creation_date</th>
      <th>account_language</th>
      <th>tweet_language</th>
      <th>tweet_text</th>
      <th>tweet_time</th>
      <th>tweet_client_name</th>
      <th>in_reply_to_tweetid</th>
      <th>in_reply_to_userid</th>
      <th>quoted_tweet_tweetid</th>
      <th>is_retweet</th>
      <th>retweet_userid</th>
      <th>retweet_tweetid</th>
      <th>latitude</th>
      <th>longitude</th>
      <th>quote_count</th>
      <th>reply_count</th>
      <th>like_count</th>
      <th>retweet_count</th>
      <th>hashtags</th>
      <th>urls</th>
      <th>user_mentions</th>
      <th>poll_choices</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>132</td>
      <td>120</td>
      <td>2013-12-07</td>
      <td>ru</td>
      <td>ru</td>
      <td>RT @ruopentwit: ⚡️У НАС НОВОЕ ВИДЕО! Американе...</td>
      <td>2017-06-22 16:03</td>
      <td>TweetDeck</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>True</td>
      <td>2572896396</td>
      <td>8.779172e+17</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>[]</td>
      <td>[http://ru-open.livejournal.com/374284.html]</td>
      <td>[2572896396]</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>74</td>
      <td>8</td>
      <td>2014-03-15</td>
      <td>en</td>
      <td>ru</td>
      <td>Серебром отколоколило http://t.co/Jaa4v4IFpM</td>
      <td>2014-07-24 19:20</td>
      <td>generationπ</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>False</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>NaN</td>
      <td>[http://pyypilg33.livejournal.com/11069.html]</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>165</td>
      <td>454</td>
      <td>2014-04-29</td>
      <td>en</td>
      <td>bg</td>
      <td>@kpru С-300 в Иране https://t.co/elnu3qLUW7</td>
      <td>2016-04-11 09:20</td>
      <td>TweetDeck</td>
      <td>7.194399e+17</td>
      <td>40807205</td>
      <td>NaN</td>
      <td>False</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>[]</td>
      <td>[https://www.youtube.com/watch?v=9GvpImWxTJc]</td>
      <td>[40807205]</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>165</td>
      <td>454</td>
      <td>2014-04-29</td>
      <td>en</td>
      <td>ru</td>
      <td>Предлагаю судить их за поддержку нацизма, т.к....</td>
      <td>2014-11-22 15:28</td>
      <td>Twitter Web Client</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>False</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>[STOPNazi]</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4430</td>
      <td>4413</td>
      <td>2012-02-25</td>
      <td>ru</td>
      <td>bg</td>
      <td>Предостережение американского дипломата https:...</td>
      <td>2017-03-13 22:08</td>
      <td>Twitter Web Client</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>False</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>3.0</td>
      <td>4.0</td>
      <td>[]</td>
      <td>[https://goo.gl/fBp94X]</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>



It looks like many of these tweets are in Russian. For the natural language processing portion of the project, I'll work entirely with english language tweets. 


```python
en_tweets = df[df.tweet_language == 'en']
```


```python
en_tweets.shape
```




    (3261931, 31)




```python
en_tweets.iloc[:,7:].head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>follower_count</th>
      <th>following_count</th>
      <th>account_creation_date</th>
      <th>account_language</th>
      <th>tweet_language</th>
      <th>tweet_text</th>
      <th>tweet_time</th>
      <th>tweet_client_name</th>
      <th>in_reply_to_tweetid</th>
      <th>in_reply_to_userid</th>
      <th>quoted_tweet_tweetid</th>
      <th>is_retweet</th>
      <th>retweet_userid</th>
      <th>retweet_tweetid</th>
      <th>latitude</th>
      <th>longitude</th>
      <th>quote_count</th>
      <th>reply_count</th>
      <th>like_count</th>
      <th>retweet_count</th>
      <th>hashtags</th>
      <th>urls</th>
      <th>user_mentions</th>
      <th>poll_choices</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>8</th>
      <td>696</td>
      <td>863</td>
      <td>2013-08-06</td>
      <td>en</td>
      <td>en</td>
      <td>As sun and cloud give way to moon and shadow, ...</td>
      <td>2015-02-16 16:19</td>
      <td>Twitter Web Client</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>False</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>10</th>
      <td>103</td>
      <td>218</td>
      <td>2014-03-24</td>
      <td>en</td>
      <td>en</td>
      <td>Down in the comfort of strangers, I...</td>
      <td>2014-07-28 23:02</td>
      <td>vavilonX</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>False</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>11</th>
      <td>103</td>
      <td>218</td>
      <td>2014-03-24</td>
      <td>en</td>
      <td>en</td>
      <td>Im laughing more than i should #USA</td>
      <td>2014-07-28 09:24</td>
      <td>vavilonX</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>False</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>[USA]</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>12</th>
      <td>103</td>
      <td>218</td>
      <td>2014-03-24</td>
      <td>en</td>
      <td>en</td>
      <td>No, I'm not saying I'm sorry</td>
      <td>2014-08-08 00:43</td>
      <td>vavilonX</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>False</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>32</th>
      <td>63</td>
      <td>77</td>
      <td>2014-05-23</td>
      <td>en</td>
      <td>en</td>
      <td>Laugh it all off in your face</td>
      <td>2014-08-17 10:46</td>
      <td>vavilonX</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>False</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>



Great! We've filtered down to tweets containing english text. Let's see how many unique accounts there are from this group.


```python
print("Number of unique accounts with english text:", len(set(en_tweets.userid)))
```

    Number of unique accounts with english text: 3259


Interesting! In the coming weeks, I will be digging into natural language processing and trying to find patterns in the text posted by these accounts. 
