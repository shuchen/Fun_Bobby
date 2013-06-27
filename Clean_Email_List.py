import csv

with open('contacts_2.txt', 'rb') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=';')
	for row in spamreader:
		print row