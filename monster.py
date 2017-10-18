import requests
from lxml import etree
import pymongo
url= 'https://www.monster.se/jobb/sok/Data-IT_4?intcid=swoop_BrowseJobs_Data-IT&page='
connection = pymongo.MongoClient('localhost:27017') #local host connection with database
db = connection.jobdetails #database name
db_table = db.jobdetailofmonster #table name
max = 4 # maximum no. f the page till that you want to scrap
min =1 #minimum no of the pages till you scraped last, also can create a table who record the last fetch details like min
for var in range(min,max,1):
    url = 'https://www.monster.se/jobb/sok/Data-IT_4?intcid=swoop_BrowseJobs_Data-IT&page='+str(var)
    print url #dynamic url
    response = requests.get(url)
    myparser = etree.HTMLParser(encoding="utf-8")
    tree = etree.HTML(response.text, myparser)

    length = len(tree.xpath('//*[@id="resultsWrapper"]/div/article/div[2]/h2/a/span'))
    print length #no. of posted jobs on a var number page
    stringJobTitle = tree.xpath('//*[@id="resultsWrapper"]/div/article/div[2]/h2/a/span/text()')
    stringCompany = tree.xpath('//*[@id="resultsWrapper"]/div/article/div[3]/a/span/text()')
    stringLocationOriginal = []
    xpath_one = '//*[@id="resultsWrapper"]/div/article/div[4]/descendant-or-self::*/text()'
    xpath_two = '//*[@id="resultsWrapper"]/div/article/div[4]/text()'
    stringLocation = tree.xpath(xpath_one)
    print stringLocation

    for i in range(0,length):
        companyInDB = stringCompany[i]
        jobTitleInDB = stringJobTitle[i]
        locationInDB = stringLocation[i]
        print companyInDB,' IS COMPANY AND TITLE IS ',jobTitleInDB,'AND LOCATIONS ARE',locationInDB
        # details = {'title':jobTitleInDB,'company':companyInDB,'location':locationInDB}
        # db_table.insert_one(details) #database insertion
#/html/body/div[4]/div[1]/div/div/div/div/div[2]/div/div[2]/section/div[2]/article/div[4]/a
#/html/body/div[4]/div[1]/div/div/div/div/div[2]/div/div[2]/section/div[4]/article/div[2]/h2/a/span