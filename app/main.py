from flask import Flask, Response
import time

from prometheus_client import (
    Counter,
    Histogram,
    generate_latest,
    CONTENT_TYPE_LATEST
)

app = Flask(__name__)

# -----------------------
# Prometheus Metrics
# -----------------------

REQUEST_COUNT = Counter(
    "app_requests_total",
    "Total number of HTTP requests",
    ["method", "endpoint"]
)

REQUEST_LATENCY = Histogram(
    "app_request_latency_seconds",
    "Request latency in seconds",
    ["endpoint"]
)

# -----------------------
# Application Endpoints
# -----------------------

@app.route("/")
def home():
    REQUEST_COUNT.labels(method="GET", endpoint="/").inc()
    return "DevOps Production App is running"


@app.route("/work")
def work():
    start_time = time.time()

    # Simulate CPU load
    end = start_time + 5
    x = 0
    while time.time() < end:
        x += 1

    REQUEST_COUNT.labels(method="GET", endpoint="/work").inc()
    REQUEST_LATENCY.labels(endpoint="/work").observe(time.time() - start_time)

    return "Work done"


# -----------------------
# Metrics Endpoint
# -----------------------

@app.route("/metrics")
def metrics():
    return Response(
        generate_latest(),
        mimetype=CONTENT_TYPE_LATEST
    )


# -----------------------
# App Entry Point
# -----------------------

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


########### local minikube  based app ##############

# from flask import Flask
# import time
# import random

# app = Flask(__name__)

# @app.route("/")
# def home():
#     return "DevOps Production App is running"

# @app.route("/work")
# # def work():
# #     time.sleep(random.uniform(0.1, 0.5))
# #     return "Work done"

# # to trigger HPA
# @app.route("/work")
# def work():
#     end = time.time() + 5  # burn CPU for 5 seconds
#     x = 0
#     while time.time() < end:
#         x += 1
#     return "Work done"

# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=5000)

########### local minikube based app ##############