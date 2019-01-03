'''
1. suma toatala a literelor din TOATE dictionarele (cheile + valorile)  REVIEW
2. Suma toatala literelor din fiecare dictionar in parte REVIEW
3. afiseaza dictionarul intreg, care are cele mai multe litere in el for loop
'''


import requests


URL = "https://jsonplaceholder.typicode.com/photos"

response = requests.get(URL)
responseBody = response.json()
responseLength = len(responseBody)
keys_lengh = 0
value_length = 0
values_length1 = 0
total_each = 0
value_each = 0

if responseLength:
	for element in responseBody:
		for keys in element.keys():
			keys_lengh = len(keys) + keys_lengh
		for values in element.values():
			value_length1 = len(element['title']) + len(element['url']) + len(element['thumbnailUrl']) + element['albumId'] + element['id']
			value_length = value_length1 + value_length
		value_each = len(element['title']) + len(element['url']) + len(element['thumbnailUrl']) + element['albumId'] + element['id']
		print('\n keys: ',len(keys))
		print("\n values",value_each)
		total_each = len(keys) + value_each
		print("\n total: ", total_each)
		print("-------------")


total_length = value_length + keys_lengh
print('suma toatala: ', total_length)

