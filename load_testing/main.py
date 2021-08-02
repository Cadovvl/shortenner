
import concurrent.futures
import requests
import time
import random

urls = ["http://speedwagon.local/s/yoxaZ",
        "http://speedwagon.local/links/?format=json"]


def request_get(i):
    try:
        time.sleep(0.01 * i)
        start = time.time()
        resp = requests.get(random.choice(urls), allow_redirects=False)
        end = time.time()
        if resp.status_code == 200:
            return f"OK   :\t\t{end - start:.3f}"
        if resp.status_code == 301:
            return f"REDIRECTED\t{end - start:.3f}"
        return f"** ERROR:\t{end - start:.3f} **"
    except:
        return "**** FAIL!!! **** "


for i in range(10000):
    with concurrent.futures.ThreadPoolExecutor() as executor: # optimally defined number of threads
        res = [executor.submit(request_get, i) for i in range(1000)]
        for future in concurrent.futures.as_completed(res):
            print(future.result())
    time.sleep(random.random())


