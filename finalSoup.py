import requests
from lxml import etree
import pymongo

url= 'https://www.stepstone.se/lediga-jobb-i-hela-sverige/data-it/sida'
connection = pymongo.MongoClient('localhost:27017') #client host
db = connection.jobdetails #database
db_table = db.jobdetailofstepstone # table

max = 13 # maximum no. f the page till that you want to scrap
min = 1 #minimum no of the pages till you scraped last, also can create a table who record the last fetch details like min
for var in range(min,max,1):
    url = 'https://www.stepstone.se/lediga-jobb-i-hela-sverige/data-it/sida'+str(var)+'/'
    print url #variable url, change min and max to get last and next page data
    response = requests.get(url)
    myparser = etree.HTMLParser(encoding="utf-8")
    tree = etree.HTML(response.text, myparser)
    #length is to determine the total posts in page
    length = len(tree.xpath('/html/body/div[1]/div/section/div[3]/section/article/div[2]/div/span[1]/a'))
    print length
    stringCompany = tree.xpath('/html/body/div[1]/div/section/div[3]/section/article/div[2]/div/span[1]/a/text()')
    stringJobTitle = tree.xpath('/html/body/div[1]/div/section/div[3]/section/article/div[2]/div/h5/a/text()')
    stringLocation = tree.xpath('/html/body/div[1]/div/section/div[3]/section/article/div[2]/div/span[2]/span[2]/text()')
    #working code that will take useful data
    for i in range(0,length):
        companyInDB = stringCompany[i]
        jobTitleInDB = stringJobTitle[i]
        locationInDB = stringLocation[i]
        output = {'title':jobTitleInDB,'company':companyInDB,'location':locationInDB}
        db_table.insert_one(output)
        #database insertion
