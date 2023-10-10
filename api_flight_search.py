from flask import Flask, request, render_template
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def request_from():
	data = get_flight_radar()
	if request.method == 'POST':
		text = request.form["from"].upper()
		return render_template('api_flight_search.html', text = text, data = data)
	else:
		text = ""
		return render_template('api_flight_search.html', text = text, data = data)


def get_flight_radar():
	url = "https://flight-radar1.p.rapidapi.com/aircrafts/list"

	headers = {
		"X-RapidAPI-Key": "fa97e59c65mshccb0c63302d8440p13c575jsn4742b0fd94a2",
		"X-RapidAPI-Host": "flight-radar1.p.rapidapi.com"
	}

	response = requests.get(url, headers=headers)

	return (response.json())

if __name__ == '__main__':
    app.run(debug=True)
