from flask import Flask, render_template
import requests
import json

app = Flask(__name__)

@app.route('/')

def index():
	name = "Pham Trung Dung"
	response = get_json()
	len_json = len(response.json())


	return render_template('index.html', name = name, response = response.json(), len_json = len_json)
	# return render_template('index_one_flight.html', name = name, response = response.json)

def get_json():
	url = "https://iata-and-icao-codes.p.rapidapi.com/airlines"
    
	headers = {
		"content-type": "application/octet-stream",
		"X-RapidAPI-Key": "d91fb1e8a3msh22ab32c37f06602p1e9875jsnc5aefe1fe85d",
		"X-RapidAPI-Host": "iata-and-icao-codes.p.rapidapi.com"
	}

	response = requests.get(url, headers=headers)
	return response

if __name__ == '__main__':
	app.run(debug=True)