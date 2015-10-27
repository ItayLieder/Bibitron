# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 15:30:15 2015

@author: User
"""

import pickle
bibi = pickle.load(open('all_speeches.p', 'rb'))

test = 'אל-אקצה'
bibi[0].find(test)

test[1]