# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 14:44:53 2023

@author: Joseph Prieto
@Description:
    This code scrapes the concord health supply website to extract review data. If the structure of the 
    website changes, this code may need to be altered.
"""
from selenium import webdriver 
from bs4 import BeautifulSoup 
from dateutil.parser import parse
from datetime import datetime
import csv
import time
import emoji
  

#Initializing variables to be used later on in the code
review_id = 1
csv_filename = 'concord_medical_device_reviews.csv'
href_str = "ProductDetails.asp?ProductCode=75026"
url_iterator = 'https://www.concordhealthsupply.com/ReviewsList.asp?SortBy=Newest&Page=1&ProductCode=75023&Reviews=Y'
base_url = 'https://www.concordhealthsupply.com/ReviewsList.asp?SortBy=Newest&Page=1&ProductCode=75023&Reviews=Y'
source = 'https://www.concordhealthsupply.com/'
header = ["reviewId","reviewer","reviewerLocation","datePublished","starRatingOutOfFive","reviewTitle","reviewComment","product","source"]
#Product codes to iterate through by replacing in the url
product_codes = ['75023','75026','NON-9590','CCI-300','CCI-BLACK-OX','CCI-BLACK-OX-DLX','CCI-300C3-BLUE-DLX',
                 'CCI-50DL','75006','75004','75071','75028','10975']
#Start by opening my csv file to beigin writing to it
with open(csv_filename,'w',encoding="utf-8") as csv_file:
    writer=csv.writer(csv_file, delimiter='\t',lineterminator='\n',)
    writer.writerow(header)
    #Iterate through product codes
    for product_code in product_codes:
        #Need to extract number of pages and product name first
        url_to_use = base_url.replace("&ProductCode=75023","&ProductCode="+product_code)
        driver = webdriver.Chrome()  # Use appropriate webdriver here (e.g., Chrome, Firefox)
        driver.get(url_to_use)
        r = driver.page_source
        driver.quit()
        soup = BeautifulSoup(r, 'html.parser') 
        #Extract the number of pages of reviews available
        page_num = soup.find("font",{"face":"Arial","size":"2"})
        num_pages = int(page_num.text.split('of',1)[1])
        href_str_to_use = href_str.replace("?ProductCode=75026","?ProductCode="+product_code)
        #Extract the product name from the webpage
        product_name_element = soup.find("a",{"href":href_str_to_use}) 
        product = product_name_element.text.strip()
        product =product.split('to',1)[1].strip()
        #Loop through pages
        for page in range(1,num_pages+1):
            url_to_use = url_iterator.replace("Newest&Page=1","Newest&Page="+str(page))
            url_to_use = url_to_use.replace("&ProductCode=75023","&ProductCode="+product_code)
            # Use Selenium to load the page
            driver = webdriver.Chrome()  # Use appropriate webdriver here (e.g., Chrome, Firefox)
            driver.get(url_to_use)
            # Get page source after dynamic content is loaded
            time.sleep(1)
            r = driver.page_source
            
            # Close the Selenium-controlled browser
            driver.quit()
            # Parsing the HTML 
            soup = BeautifulSoup(r, 'html.parser') 
              
              
            #Grab all of the reviews available on the page
            List = soup.find_all("table",{"id":"product_reviews_description_box"}) 
            #Iterate through the reviews in list
            for entry in List:
                print()
                print("NEW REVIEW")
                #Grab elements containing field required for data set
                title = entry.find("b")
                date_shopper_combo = entry.find_all("i")
                starRating = title.find("img")
                comment = entry.find_all("td",{"width":"100%","valign":"top"})
                #string operations to clean data
                #clean comment string
                sub1 = date_shopper_combo[1].text
                sub2 = "Was this review helpful to you"
                raw_comment = comment[1].text
                idx1 = raw_comment.index(sub1)
                idx2 = raw_comment.index(sub2)
                extractedComment = raw_comment[idx1 + len(sub1) + 1: idx2]
                extractedComment = emoji.demojize(extractedComment.strip())
                #Clean reviwer String
                Reviewer_clean = date_shopper_combo[1].text.strip()
                Reviewer_clean = Reviewer_clean.replace('Reviewer:','').strip()
                if 'from' in Reviewer_clean.split():
                    location = Reviewer_clean.split("from",1)[1]
                    Reviewer_clean = Reviewer_clean.split("from",1)[0]
                else:
                    location = ''
                loaction= location.strip(',')
                #Clean star rating string
                StarRating_clean = starRating['alt']
                StarRating_clean = StarRating_clean.split(" of ",1)[0].strip()
                #Clean date string 
                Date = date_shopper_combo[0].text
                dt = parse(Date)
                dt= dt.strftime('%m/%d/%Y')
                #Clean Title string
                Title_clean = title.text.strip()
                print("Shopper",Reviewer_clean)
                print("starRating",StarRating_clean)
                print("Date",dt)
                print("comment",extractedComment)
                print("Title",Title_clean)
                print("Location",location)
                #Write to csv
                writer.writerow([review_id,Reviewer_clean,location,dt,StarRating_clean,Title_clean,extractedComment,product,source])
                review_id+=1
        
        
        
    




