from flask import Flask
app = Flask(__name__)
@app.route('/')

def in_mot(number):
    u = number // 2
    for i in range(2, u + 1):
        if (number % i == 0):
            return False
    return True

def hello():
    result = ""
    for i in range(1, 10):
        if in_mot(i):
            print("Dung:" + i)
    return result
if __name__ == '__main__':
    app.run(debug=True)