import urllib2
import csv
from bs4 import BeautifulSoup
import requests

soup = BeautifulSoup(open("AppAnnie_iOS_Games_500_US.html"))

paid_apps = soup.findAll('td',{'class':'app paid no_iap'}) 
free_apps = soup.findAll('td',{'class':'app free no_iap'}) 
grossing_apps = soup.findAll('td',{'class':'app free has_iap'})
grossing_apps1 = soup.findAll('td',{'class':'app paid has_iap'})

i=0

for free_app in free_apps:
	free_app_url=free_app.find('a',href=True)['href']
	free_app_name=free_app.find('span',{'class':'app-name'})['title']
	free_app_publish=free_app.find('span',{'class':'app-pub-er'})['title']
	print "free_no_in_app"+";"+free_app_url+";"+free_app_name+";"+free_app_publish
	##i=i+1

##print i

for grossing_app in grossing_apps:
	grossing_app_url=grossing_app.find('a',href=True)['href']
	grossing_app_name=grossing_app.find('span',{'class':'app-name'})['title']
	grossing_app_publish=grossing_app.find('span',{'class':'app-pub-er'})['title']
	print "free_have_in_app"+";"+grossing_app_url+";"+grossing_app_name+";"+grossing_app_publish
	##i=i+1

##print i

for paid_app in paid_apps:
	paid_app_url=paid_app.find('a',href=True)['href']
	paid_app_name=paid_app.find('span',{'class':'app-name'})['title']
	paid_app_publish=paid_app.find('span',{'class':'app-pub-er'})['title']
	print "paid_no_in_app"+";"+paid_app_url+";"+paid_app_name+";"+paid_app_publish
	##i=i+1

##print i

for grossing_app1 in grossing_apps1:
	grossing_app1_url=grossing_app1.find('a',href=True)['href']
	grossing_app1_name=grossing_app1.find('span',{'class':'app-name'})['title']
	grossing_app1_publish=grossing_app1.find('span',{'class':'app-pub-er'})['title']
	print "paid_have_in_app"+";"+grossing_app1_url+";"+grossing_app1_name+";"+grossing_app1_publish
	##i=i+1

##print i

