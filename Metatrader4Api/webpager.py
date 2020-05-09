from selenium import webdriver
import re
import time
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
class tradedriver:
	def __init__(self):
		self.driver = webdriver.Chrome()
		self.actionChains = ActionChains(self.driver)
		self.driver.get("https://www.mql5.com/en/trading")
		self.frame = self.driver.find_element_by_css_selector('#webTerminalHost')
		self.driver.switch_to_frame(self.frame)	

		self.activeorders_manual=list()

	def read_current_val(self,symbol):
		pass

	def authorize_oneclick(self):
		oneclicktrading=WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'body > div:nth-child(2) > div > div:nth-child(5)')))
		oneclicktrading.click()
		oneclicktrading2=WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'body > div:nth-child(2) > div > div:nth-child(5) > span.box > span')))
		oneclicktrading2.click()
		oneclicktrading3=WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#one-click-accept')))
		oneclicktrading3.click()
		oneclicktrading4=WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'body > div:nth-child(19) > div > div.b > button:nth-child(4)')))
		oneclicktrading4.click()

	def place_order(self,symbol,what,volume,stoploss,takeprofit): # self je samo ime, nerabi bit vedno seflg, lahko je tud slojfer, cevap, j, s , kk ...
		narocilo=self.driver.find_element_by_css_selector('#'+symbol) # odprtje okna za postavitev narocila
		self.actionChains.double_click(narocilo).perform()
		time.sleep(1)
		comment=self.driver.find_element_by_css_selector('#order-ie-dialog-comment')
		comment.click()
		comment.send_keys("order number 1csasf")

		vol=self.driver.find_element_by_css_selector('#order-ie-dialog-volume')
		vol.click()
		vol.send_keys(str(volume))
		if stoploss is not 0:
			stop_loss=self.driver.find_element_by_css_selector('#order-ie-dialog-sl')
			stop_loss.click()
			stop_loss.send_keys(str(stoploss))

		if takeprofit is not 0:
			take_profit=self.driver.find_element_by_css_selector('#order-ie-dialog-tp')
			take_profit.click()
			take_profit.send_keys(str(takeprofit))

		if what=="buy":
			buy= WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'body > div:nth-child(20) > div > div.b > div.page-block > div:nth-child(1) > button:nth-child(16)')))
			buy.click()
		elif what=="sell":
			sell= WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'body > div:nth-child(20) > div > div.b > div.page-block > div:nth-child(1) > button:nth-child(15)')))
			sell.click()
		else:
			raise ValueError('invallid, must be buy or sell')


		if (self.check_exists_by_selector('body > div:nth-child(20) > div > div.b > div.page-block > div:nth-child(1) > button:nth-child(20)')):
			pressaccept = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'body > div:nth-child(20) > div > div.b > div.page-block > div:nth-child(1) > button:nth-child(20)')))
			pressaccept.click()

		getordername=WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'body > div:nth-child(20) > div > div.b > div.page-block > div:nth-child(1) > div:nth-child(14)')))
		ordername=None
		try:
			ordername=re.search(r"(?<=#).*?(?= )", getordername.text).group(0)
			self.orders_maneger("add","position_"+ordername)
		except:
			pass

		pressexit = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'body > div:nth-child(20) > div > div.wx')))
		pressexit.click()
		return ordername
	

	def close_orders(self,ordername):
		order_element=0
		if ordername=="all":
			self.check_for_open_orders()
			for elid in self.activeorders:
					order_element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, elid)))
					order_element.click()
					order_element.click()
		else:
			order_element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, ordername)))
		
	def check_exists_by_selector(self,selector):
		try:
			WebDriverWait(self.driver, 2).until(EC.visibility_of_element_located((By.CSS_SELECTOR, selector)))
		except: 
			return False
		else:
			return True		

	def orders_maneger(self,status,ordername):
		if status=="add":
			self.activeorders_manual.append(str(ordername))
		elif status=="remove":
			pass

	def check_for_open_orders(self):
		if self.check_exists_by_selector('body > div.page-block.frame.bottom > div.ext-table.fixed.odd.grid.no-border.trade-table.toolbox-table.at-trade-table > div.tables-box > table >tbody'):
			activeorders=list()
			orders_table=self.driver.find_element_by_css_selector('body > div.page-block.frame.bottom > div.ext-table.fixed.odd.grid.no-border.trade-table.toolbox-table.at-trade-table > div.tables-box > table >tbody')
			orders_table_names=orders_table.find_elements(By.CLASS_NAME,"filled")
			for ii in orders_table_names:
				ordername=ii.get_attribute('id')
				if ordername !="total":
					activeorders.append(str(ordername))
				else:
					activeorders=list()
			return activeorders
		else:
			return list()
