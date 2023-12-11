# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 14:44:53 2023

@author: Joseph Prieto
@Description:
    This code scrapes the tenspro website to extract review data. If the structure of the 
    website changes, this code may need to be altered.
"""
from selenium import webdriver
from bs4 import BeautifulSoup 
import time
from dateutil.parser import parse
from datetime import datetime
import csv
import emoji

#Initializing variables to be used later on in the code
review_id = 1
csv_filename = 'tenspro_medical_device_reviews.csv'
base_url = 'https://www.tenspros.com/'
source = 'https://www.tenspros.com/'
header = ["reviewId","reviewer","reviewerLocation","datePublished","starRatingOutOfFive","reviewTitle","reviewComment","product","source"]
#List of urls to iterate through
urls = [
        'https://www.tenspros.com/review.asp?action=listall&catalogid=8',
        'https://www.tenspros.com/review.asp?action=listall&catalogid=12',
        'https://www.tenspros.com/review.asp?action=listall&catalogid=11',
        'https://www.tenspros.com/review.asp?action=listall&catalogid=168',
        'https://www.tenspros.com/review.asp?action=listall&catalogid=689',
        'https://www.tenspros.com/review.asp?action=listall&catalogid=347',
        'https://www.tenspros.com/review.asp?action=listall&catalogid=15',
        'https://www.tenspros.com/review.asp?action=listall&catalogid=23',
        'https://www.tenspros.com/review.asp?action=listall&catalogid=234',
        'https://www.tenspros.com/review.asp?action=listall&catalogid=196',
        'https://www.tenspros.com/review.asp?action=listall&catalogid=63',
        'https://www.tenspros.com/review.asp?action=listall&catalogid=326',
        'https://www.tenspros.com/review.asp?action=listall&catalogid=175',
        'https://www.tenspros.com/review.asp?action=listall&catalogid=627',
        'https://www.tenspros.com/review.asp?action=listall&catalogid=724',
        'https://www.tenspros.com/review.asp?action=listall&catalogid=329',
        'https://www.tenspros.com/review.asp?action=listall&catalogid=73'
]
#Start by opening my csv file to beigin writing to it
with open(csv_filename,'w') as csv_file:
    writer=csv.writer(csv_file, delimiter='\t',lineterminator='\n',)
    writer.writerow(header)
    #Iterate through urls
    for url_to_use in urls:
        # Use Selenium to load the page
        driver = webdriver.Chrome()
        #Here we needed to first access the first url because the url that contains the reviews 
        #needs cookies to be set by accessing the base website to allow us to view them
        driver.get(base_url)
        #Incorporate sleeps so that the webpage has time to load
        time.sleep(2)
        
        driver.get(url_to_use)
        time.sleep(3)
        # Get page source after dynamic content is loaded
        r = driver.page_source
        # Close the Selenium-controlled browser
        driver.quit()
        
        soup = BeautifulSoup(r, 'html.parser') 
        
        #Extracting the product name from the webpage
        product_name_element = soup.find("h1",{"class":"page_headers"}) 
        product = product_name_element.text.strip()
          
        #Finding the list of reviews
        List = soup.find_all("div",{"class":"user_reviews"}) 
        print(List)
        print()
        #Iterate through reviews in list
        for entry in List:
            print()
            print("NEW REVIEW")
            #Grab elements neccessary for data set
            reviewer_date_location = entry.find("em",{"class":"reviewed-by"})
            starRating = entry.find("div",{"class":"star-rating"})
            stars = starRating.find("img")
            title = entry.find("div",{"class":"review-shortDesc"})
            comment = entry.find("div",{"class":"review-longDesc"})
            #Clean strings
            #Clean reviewer, date, and location
            split_text = reviewer_date_location.text.split('from',1)
            reviewer_clean = split_text[0]
            reviewer_clean = reviewer_clean.replace('Reviewed by:','').strip()
            date_location_split = split_text[1].split('\non')
            location_clean = date_location_split[0].strip('\n. ')
            date = date_location_split[1]
            dt = parse(date)
            dt= dt.strftime('%m/%d/%Y')
            #clean stars string
            stars_clean = int(stars['alt'].replace('Stars','').strip())
            #clean title
            title_clean = title.text.strip()
            #clean comment
            comment_clean = emoji.demojize(comment.text.strip())
            print("Reviewer",reviewer_clean)
            print("location",location_clean)
            print("date",dt)
            print("starRating",stars_clean)
            print("Title",title_clean)
            print("comment",comment_clean)
            #Write to csv
            writer.writerow([review_id,reviewer_clean,location_clean,dt,stars_clean,title_clean,comment_clean,product,source])
            review_id+=1
    
        
        
    




