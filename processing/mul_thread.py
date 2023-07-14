
import grequests
import threading
import time

# Number of requests to send
num_requests = 500

# URL to send requests to
url = 'https://www.google.com'

# Function to send a request using grequests
def send_request(session):
    return grequests.get(url, session=session)

if __name__ == '__main__':
    # Create a session for grequests
    session = grequests.Session()

    # Create a list to hold the request objects
    requests = []

    # Generate the request objects
    for _ in range(num_requests):
        requests.append(grequests.request('GET', url, session=session))

    # Send requests using multithreading
    start_time = time.time()
    threads = []
    for request in requests:
        thread = threading.Thread(target=send_request, args=(session,))
        threads.append(thread)
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()
    end_time = time.time()

    # Calculate the total time taken
    total_time = end_time - start_time

    # Print the results
    print(f"Total requests sent: {num_requests}")
    print(f"Total time taken: {total_time} seconds")
