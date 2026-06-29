import threading
import requests

URL = "http://127.0.0.1:5000/send"

def worker(i):
    msg = f"Thread-{i}"

    res = requests.post(URL, json={"message": msg})
    print(f"[Thread {i}] → {res.status_code}")

def run_threads():
    threads = []

    for i in range(20):
        t = threading.Thread(target=worker, args=(i,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("✅ All threads done")

if __name__ == "__main__":
    run_threads()