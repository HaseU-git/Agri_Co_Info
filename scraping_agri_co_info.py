import urllib.parse
import time
from selenium import webdriver
import pandas as pd

BASE_URL = "https://www.be-farmer.jp/experience/intern/search/"
CSV_NAME = "result.csv"
DIR = "./"
COMPANY_NUM = 541
CONTENT_SELECOTR = ".type.type-b dd dd"
COLUMNS_SELECOTR = ".type.type-b dd dt"
INTERVAL = 1

def create_url_list():
	url = BASE_URL + "detail/"
	company_id_list = range(COMPANY_NUM)
	url_list = []
	
	for company_id in company_id_list:
		# id=0, id=1は会社が割り当てられていないため
		query = "?id=" + str(company_id + 2)
		url = urllib.parse.urljoin(url, query)
		url_list.append(url)

	return url_list

def create_parsed_list(url, selector, driver):
	ret_list = []

	driver.get(url)
	res = driver.find_elements_by_css_selector(selector)
	for el in res:
		ret_list.append(el.text)

	time.sleep(INTERVAL)

	return ret_list


def create_ret_df(url_list):
	columns_list = []
	contents_lists = []

	driver = webdriver.Firefox()

	index_list = create_parsed_list(url_list[0], COLUMNS_SELECOTR, driver)

	for url in url_list:
		contents_list = create_parsed_list(url, CONTENT_SELECOTR, driver)
		contents_lists.append(contents_list)

	df = pd.DataFrame(contents_lists, columns=columns_list)

	return df

def main_func():
	url_list = create_url_list()
	df = create_ret_df(url_list)
	df.to_csv(DIR + CSV_NAME)

main_func()
