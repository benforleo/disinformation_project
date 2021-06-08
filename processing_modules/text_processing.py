#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 10:44:09 2019

@author: benjaminforleo
"""

from spacy.lang.en.stop_words import STOP_WORDS
import re
import string


def hashtag_token(doc):
    """Create a hashtag token by merging the # token and relevant text"""

    indexes = [m.span() for m in re.finditer(r'#\w+', doc.text, flags=re.IGNORECASE)]

    for start, end in indexes:
        doc.merge(start_idx=start, end_idx=end)

    pattern = re.compile(r'#\w+')
    for token in doc:
        if bool(re.match(pattern, token.text)):
            token._.is_hashtag = True

    return doc


def account_token(doc):
    """Flag user accounts with custom .is_account attribute"""

    pattern = re.compile(r"@\w+")

    for token in doc:
        if bool(re.match(pattern, token.text)):
            token._.is_account = True

    return doc


def lemmatize_and_clean_document(doc):
    """Returns a list of lemmatized list of tokens free of stop words."""

    pattern = re.compile(r'\.+')

    token_list = []

    for token in doc:
        if token._.is_account or token._.is_hashtag:
            token_list.append(token.text)

        elif (token.lemma_ != "-PRON-") \
                and (not token.is_punct) \
                and (not token.is_space) \
                and (not bool(re.fullmatch(pattern, token.lemma_))) \
                and (not token.is_stop) \
                and (not token.lemma_ == '�'):

            token_list.append(token.lemma_.lower().strip())

        elif token.lemma_ == "-PRON-":
            token_list.append(token.lower_)

    return token_list


def clean_document(doc):
    """Returns a list of tokens, without lemmatizing or removing stopwords."""

    pattern = re.compile(r'\.+')

    token_list = []

    for token in doc:
        if token._.is_account or token._.is_hashtag:
            token_list.append(token.text)

        elif (not token.is_punct) \
                and (not token.is_space) \
                and (not bool(re.fullmatch(pattern, token.lemma_))) \
                and (not token.lemma_ == '�'):

            token_list.append(token.lower_.strip())

    return token_list


def retweet_remover(doc):
    """Removes the RT Symbol from a string."""

    rt_pattern = re.compile("RT ")

    less_rt = re.sub(rt_pattern, "", doc)

    return less_rt


def link_remover(doc):
    """ Removes and linkes from a string. """

    link_pattern = re.compile(
        r"(http|ftp|https)://([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])?")

    less_link = re.sub(link_pattern, "", doc)

    return less_link


def lower_case(doc):
    """Returns the lowercase form of a token"""

    token_list = []

    for token in doc:
        token_list.append(token.lower_)

    return token_list


def group_lists(list_of_lists):
    """Flattens a list of lists into a single list. """

    return [item for sublist in list_of_lists for item in sublist]
