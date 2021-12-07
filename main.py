from flask import Flask
from redis import Redis

app = Flask(__name__)
redis = Redis(host='redis', port=6379)

@app.route('/')
def hello_world():
    redis.incr('hits')
    return f"{int(redis.get('hits'))} So it goes. " * 1000


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
    # app.run(port=5001, debug=True)
