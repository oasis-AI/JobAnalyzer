import threading
import time

def cpu_bound(thread_id):
    """CPU密集型计算"""
    start_time = time.time()
    counter = 0
    last_print = start_time
    
    while time.time() - start_time < 2:
        counter += 1
        if counter % 1000000 == 0:  # 减少打印频率
            current = time.time()
            if current - last_print >= 0.1:
                print(f"线程{thread_id}: {counter//1000000}M次迭代")
                last_print = current

# 创建两个CPU密集型线程
t1 = threading.Thread(target=cpu_bound, args=(1,))
t2 = threading.Thread(target=cpu_bound, args=(2,))

t1.start()
t2.start()
t1.join()
t2.join()