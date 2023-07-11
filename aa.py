from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')

def index():
    return render_template('get_input.html')

@app.route('/submit', methods=['POST'])

def submit():
    name = request.form.get('name')
    email = request.form.get('email')
    return f'Thanks for submitting the form, {name} ({email})!'
