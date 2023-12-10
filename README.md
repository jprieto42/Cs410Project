# CS410 Project - Medical Device Reviews Data Set Creation
## Project Description
  The purpose of the project is to create data sets comprised of reviews of medical device sellers and their products. To do this, custom python code was written to scrape the data off of websites, and clean the data as well. The intended use of the data sets created was for sentiment analysis, however it can be used for other Natural Language Processing Purposes as well. I chose to create separate data sets because each source has different fields of information available. However, they do have some fields in common and can be combined. To test or run the python code used to create the data sets, simply download the scripts and run them. I ran them from the Spyder IDE.
## Data Sets
A total of 3 data sets were created from 3 different sources.
### Concord Health Supply Data Set
  This data set consists of reviews about specific medical products from the concord health supply website : https://www.concordhealthsupply.com/ .
  The file format of the data set is a tab delimeted csv file with a size x of with x unique rows. The date has a standard format but I was unable to standardize the location strings becuase there aren't very powerful location parsers available. The rest of the strings were striped of newlines and spaces but contain raw text extracted from the websites.
|   | Feature             | Description  | Data Type  |
| - |:-------------------:| ------------:|------------:|
| 1 | reviewId            | Data set Unique Identifier        | Integer       |
| 2 | reviewer            | Username or Name of Reviewer        | String        |
| 3 | reviewerLocation    | Location of reviewer       |    String     |
| 4 | datePublished       | Date that the review was published | String Format: month/day/year       |
| 5 | starRatingOutOfFive | Star rating associated with review(5=best, 1 =worst)        |    Integer      |
| 6 | reviewTitle         | Title of review        |   String      |
| 7 | reviewComment       | Body of review       |    String       |
| 8 | product             | Product associated with review       |   string        |
| 9 | source              | web source of review      |    string      |
### American AED Data Set
  This data set consists of reviews about the service and products from the american aed website : https://americanaed.com/ .
  The file format of the data set is a tab delimeted csv file with a size x of with x unique rows. The date has a standard format. The rest of the strings were striped of newlines and spaces but contain raw text extracted from the websites.
|   | Feature             | Description  | Data Type  |
| - |:-------------------:| ------------:|------------:|
| 1 | reviewId            | Data set Unique Identifier        | Integer       |
| 2 | reviewer            | Username or Name of Reviewer        | String        |
| 3 | datePublished       | Date that the review was published | String Format: month/day/year       |
| 4 | starRatingOutOfFive | Star rating associated with review(5=best, 1 =worst)        |    Integer      |
| 5 | reviewTitle         | Title of review        |   String      |
| 6 | reviewComment       | Body of review       |    String       |
| 7 | source              | web source of review      |    string      |
### TensPro Data Set
  This data set consists of reviews about specific medical products from the tenspro website : https://www.tenspros.com/ .
  The file format of the data set is a tab delimeted csv file with a size x of with x unique rows. The date has a standard format but I was unable to standardize the location strings becuase there aren't very powerfull location parsers available. The rest of the strings were striped of newlines and spaces but contain raw text extracted from the websites. In the reviewComment this data set contains emoji data that was converted into text in some of the entries, so be aware of that when designing your sentiment analysis or NLP code.
|   | Feature             | Description  | Data Type  |
| - |:-------------------:| ------------:|------------:|
| 1 | reviewId            | Data set Unique Identifier        | Integer       |
| 2 | reviewer            | Username or Name of Reviewer        | String        |
| 3 | reviewerLocation    | Location of reviewer       |    String     |
| 4 | datePublished       | Date that the review was published | String Format: month/day/year       |
| 5 | starRatingOutOfFive | Star rating associated with review(5=best, 1 =worst)        |    Integer      |
| 6 | reviewTitle         | Title of review        |   String      |
| 7 | reviewComment       | Body of review       |    String       |
| 8 | product             | Product associated with review       |   string        |
| 9 | source              | web source of review      |    string      |
