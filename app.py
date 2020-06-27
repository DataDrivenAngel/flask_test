from flask import Flask

app = Flask(__name__)

@app.route("/")
def ohell():
    return "Oh Hell World"


if __name__ == "__main__":
    app.run()