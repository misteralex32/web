from flask import Flask
from prometheus_flask_exporter import PrometheusMetrics


app = Flask(__name__)
metrics = PrometheusMetrics(app, group_by='endpoint')

@app.route('/')
def hello_world():
    return 'Hello World!'
@app.route('/collection/:collection_id/item/:item_id')
@metrics.counter(
    'cnt_collection', 'Number of invocations per collection', labels={
        'collection': lambda: request.view_args['collection_id'],
        'status': lambda resp: resp.status_code
    })
def get_item_from_collection(collection_id, item_id):
    pass

if __name__ == "__main__":
    app.run("0.0.0.0")