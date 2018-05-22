from bs4 import BeautifulSoup
import requests
from pymongo import MongoClient
import sys

def mongoConnection():
    client = MongoClient()
    db = client.imagesdb
    return db

db = mongoConnection()

def saveImage(name, db):
	temp = db.images.find_one({'name': name})
	if(temp is None):
	    db.images.insert({'name': name, 'count': 1})
	else:
		db.images.update({'name': name}, {'$inc': {'count': 1}})

def save_image_names(url):
    site = requests.get(url)
    soup = BeautifulSoup(site.text,'html.parser')
    for img in soup.find_all('a',attrs={"class": "image"}):
        saveImage(img['href'],db)


def main():
    name_file = sys.argv[1]
    links = open('links' + name_file + '.txt','r')
    open('cont' + name_file + '.txt','a')
    cont = open('cont' + name_file + '.txt','r')

    continua = []
    
    for c in cont:
         continua.append(c.replace('\n',''))

    for link in links:
        url = link.replace('\n','')
        if(url not in continua):
            save_image_names(url)
            cont = open('cont' + name_file + '.txt','a').write(url+'\n')

main()
