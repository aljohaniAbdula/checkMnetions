#twitter mentioning network Matrix
#goal is to make it up-to-date everytime
#this code is run by a user

#!/usr/bin/env python
# encoding: utf-8
import time
from selenium import webdriver #solve scroll problem????
from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.support.ui import WebDriverWait
#import selenium.webdriver.support.expected_conditions as EC
#from selenium.webdriver.common.by import By
import csv
driver = webdriver.Chrome() # edit to webdriver.PhantomJS("phantomjs")
                            # to utilize phantomjs instead

#take command line argument of file name
'''
try:
    filename = sys.argv[1]
except IndexError:
    filename = "edges.csv"
'''
fd = open('new_edges.csv', 'wb')
#mentioner is from whome the mention, and mentiong is the person
#being mentioned
def get_total_mention(mentioner, mentioning):
    url = u'https://twitter.com/search?f=tweets&q=from%3A'+mentioner+'%20%40'+mentioning+'&src=typd'
    driver.get(url)
    time.sleep(2)
    body = driver.find_element_by_tag_name('body')
    
    for _ in range(400):
        body.send_keys(Keys.PAGE_DOWN)

    #    if driver.find_elements_by_class_name('stream-end-inner'):
    #        next
    #    time.sleep(0.2)
        #if driver.find_elements_by_class_name('stream-end-inner')
        #continue
    tweets = driver.find_elements_by_class_name('tweet-text')

    counter = 0
    for tweet in tweets:
        if not tweet:
            continue
        counter += 1
    results = '%s,%s,%s\n' % (mentioner,mentioning,counter)#outputformat gephi edges
    fd.write(results)
with open(var, 'r') as file1:
    l = []
    for usern in file1:
        usern = usern.rstrip()
        l.append(usern)
    for mentioner in l:
        time.sleep(2) #find best time sleep for twitter
        for mentioning in l: #what's newer way to do nested loop?find
            get_total_mention(mentioner, mentioning)
fd.close()
