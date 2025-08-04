from flask import Flask, request, jsonify
from prometheus_flask_exporter import PrometheusMetrics
from jobs import url_validator

# Initialize Flask app and Prometheus metrics
app = Flask(__name__)
metrics = PrometheusMetrics(app)    


# Retrieve all jobs available in API
@app.route("/api/v1/jobs", methods=["GET"])
def get_jobs():
    return {
        "jobs": [
            {
                "name": "validate-url",
                "description": "Validates a URL for format, reachability, and HTTPS support"
            }
        ]
    }, 200

# Run URL validation job
@app.route("/api/v1/jobs/validate-url", methods=["POST"])
def url_validation():
    url = request.json.get("url")

    if not url:
        return {"error": "URL is required"}, 400
    
    job_result = url_validator.validate_url(url)

    if job_result["error"]:
        return {"error": job_result["error"]}, 400
    return {
        "is_valid": job_result["is_valid"],
        "https_supported": job_result["https_supported"],
        "status_code": job_result["status_code"]
    }, 200

# Health check endpoint
@app.route("/health", methods=["GET"])
def health_check():
    return jsonify({"status": "healthy"}), 200



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
