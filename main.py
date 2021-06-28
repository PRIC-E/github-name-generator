import string
import random
import requests
import json

print(":: THIS DOES NOT CONSIDER SUSPENDED ACCOUNTS AS INEXISTENT, RESULTS VARY ::")

def generateUser(size=3, chars=string.ascii_lowercase):
    return ''.join(random.choice(chars) for _ in range(size))

for x in range(200):
    user = generateUser()
    try:
        jsonData = json.loads(
            requests.get(f"https://api.github.com/users/{user}").text
            )
        print (jsonData['login'] + ' exists, joined at: ' + jsonData['created_at'][:-10])
    except Exception as e:
        print (f'User: {user}, inexistent, free to take\n')
        
