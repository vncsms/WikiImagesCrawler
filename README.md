# WikiImagesCrawler

- Install MongoDB
- Install Pypy

  `pip install pymongo`
 
  `pip install requests`
  
  `pip3 install beautifulsoup4`

  or 

  `pip install -r requirements.txt`
  

- To execute: 
	`python main.py 0 mongo download print`

	- The argument `0` will choose the file `links0.txt`. This arguments need to be the first after main.py. If you have a file: `links1.txt` so the argument will be `1`.
	- The argument `mongo` will save the url images in mongo. Otherwise will not save in mongo.
	- The argument `download` will save all images inside the folder `images`. Otherwise not. Be careful what you will download, some images in wikipedia have some weirds and big names. And some articles has a lot of images.
	- The argument `print` will print all url images. Otherwise not.

- The `cont0.txt` file will be necessary to not repeat articles, is file will be generated.
