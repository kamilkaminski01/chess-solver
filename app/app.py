from flask import Flask
from flask_restful import Api

app = Flask(__name__)
api = Api(app)


@app.route("/")
def hello_world():
    return "<h1>Hello world</h1>"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
