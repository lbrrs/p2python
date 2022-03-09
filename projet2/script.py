import requests
from bs4 import BeautifulSoup
import csv

url = "http://books.toscrape.com/index.html"


def extract_category_data(url):

    reponse = requests.get(url)
    soup = BeautifulSoup(reponse.content, 'html.parser')

    link_category = []
    text_category =  []
    category = soup.find("ul", class_='nav')

    extract_category = dict()

    for link in category.findAll('a'):
        link_category.append('http://books.toscrape.com/' + link.get('href'))

    for text in category.text:
        text_category.append(text)
    
    extract_category[text] = link_category
    '''print(extract_category)'''
        
    return extract_category

data = extract_category_data(url)



url_category = "http://books.toscrape.com/catalogue/category/books_1/index.html"

def extract_book_link(url_category):

    reponse = requests.get(url_category)
    soup = BeautifulSoup(reponse.content, 'html.parser')

    link_book = []
    category = soup.find("div", class_='image_container')

    extract_book = dict()

    for link in category.findAll('a'):
        link_book.append('http://books.toscrape.com/catalogue/' + link.get('href').replace('../', ''))

    '''print(link_book)'''

    return link_book

url_book = extract_book_link(url_category)



book = 'http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html'

def extract_book_data(book):

    reponse = requests.get(book)
    soup = BeautifulSoup(reponse.content, 'html.parser')

    data_book = []

    title = soup.title.string
    img = soup.img
    price = soup.find("p", class_="price_color")
    stock = soup.find("p", class_="instock")

    th = soup.find_all("th")
    th_textes = []
    for characteristic in th:
        th_textes.append(characteristic.string)

    td = soup.find_all("td")
    td_textes = []
    for data in td:
        td_textes.append(data.string)

    category = soup.find_all("a")
    category_textes = []
    for texte in category:
        category_textes.append(texte.string)

    stars = soup.find("p", class_="Three")

    description = soup.find_all("p")
    p_texte = []
    for texte in description:
        p_texte.append(texte.string)
    
    universal_product_code = td_textes[0]

    price_including_tax = td_textes[2]
    price_excluding_tax = td_textes[3]
    number_available = td_textes[5]
    
    print(title)
    print(img["src"].replace('../../', 'http://books.toscrape.com/'))
    print(price.text)
    print(stock.text)
    print(th_textes)
    print(td_textes)
    print(category_textes[-1])
    print(stars)
    print(p_texte[3])

    return data_book

data_book = extract_book_data(book)


def main():

    header = ['Category_name', 'Category_URL', 'Category_books', 'product_page_url', 'title', 'image_url', 'price_including_tax', 'price_excluding_tax', 'number_available', 'product_description', 'review_rating', 'universal_ product_code']
    data = [text_category, ]

    with open('books.csv','w',encoding='UTF8', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(header)
        csv_writer.writerow(data)

    return main

file_projet = main()


    
