# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 15:26:47 2015

@author: tomhope
"""
import cPickle as pickle
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import CountVectorizer
import re

def tokenize_speeches(text):
    text = re.sub('[\[\]<>\'\+\=\/(.?\",&*!_#:;@$%|)0-9]'," ", text)
    
    text = ' '.join(text.split())
    text = word_tokenize(text)
    
    tokens = [re.sub(r'(?<![\x00-\x9F])[-]',"", t.encode("UTF-8")).decode("UTF-8") for t in text if len(t)>=2]
    tokens = [re.sub(r'[-](?![\x00-\x9F])',"", t.encode("UTF-8")).decode("UTF-8") for t in tokens if len(t)>=2]

    
    return tokens
  
ss = tokenize_speeches(bibi_speeches[0])  
for s in ss[0:10]:
    print s

count_vect = CountVectorizer(ngram_range = (1,2), max_df = 0.75, min_df = 10,
                             tokenizer = tokenize_speeches)
                             
X_train_counts = count_vect.fit_transform(bibi_speeches)
                            
h = count_vect.get_feature_names()[0:20]
print h

ss = count_vect.get_feature_names()
for i in range(600,700):
    print ss[i]
