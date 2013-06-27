import urllib,re
from string import punctuation
from operator import itemgetter

ins = open( "emails_1.txt", "r" )
i=0

for line in ins:
	email_list = []
	eamil_list = line
	print line
	i=i+1
	print i, ";", set(email_list)
