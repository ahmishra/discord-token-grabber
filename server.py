from flask import Flask, render_template
from backend import main
from pprint import pprint

app = Flask(__name__)


@app.route("/")
def home():
    main()
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
