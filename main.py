from bs4 import BeautifulSoup
import requests
from pymongo import MongoClient
import sys


def mongoConnection():
    client = MongoClient()
    db = client.imagesdb
    return db


if 'mongo' in sys.argv:
    db = mongoConnection()


def saveImage(name, db):
    temp = db.images.find_one({'name': name})
    if(temp is None):
        db.images.insert({'name': name, 'count': 1})
    else:
        db.images.update({'name': name}, {'$inc': {'count': 1}})


def saveImageFolder(url):
    resp = requests.get('https:' + url)
    file = open('images/'+url.split('/')[-1], 'wb')
    file.write(resp.content)
    file.close()


def save_image_names(url):
    site = requests.get(url)
    soup = BeautifulSoup(site.text, 'html.parser')
    for img in soup.find_all('a', attrs={"class": "image"}):
        image = img.find('img')
        image['src']
        if 'mongo' in sys.argv:
            saveImage(image['src'], db)
        if 'print' in sys.argv:
            print(image['src'])
        if 'download' in sys.argv:
            saveImageFolder(image['src'])


def main():
    name_file = sys.argv[1]
    links = open('links' + name_file + '.txt', 'r')
    open('cont' + name_file + '.txt', 'a')
    cont = open('cont' + name_file + '.txt', 'r')

    continua = []

    for c in cont:
        continua.append(c.replace('\n', ''))

    for link in links:
        url = link.replace('\n', '')
        if(url not in continua):
            save_image_names(url)
            cont = open('cont' + name_file + '.txt', 'a').write(url+'\n')


main()
