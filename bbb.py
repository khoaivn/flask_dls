from flask import Flask
app = Flask(__name__)

def in_mot(number):
    u = number // 2
    for i in range(2, u + 1):
        if (number % i == 0):
            return False
    return True


@app.route('/')
def hello():
    result = ""
    for i in range(1, 90):
        if in_mot(i):
            result += " " + str(i)
    return result
if __name__ == '__main__':
    app.run(debug=True)