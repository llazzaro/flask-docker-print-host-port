from random import randint
from flask import Flask, request

app = Flask(__name__)
APP_ID = randint(0, 10000000)

@app.route("/")
def hello():
    return "Running at {0}. APP_ID={1}".format(request.host, APP_ID)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
