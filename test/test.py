import requests

BASE = "http://127.0.0.1:5000/"

response = requests.put(BASE + "students/125122", {"name":"Peter Stedman", "class":"sophomore"})
print(response.json())