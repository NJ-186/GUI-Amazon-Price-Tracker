import bs4
from urllib.request import urlopen
from urllib.request import Request
from bs4 import BeautifulSoup

class Track:
    def start_scrape(myLink):
        req = Request(myLink, headers={'User-Agent': 'Mozilla/5.0 (Linux; <Android Version>; <Build Tag etc.>) AppleWebKit/<WebKit Rev> (KHTML, like Gecko) Chrome/<Chrome Rev> Mobile Safari/<WebKit Rev>'})

        uclient  = urlopen(req, timeout=10)

        page_html = uclient.read()

        uclient.close()	#closing the connection

        pagesoup = BeautifulSoup(page_html,"html.parser")

        price = pagesoup.find(id='priceblock_ourprice').get_text()

        final_price = float(price[2:])

        return final_price

    def stop_scrape():
        print('scrapping stopped')
        exit()

