import urllib.parse
#from urllib.parse import urlparse
import pandas as pd

BASE = "https://www.be-farmer.jp/experience/intern/search/"

def create_url_list():
	url = BASE + "list/"
	area_num_list = range(9)
	url_list = []
	
	for area_num in area_num_list:
		query = "?area=" + str(area_num)
		url = urllib.parse.urljoin(url, query)
		url_list.append(url)

	return url_list

#def create_url_detail():

print(create_url_list())


