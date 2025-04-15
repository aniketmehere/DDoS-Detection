from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route("/")
def home():
    logs = []
    if os.path.exists("alerts.log"):
        with open("alerts.log", "r") as f:
            logs = f.readlines()
    return "<h1>DDoS Alerts</h1><pre>" + "".join(logs) + "</pre>"

if __name__ == "__main__":
    app.run(debug=True)

