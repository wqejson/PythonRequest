import requests

URL = 'https://jsonplaceholder.typicode.com/comments'

response = requests.get(URL)

responseBody = response.json()
responseLength = len(responseBody)

if responseLength:
    for element in responseBody:
        print '%d --> %s' % (element['id'], element['email'])
else:
    print('Error: empty response!')

