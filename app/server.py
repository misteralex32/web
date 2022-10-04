from flask import Flask, render_template, jsonify
from prometheus_flask_exporter import PrometheusMetrics


app = Flask(__name__)
metrics = PrometheusMetrics(app)
health_status = True

@app.route('/')
def hello_world():
    return "Hello, World!"


@app.route('/toggle')
def toggle():
    global health_status
    health_status = not health_status
    return jsonify(health_value=health_status)

@app.route('/health')
def health():
    if health_status:
        resp = jsonify(health="healthy")
        resp.status_code = 200
    else:
        resp = jsonify(health="unhealthy")
        resp.status_code = 500

    return resp
    
if __name__ == "__main__":
    app.run("0.0.0.0")