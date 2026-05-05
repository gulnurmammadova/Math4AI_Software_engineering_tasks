

import threading
import time
import multiprocessing
import requests


'''Tapşırıq 1
3 funksiya yazın: send_email(), download_file(), 
save_log(). Hər biri 2 saniyə gözləsin və thread ilə eyni 
vaxtda işləsin.'''

def send_email():
    print("Email göndərilir...")
    time.sleep(2)
    print("Email göndərildi.")
def download_file():
    print("Fayl yüklənir...")
    time.sleep(2)
    print("Fayl yükləndi.")
def save_log():
    print("Log yadda saxlanılır...")
    time.sleep(2)
    print("Log yadda saxlanıldı.")
threads = [
    threading.Thread(target=send_email),
    threading.Thread(target=download_file),
    threading.Thread(target=save_log)]
start_time = time.time()
for t in threads: t.start()
for t in threads: t.join()
print(f"Cəmi vaxt: {time.time() - start_time} saniyə") 

if __name__ == "__main__":
    
    threads = [
        
    threading.Thread(target=send_email),
    threading.Thread(target=download_file),
    threading.Thread(target=save_log)
    ]
    start_time = time.time()
    for t in threads: t.start()
    for t in threads: t.join()
    print(f"Cəmi vaxt: {time.time() - start_time} saniyə")

    
'''Tapşırıq 2
10 URL üçün requests.get() edin. Hər URL ayrı thread
də işləsin və status_code çap olunsun'''


def check_url(url):
    try:
        status = requests.get(url, timeout=5).status_code
        print(f"{url} -> {status}")
    except:
        print(f"{url} -> İşləmir")

if __name__ == "__main__":
    urls = ["https://google.com", "https://github.com", "https://python.org"] * 3 + ["https://example.com"]
    for url in urls:
        threading.Thread(target=check_url, args=(url,)).start()

'''Tapşırıq 3
counter = 0 yaradın. 2 thread counter-i artırsın. Əvvəl 
Lock olmadan, sonra Lock ilə yoxlayın'''
counter = 0
lock = threading.Lock()

def increase():
    global counter
    for _ in range(1000000):
        with lock:
            counter += 1

t1 = threading.Thread(target=increase)
t2 = threading.Thread(target=increase)

t1.start(); t2.start()
t1.join(); t2.join()

print(f"Yekun Counter: {counter}") 

'''Tapşırıq 4
multiprocessing ilə 4 process yaradın. Hər process bir 
ədədin kvadratını hesablasın.'''
def square(n):
    return n * n

if __name__ == "__main__":
    numbers = [11, 12, 16, 18, 19, 24]
    with multiprocessing.Pool(processes=4) as pool:
        results = pool.map(square, numbers)
    
    print(f"Nəticə: {results}")


'''Tapşırıq 5
Pool istifadə edərək numbers = [2, 4, 6, 8, 10, 12] 
siyahısının kvadratlarını tapın'''
  

def square(n):
    return n * n

if __name__ == "__main__":
    numbers = [2, 4, 6, 8, 10, 12]

    with multiprocessing.Pool() as pool:
        results = pool.map(square, numbers)

    print(f"Orijinal siyahı: {numbers}")
    print(f"Kvadratlar siyahısı: {results}")