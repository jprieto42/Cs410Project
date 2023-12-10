# CS410 Project - Medical Device Reviews Data Set Creation
## Project Description
  The purpose of the project is to create data sets comprised of reviews of medical device sellers and their products. To do this, custom python code was written to scrape the data off of websites, and clean the data as well. The intended use of the data sets created was for sentiment analysis, however it can be used for other Natural Language Processing Purposes as well. I chose to create separate data sets because each source has different fields of information avialable. However, they do have some fields in common and can be combined. To test or run the python code used to create the data sets, simply download the scripts and run them. I ran them from the Spyder IDE.
## Data Sets
A total of 3 data sets were created from 3 different sources.
#### Concord Health Supply Data Set
  This data set was created from the concord health supply website : https://www.concordhealthsupply.com/
  The file format of the data set is a tab delimeted csv file with a size of .
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

