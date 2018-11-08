import requests
import json
url = 'https://start-stop-adithya-instance2-dot-fca-ai.appspot.com'
try:
   result=requests.get(url)
   print(json.loads(result.content))
except requests.exceptions.RequestException as e:
   print(e)

