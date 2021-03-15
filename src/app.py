from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "testing initial"

if __name__ == "__main__":
    app.run()
