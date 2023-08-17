import threading

def HelloWorld():
    print('Hello World!')

thread_01 = threading.Thread(target= HelloWorld)
thread_01.start()