import socket
from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def hello():
    return "Running at {0}".format(request.host)


if __name__ == "__main__":
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('0.0.0.0', 0))
    port = sock.getsockname()[1]
    sock.close()
    app.run(debug=True, host='0.0.0.0', port=port)
