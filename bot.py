from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


class AmazonBot(object):
	"""docstring for TwitterBot"""
	def __init__(self):
		self.bot = webdriver.Firefox(executable_path = '/Users/dipali/opt/anaconda3/lib/python3.7/geckodriver')

	def start_scrape(self,myLink):
		bot = self.bot
		bot.get(myLink)
		time.sleep(5)

		bot.execute_script('window.scrollTo(0,document.body.scrollHeight);')

		time.sleep(2)

		price = bot.find_element_by_xpath('//*[@id="priceblock_ourprice"]').text

		final_price = price[2:7]

		return(final_price)

		bot.quit()





