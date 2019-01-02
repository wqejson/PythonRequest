'''
ia scriptul cela care-i in git la tine si fa urmatoarele:
- afiseaza cel mai lung email (ma refer la lunginea in caractere)
- afiseaza ID-ul care corespunde celui mai lung email
cind te convingi ca lucreaza, fa commit si eu o sa fac review

'''


import requests

email = 0
email_counter = 0
id = 0

URL = 'https://jsonplaceholder.typicode.com/comments' 

response = requests.get(URL) 

responseBody = response.json()
responseLength = len(responseBody)

if responseLength:
	for element in responseBody:
		if len(element['email']) > email_counter:  
			email_counter = len(element['email'])    
			email = element['email']
			id = element['id']

print('cel mai lung email : ', email, 'id: ', id)			
	


			



				
