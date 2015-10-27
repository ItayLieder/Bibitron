# -*- coding: utf-8 -*-
import urllib2
from bs4 import BeautifulSoup
import sys
import nltk
import cPickle as pickle
from nltk.tokenize import sent_tokenize


var = pickle.load( open( "all_speeches.p", "rb" ) )

"""
Scrapes and extracts Bibi's speeches
Tom Hope and Itay Lieder
"""

"""
%%%%%%%%%%%%%%%%%%%%%%%%%%%%
======== parameters ========
%%%%%%%%%%%%%%%%%%%%%%%%%%%%
"""
#all_speech_list = []
#error_links = []
#num_pages = 49
#
#
#for page in range(num_pages,num_pages+1):
#    home_url = "http://www.pmo.gov.il/MEDIACENTER/SPEECHES/Pages/default.aspx?PN=" + str(page)
#    print page
#    sys.stdout.flush()
#    
#    site = urllib2.urlopen(home_url) # open page
#    print "done opening page"
#    sys.stdout.flush()
#    
#    html = site.read()
#    soup = BeautifulSoup(html,"lxml")
#    link_tags = soup.findAll('a',attrs={'class':"AggMoreDetailsLink"})
#    speech_links = [a.attrs.get('href') for a in link_tags] # get speech link per page
# 
#    for speech_link in speech_links:
#        print speech_link
#        sys.stdout.flush()
#        try:    
#            speech_page = urllib2.urlopen(speech_link)
#        except:
#            print "can't open"
#            error_links.append(speech_link)
#            next;
#        print "done getting speech"
#        sys.stdout.flush()
#        speech_html = speech_page.read()
#        speech_soup = BeautifulSoup(speech_html,"lxml")
#        speech_text = speech_soup.findAll('div',attrs={'class':"contentTXT"})
#        if not speech_text:
#            print("SHITTTT")
#            continue
#        clean_speech = speech_text[0].get_text()
#        all_speech_list.append(clean_speech)
#    name = "bibi_speeches" + str(num_pages) + ".p"   
#    pickle.dump(all_speech_list,open(name, "wb"))

###save to disk

#
#for speech in all_speech_list:
#    all_sentences = sent_tokenize(speech)
#    print "***"
#    print "start: ", all_sentences[0]
#    print "start+1: ", all_sentences[1]
#    print "end: ", all_sentences[-1]
#     
#for sent in sent_tokenize(all_speech_list[0]):
#    print sent
#    print "***"
#
