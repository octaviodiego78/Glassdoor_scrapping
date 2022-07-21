# -*- coding: utf-8 -*-
"""
Created on Mon Jul 18 15:06:18 2022

@author: octav
"""

import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer


def unigrams(df):


    stop_words=['and','a','to','of']    #Add all the words you dont want to count
    word_vectorizer = CountVectorizer(ngram_range=(1,1),lowercase=True,stop_words=stop_words)
    
    #learning the vocabulary dictionary
    matrix = word_vectorizer.fit_transform(df['text'])
    
    #Grouping
    frequencies = sum(matrix).toarray()[0]
    
    #Saving the unigrams as a csv 
    unigrams = pd.DataFrame(frequencies, index=word_vectorizer.get_feature_names(), columns=['frequency'])
    unigrams.to_csv('unigrams.csv')
    
    
def bigrams(df):


    stop_words=['and','a','to','of']    #Add all the words you dont want to count
    word_vectorizer = CountVectorizer(ngram_range=(2,2),lowercase=True,stop_words=stop_words)
    
    #learning the vocabulary dictionary
    matrix = word_vectorizer.fit_transform(df['text'])
    
    #Grouping
    frequencies = sum(matrix).toarray()[0]
    
    #Saving the biigrams as a csv 
    biigrams = pd.DataFrame(frequencies, index=word_vectorizer.get_feature_names(), columns=['frequency'])
    biigrams.to_csv('bigrams.csv')
    

df = pd.read_csv('df.csv')

unigrams(df)
bigrams(df)
