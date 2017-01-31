from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def hello():
    return "Running at {0}".format(request.host)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
