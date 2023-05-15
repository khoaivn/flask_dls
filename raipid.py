from flask import Flask, render_template
import requests
import json

app = Flask(__name__)

@app.route('/')

def index():
	name = "Pham Trung Dung"
	response = get_json_flight_area()
	len_json = len(response.json()['flights'])


	return render_template('index.html', name = name, response = response.json(), len_json = len_json)
	# return render_template('index_one_flight.html', name = name, response = response.json)

def get_json_flight_area():

	url = "https://flight-data4.p.rapidapi.com/get_area_flights"

	querystring = {"latitude":"21.0278","longitude":"105.8342"}

	headers = {
		"X-RapidAPI-Key": "fa97e59c65mshccb0c63302d8440p13c575jsn4742b0fd94a2",
		"X-RapidAPI-Host": "flight-data4.p.rapidapi.com"
	}

	response = requests.get(url, headers=headers, params=querystring)

	return response

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