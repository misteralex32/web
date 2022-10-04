from flask import Flask
from prometheus_flask_exporter import PrometheusMetrics
app = Flask(__name__)
metrics = PrometheusMetrics(app)

@app.route('/')
def main():
    return 'OK'
def hello_world():
    return 'Hello World!'

if __name__ == "__main__":
    app.run(host="0.0.0.0")