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

# %%

## remove weblinks and RT symbol

def clean_doc(doc):
    
    """Removes hyperlinks, the RT indicator, punctuation and stop words. 
    Returns lowercase lemmatized words"""
    
    from spacy.lang.en.stop_words import STOP_WORDS
    import re

    link_pattern = re.compile("(http|ftp|https)://([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])?")

    token_list = []

    for token in doc:
    
        if token._.is_account or token._.is_hashtag:
            token_list.append(token.text)
  
        elif (token.text != "RT") and not(token.text in STOP_WORDS) \
        and not bool(re.match(link_pattern, token.text)) \
        and not(token.is_punct):
            token_list.append(token.lemma_)
     
    return token_list

#%%



    