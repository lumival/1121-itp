import json
import requests

r = requests.get('https://rickandmortyapi.com/api/character')

print(r.status_code)
# Need to install pip in the terminal.
# 1.) pip3 install requests (if this does not work, do the next one)
# 2.) python3 -m pip install requests

# print(r.status_code)
#print(r.text)

data = json.loads(r.text)
print(data)
print(type(r.text))
print(type(data))

print(data['results'][2]['name'])

# Create a new worksheet
# assign new worksheet to a variable
# and create the following columns and populate the data from the API
# Name
# status
# species
# gender