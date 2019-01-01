'''
ia scriptul cela care-i in git la tine si fa urmatoarele:
- afiseaza cel mai lung email (ma refer la lunginea in caractere)
- afiseaza ID-ul care corespunde celui mai lung email
cind te convingi ca lucreaza, fa commit si eu o sa fac review

'''


import requests

email = 0

URL = 'https://jsonplaceholder.typicode.com/comments' 

response = requests.get(URL) 

responseBody = response.json()
responseLength = len(responseBody)

if responseLength:
	for element in responseBody:
		email_counter = 0
		if len(element['email']) >= email_counter:
			email_counter = len(element['email'])
			if email_counter >= email:
				email = email_counter

for element in responseBody:
	if len(element['email']) == email:
		print('cel mai mare email: ',element['email'])
		print('id: ',element['id'])


			



				
