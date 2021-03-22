import os
import numpy as np
import pandas as pd
import spacy
from processing_modules.io_data import ImportData

class AccountVectorizer:

    def __init__(self, data_frame):
        self.df = data_frame

    def filter_tweet_language(self, language='English'):
        self.df = self.df[self.df.language == language]


