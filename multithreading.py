import threading
import time

def func(seconds):
    print(f"sleeping for {seconds} seconds")
    time.sleep(seconds)
    print(f"finished sleeping for {seconds} seconds")

if __name__ == "__main__":
    # func(10)
    # func(4)

    t1 = threading.Thread(target=func, args=[10])
    t1.start()

    t2 = threading.Thread(target=func, args=[4])
    t2.start()