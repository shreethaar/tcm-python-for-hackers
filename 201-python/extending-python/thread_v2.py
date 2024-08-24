import threading,time
from datetime import datetime

data_lock=threading.Lock()
data=[x for x in range(1000)]

def sync_consume_thread():
    global data_lock, data
    while True:
        data_lock.acquire()
        if Len(data) > 0:
            print(threading.current_thread().name,data.pop())
        data_lock.release()

threading.Thread(target=sync_consume_thread).start()
threading.Thread(target=sync_consume_thread).start()
threading.Thread(target=sync_consume_thread).start()
threading.Thread(target=sync_consume_thread).start()


