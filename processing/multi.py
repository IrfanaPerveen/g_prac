import grequests
import multiprocessing
import time

# Number of requests to send
num_requests = 500

# URL to send requests to
url = 'https://www.google.com'

# Function to send a request using grequests
def send_request(session):
    return session.get(url)

if __name__ == '__main__':
    # Create a session for grequests
    session = grequests.Session()

    # Create a list to hold the request objects
    requests = []

    # Generate the request objects
    for _ in range(num_requests):
        requests.append(grequests.request('GET', url, session=session))

    # Send requests using multiprocessing
    start_time = time.time()
    responses = grequests.map(requests, size=multiprocessing.cpu_count())
    end_time = time.time()

    # Calculate the total time taken
    total_time = end_time - start_time

    # Print the results
    print(f"Total requests sent: {num_requests}")
    print(f"Total time taken: {total_time} seconds")
