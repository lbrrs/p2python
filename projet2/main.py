import requests
from bs4 import BeautifulSoup

url = "http://books.toscrape.com/index.html"


def extract_book_data (url):

    reponse = requests.get(url)
    soup = BeautifulSoup(reponse.content, 'html.parser')

    '''
    reponse = requests.get(url)
    # condition si pas de requete
    if reponse is not None:
        soup = BeautifulSoup(reponse.content, 'html.parser')

        extract = dict()

        extract["url"] = url
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
        
        print(extract["url"])
        print(title)
        print(img["src"])
        print(price.text)
        print(stock.text)
        print(th_textes)
        print(td_textes)
        print(category_textes[-1])
        print(stars)
        print(p_texte[3])
    else: print("error")

    return extract
    '''
    extract_category = {}
    category = soup.find("ul", class_='nav')

    for link in category.findAll('a'):
        print('http://books.toscrape.com/' + link.get('href'))
    
    
    

'''
    extract_category["url"] = 'http://books.toscrape.com/' + link.get('href').replace('/n', '')
    print(extract_category)

    for url_book in extract_category:
        extract_category.findAll('h3')
'''



data = extract_book_data(url)
