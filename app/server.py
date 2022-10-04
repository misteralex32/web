from flask import Flask, render_template
from prometheus_flask_exporter import PrometheusMetrics


app = Flask(__name__)
metrics = PrometheusMetrics(app)

@app.route('/')
def hello():
    return '<h1>Hello, World!</h1>'

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