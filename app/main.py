from flask import Flask
import time
import random

app = Flask(__name__)

@app.route("/")
def home():
    return "DevOps Production App is running"

@app.route("/work")
# def work():
#     time.sleep(random.uniform(0.1, 0.5))
#     return "Work done"

@app.route("/work")
def work():
    end = time.time() + 5  # burn CPU for 5 seconds
    x = 0
    while time.time() < end:
        x += 1
    return "Work done"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)