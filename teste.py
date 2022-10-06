import requests 

r = requests.post("http://localhost:9000/main", json={"planeta1": "earth", "planeta2": "mars"})

print(r.json())