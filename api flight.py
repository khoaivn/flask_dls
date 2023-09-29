from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    ds_hangbay = ("Vietnam Airline", "Vietjet Air", "Bamboo Airways", "Jetstar Pacific Airlines")
    name = 'Pham Trung Dung'
    
    return render_template('index.html', name = name, ds_hangbay = ds_hangbay)


if __name__ == '__main__':
    app.run(debug=True)
