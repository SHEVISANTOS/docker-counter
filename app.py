import os
import redis
from flask import Flask

app = Flask(__name__)

# This line is crucial: it uses 'localhost' for testing, and 'redis_db' for Docker
redis_host = os.environ.get('REDIS_HOST', 'redis_db')
cache = redis.Redis(host=redis_host, port=6379, decode_responses=True)

@app.route('/')
def hello():
    # Increment the counter in Redis
    count = cache.incr('hits')
    return f'Hello I Am Cooking Here! This page has been viewed {count} times.\n'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)# Updated via CI/CD Pipeline Mon Nov  2 10:32:19 AM EAT 2026
