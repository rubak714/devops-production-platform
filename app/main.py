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

def work():
    # heavier CPU task
    total = 0
    for i in range(10000000):
        total += i % 5
    time.sleep(random.uniform(0.1, 0.3))
    return f"Work done {total}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
