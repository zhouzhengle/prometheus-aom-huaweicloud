from random import randint
from flask import Flask, Response,jsonify
from prometheus_client import Counter, Gauge, Histogram, Summary, \
    generate_latest, CollectorRegistry

app = Flask(__name__)

registry = CollectorRegistry()
counter = Counter('order_service_processed_orders_total', 'order total', ['order_type'], registry=registry)
# gauge = Gauge('order_total_by_everyday', 'order number by everyday', ['order_type'], registry=registry)
# buckets = (100, 200, 300, 500, 1000, 3000, 10000, float('inf'))
# histogram = Histogram('api_calls_number', 'an example showed how to use histogram',
#                       ['order_type'], registry=registry, buckets=buckets)
# summary = Summary('my_summary', 'an example showed how to use summary', ['machine_ip'], registry=registry)

@app.route('/makeFoodOrder')
def makeFoodOrder():
    # 业务代码
    counter.labels('food').inc(1)
    # 业务代码
    return jsonify({"success":True})

@app.route('/makeClothingOrder')
def makeClothingOrder():
    # 业务代码
    counter.labels('clothing').inc(1)
    # 业务代码
    return jsonify({"success":True})

@app.route('/metrics')
def metrics():
    # counter.labels('127.0.0.1').inc(1)
    # gauge.labels('127.0.0.1').set(2)
    # histogram.labels('127.0.0.1').observe(1001)
    # summary.labels('127.0.0.1').observe(randint(1, 10))

    return Response(generate_latest(registry), mimetype='text/plain')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)