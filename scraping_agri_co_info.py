import urllib.parse
import time
from selenium import webdriver
import pandas as pd

BASE = "https://www.be-farmer.jp/experience/intern/search/"

def create_url_list():
	url = BASE + "detail/"
	area_num_list = range(541)
	url_list = []
	
	for area_num in area_num_list:
		query = "?id=" + str(area_num + 2)
		url = urllib.parse.urljoin(url, query)
		url_list.append(url)

	return url_list

def create_url_detail(url_list):
	
	browser = webdriver.Firefox()
	index_list = []
	contents_lists = []
	browser.get(url_list[0])
	index_res = browser.find_elements_by_css_selector(".type.type-b dd dt")
	for el in index_res:
		index_list.append(el.text)

	for url in url_list:
		content_list = []
		browser.get(url)
		content_res = browser.find_elements_by_css_selector(".type.type-b dd dd")
		for el in content_res:
			content_list.append(el.text)
		contents_lists.append(content_list)
		time.sleep(1)

	df = pd.DataFrame(contents_lists, columns=index_list)
	#df = df["売上高"].str.z2h
	#df = df["従業員数"].str.z2h
	df.to_csv("test.csv")

def main_func():
	url_list = create_url_list()
	print(url_list)
	create_url_detail(url_list)

main_func()
