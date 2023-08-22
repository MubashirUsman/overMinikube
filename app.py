from flask import Flask
app = Flask(__name__)

@app.route('/', methods=["GET"])
def hello_geek():
    return '<h2>Hello from Flask!!</h2>'


if __name__ == "__main__":
    app.run(debug=True)