from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    ds_hangbay = ("Vietnam Airline", "Vietjet Air", "Bamboo Airways", "Jetstar Pacific Airlines")
    name = 'Pham Trung Dung'
    
    return render_template('index.html', name = name, ds_hangbay = ds_hangbay)


def get_flight_radar():
	import requests

	url = "https://flight-radar1.p.rapidapi.com/aircrafts/list"

	headers = {
		"X-RapidAPI-Key": "fa97e59c65mshccb0c63302d8440p13c575jsn4742b0fd94a2",
		"X-RapidAPI-Host": "flight-radar1.p.rapidapi.com"
	}

	response = requests.get(url, headers=headers)

	return (response.json())

if __name__ == '__main__':
    app.run(debug=True)
