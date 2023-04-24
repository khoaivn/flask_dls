import requests

url = "https://iata-and-icao-codes.p.rapidapi.com/airlines"

headers = {
	"content-type": "application/octet-stream",
	"X-RapidAPI-Key": "d91fb1e8a3msh22ab32c37f06602p1e9875jsnc5aefe1fe85d",
	"X-RapidAPI-Host": "iata-and-icao-codes.p.rapidapi.com"
}

response = requests.get(url, headers=headers)

print(response.json())