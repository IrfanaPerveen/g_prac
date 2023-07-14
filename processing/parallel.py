
import grequests
import concurrent.futures
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

    # Send requests using parallel processing
    start_time = time.time()
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(send_request, session) for session in requests]
        responses = [future.result() for future in concurrent.futures.as_completed(futures)]
    end_time = time.time()

    # Calculate the total time taken
    total_time = end_time - start_time

    # Print the results
    print(f"Total requests sent: {num_requests}")
    print(f"Total time taken: {total_time} seconds")
