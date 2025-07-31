from flask import Flask
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)    

# Define a counter metric
@app.route("/api/v1")
def version_1():
    return {"message": "Hello from v1"}, 200

@app.route("/api/v2")
def version_2():
    return {"message": "Hello from v2"}, 200

@app.route("/api/v3")
def version_3():
    return {"message": "Hello from v3 on main"}, 200    

@app.route("/healthz")
def health_check():
    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
