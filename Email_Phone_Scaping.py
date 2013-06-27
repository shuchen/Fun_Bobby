import urllib,re
from string import punctuation
from operator import itemgetter

ins = open( "Links_0621.txt", "r" )
##array = []
i=0

for line in ins:

	#text = ''
	phone = []
	email = []
 
 	try:
		f = urllib.urlopen(line)
		s = f.read()
		#phone=re.findall(r"\+\d{2}\s?0?\d{10}",s)
		email=re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}",s)
	except Exception:
		pass
		#import traceback
		#checksLogger.error('generic exception: ' + traceback.format_exc())
	
	email_set = set(email)
	##i=i+1	
	##text = i.str()+";"+phone, ";", email
	##print i, ";", phone, ";", set(email)
	print list(email_set)
