import requests

# 1. Auth Service
resp = requests.post("http://localhost:5000/login", json={"username":"admin","password":"password"})
token = resp.json()["token"]
print("JWT Token:", token)

# 2. Personne Service
resp = requests.post("http://localhost:5001/persons", json={"name":"Alice"})
person_id = resp.json()["id"]
print("Created Person:", resp.json())

resp = requests.get(f"http://localhost:5001/persons/{person_id}")
print("Get Person:", resp.json())

# 3. Health Service
health_data = {"weight":65,"height":170,"heart_rate":70,"blood_pressure":"120/80"}
resp = requests.post(f"http://localhost:5002/health/{person_id}", json=health_data)
print("Add Health:", resp.json())

resp = requests.get(f"http://localhost:5002/health/{person_id}")
print("Get Health:", resp.json())
