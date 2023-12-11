# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 14:44:53 2023

@author: Joseph Prieto
@Description:
    This code scrapes the american aed website to extract review data. If the structure of the 
    website changes, this code may need to be altered.
"""
from selenium import webdriver
import requests 
from bs4 import BeautifulSoup 
from dateutil.parser import parse
from datetime import datetime
import csv
import time
import emoji

  
#Initializing variables to be used later on in the code
review_id = 1
csv_filename = 'AED_medical_device_reviews.csv'
url = 'https://www.resellerratings.com/store/americanaed_com'
source = 'https://americanaed.com/'
header = ["reviewId","reviewer","datePublished","starRatingOutOfFive","reviewTitle","reviewComment","source"]
page =1
url_to_use = url
#Start by opening my csv file to beigin writing to it
with open(csv_filename,'w') as csv_file:
    writer=csv.writer(csv_file, delimiter='\t',lineterminator='\n',)
    writer.writerow(header)
    #while the web page exists keep iterating through pages
    while requests.get(url_to_use).status_code == 200:
        url_to_use = url+'/page/'+str(page)
        #check if webpage exists
        if requests.get(url_to_use).status_code == 404:
            break
        driver = webdriver.Chrome()  
        if page==1:
            driver.get(url)
        else:
            driver.get(url_to_use)
        
        # Get page source after dynamic content is loaded
        time.sleep(1)
        r = driver.page_source
        
        # Close the Selenium-controlled browser
        driver.quit()
        # Parsing the HTML 
        soup = BeautifulSoup(r, 'html.parser') 
        
        #get list of reviews
        List = soup.find_all("div",{"class":"grid-x review store-review"}) 
    
        #Iterate through reviews in list
        for entry in List:
            print()
            print("NEW REVIEW")
            #Grab elements neccessary for data set
            reviewer = entry.find("div",{"class":"user-name"})
            starRating = entry.find("span",{"class":"starRating"})
            date = entry.find("span",{"class":"date"})
            title = entry.find("div",{"class":"cell review-title centered-medium"})
            comment = entry.find("div",{"class":"cell review-body centered-medium"})
            #Clean strings
            #Clean reviewer string
            reviewer_clean = reviewer.text.strip()
            #Clean star rating string
            starRating_clean = starRating.text.split('/',1)[0].strip()
            #clean date string
            if ':' in date.text:
                dt = date.text.split(":",1)[1]
            else:
                dt = date.text
            dt = parse(dt)
            dt= dt.strftime('%m/%d/%Y')
            #clean title string
            title_clean = title.text.strip('""')
            #clean comment string
            comment_clean = comment.text.strip('""')
            comment_clean = emoji.demojize(comment.text.strip())
            print(reviewer_clean)
            print(starRating_clean)
            print(dt)
            print(title_clean)
            print(comment_clean)
            #Write to csv
            writer.writerow([review_id,reviewer_clean,dt,starRating_clean,title_clean,comment_clean,source])
            review_id+=1
        page+=1
    
    
    
    
    
    
