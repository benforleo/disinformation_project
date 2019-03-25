#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 10:44:09 2019

@author: benjaminforleo
"""

# %%
# hashtage_pipe

def hashtag_pipe(doc):
    """Create a hashtag token by merging the # token and relevant text"""
    
    import re
    indexes = [m.span() for m in re.finditer('#[A-Za-z0-9]*', doc.text ,flags=re.IGNORECASE)]
    
    for start,end in indexes:
        doc.merge(start_idx=start,end_idx=end)
      
    pattern = re.compile('#.*')
    for token in doc:
        if bool(re.match(pattern, token.text)):
            token._.is_hashtag = True
    
    return doc
        
# %%
# flag user accounts

def is_account_pipe(doc):
    
    """Flag user accounts with custom .is_account attribute"""
    
    import re
    
    pattern = re.compile("@.*")
    
    for token in doc:
        if bool(re.match(pattern, token.text)):
            
            token._.is_account = True 
    
    return doc

# %% clean and lemmatise each document doc

def clean_doc(doc):
    
    from spacy.lang.en.stop_words import STOP_WORDS
    import re
    import string
    
    #more_stops = ['i', 'it', 'him', 'they', 'he', 'her', 'its', 'be', 'the', 'you',
    #             'not', 'we', 'a', 'me', 'like', 'his', 'this']
    pattern = re.compile('\.+')
    
    token_list = []
    
    for token in doc:
        if token._.is_account or token._.is_hashtag:
            token_list.append(token.text)
            
        elif (token.lemma_ != "-PRON-") and (not token.is_punct) and (not token.is_space) \
        and (not bool(re.fullmatch(pattern, token.lemma_)))\
        and (not token.is_stop) and (not token.lemma_ == '�'):
            
            token_list.append(token.lemma_.lower().strip())
            
        elif token.lemma_ == "-PRON-":
            
            token_list.append(token.lower_)
        
    
    #token_list = [token for token in token_list if token not in more_stops]
            
    
    return token_list


# %% clean doc with no lemmatization

def clean_doc_no_lemma(doc):
    
    import re
    import string
    punctuations = string.punctuation
    
    token_list = []
    
    for token in doc:
        if token._.is_account or token._.is_hashtag:
            token_list.append(token.text)
            
        elif (token.text.strip() not in punctuations) and (token.text.strip != ""):
            
            token_list.append(token.lower_)
            
    return token_list




# %%
## remove weblinks and RT symbol

def clean_doc_old(doc):
    
    """Removes hyperlinks, the RT indicator, punctuation and stop words. 
    Returns lowercase lemmatized words"""
    
    from spacy.lang.en.stop_words import STOP_WORDS
    import re

    link_pattern = re.compile("(http|ftp|https)://([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])?")

    token_list = []

    for token in doc:
    
        if token._.is_account or token._.is_hashtag:
            token_list.append(token.text)
  
        elif (token.text != "RT") \
        and not(token.text in STOP_WORDS) \
        and not bool(re.match(link_pattern, token.text)) \
        and not(token.is_punct):
            token_list.append(token.lower_)
     
    return token_list

#%%

def rt_remover(doc):
    
    import re
    
    rt_pattern = re.compile("RT ")
    
    less_rt = re.sub(rt_pattern, "", doc)
        
    return less_rt

# %%

def link_remover(doc):
    
    import re
    
    link_pattern = re.compile(
        "(http|ftp|https)://([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])?")
    
    less_link = re.sub(link_pattern, "", doc)
    
    return less_link

# %%

def lower_case(doc):
    
    """Returns the lowercase form of a token"""
    
    token_list = []
    
    for token in doc:
        
        token_list.append(token.lower_)
        
    return token_list

# %% flattens a lists of lists into a single list

def group_lists(l):
    
    return [item for sublist in l for item in sublist]
    
    
        
        

        
        
        
    
    



    