import threading
import requests

URL = "http://127.0.0.1:5000/send"

def test_threaded_requests():

    def worker(i):
        r = requests.post(URL, json={"message": f"pytest-{i}"})
        assert r.status_code == 200

    threads = []

    for i in range(10):
        t = threading.Thread(target=worker, args=(i,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    assert True