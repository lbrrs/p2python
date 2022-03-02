import requests
from bs4 import BeautifulSoup

url = "http://books.toscrape.com/index.html"


def extract_category_data(url):

    reponse = requests.get(url)
    soup = BeautifulSoup(reponse.content, 'html.parser')

    link_category = []
    category = soup.find("ul", class_='nav')

    extract_category = dict()

    for link in category.findAll('a'):
        link_category.append('http://books.toscrape.com/' + link.get('href'))
    
    extract_category[category.text] = link_category
    '''print(extract_category)'''
        
    return extract_category

data = extract_category_data(url)

def extract_book_link(link_category):

    reponse = requests.get(link_category)
    soup = BeautifulSoup(reponse.content, 'html.parser')

    link_book = []
    category = soup.find("div", class_='image_container')

    extract_book = dict()

    for link in category.findAll('a'):
        link_book.append('http://books.toscrape.com/catalogue/' + link.get('href'))


    print(category)

    return extract_book



    
