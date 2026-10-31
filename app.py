from flask import Flask
import redis
import os

app = Flask(__name__)

# Connect to Redis. Notice we use 'redis' (the service name), NOT 'localhost'!
cache = redis.Redis(host='redis', port=6379)

@app.route('/')
def hello():
    # Increment the counter in Redis
    count = cache.incr('hits')
    return f'Hello CI/CD! This page has been viewed {count} times.\n'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)