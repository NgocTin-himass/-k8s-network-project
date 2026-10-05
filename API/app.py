from fastapi import FastAPI
import socket
import redis

app = FastAPI()

# Kết nối tới Redis Service trong Kubernetes
r = redis.Redis(
    host="redis-service",
    port=6379,
    decode_responses=True
)

@app.get("/")
def home():
    return {
        "message": "Hello from Kubernetes API",
        "hostname": socket.gethostname()
    }

@app.get("/hello")
def hello():
    return {
        "message": "Hello from API",
        "hostname": socket.gethostname()
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }

@app.get("/redis")
def redis_test():
    r.set("message", "Hello from Redis")

    value = r.get("message")

    return {
        "redis_value": value,
        "api_hostname": socket.gethostname()
    }
