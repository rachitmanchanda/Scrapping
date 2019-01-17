# import libraries
import urllib.request
from bs4 import BeautifulSoup

x=input('Enter a letter between a to z').rstrip()

# specify the url
my_page='https://www.investopedia.com/terms//'+x

# query the website and return the html to the variable ‘page’
page = urllib.request.urlopen(my_page)

# parse the html using beautiful soup and store in variable `soup`
soup = BeautifulSoup(page,"html.parser")

name_box = soup.find("ol", attrs={"class": "list gaEvent"})

#save it in csv
filename=x+'.csv'
f=open(filename,'w')
headers='terms'
f.write(headers)

for text in name_box:
    name = name_box.text.strip()
    print(name.strip())
    f.write(name.strip())

f.close()
