from prometheus_client import start_http_server, Counter
import time
import random

# Create a counter metric for requests processed
requests_counter = Counter('myapp_requests_total', 'Total number of requests processed')

# Function to simulate processing a request
def process_request():
    # Simulate processing time
    processing_time = random.uniform(0.1, 0.5)
    time.sleep(processing_time)
    # Increment the counter
    requests_counter.inc()

if __name__ == "__main__":
    # Start HTTP server to expose metrics on port 8000
    start_http_server(8000)
    
    print("Server started at http://localhost:8000/metrics")
    
    # Simulatee processing requests indefinitely
    while True:
        process_request()

