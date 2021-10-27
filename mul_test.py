def producer(q):
    for i in range(1000):
        q.put(i)
        
def consumer(q):
    while not q.empty():
        data = q.get()
        print(data)

class tests:
    def producer(self, q):
        for i in range(1000):
            q.put(i)
        
    def consumer(self, q):
        while not q.empty():
            data = q.get()
            print(data)

import multiprocessing

if __name__=='__main__':
    # q = multiprocessing.Queue()
    # p1 = multiprocessing.Process(target=producer, args=(q,))
    # c1 = multiprocessing.Process(target=consumer, args=(q,))
    # p2 = multiprocessing.Process(target=producer, args=(q,))
    # c2 = multiprocessing.Process(target=consumer, args=(q,))

    # p1.start()
    # c1.start()
    # p2.start()
    # c2.start()

    # p1.join()
    # p2.join()

    t1 = tests()
    q = multiprocessing.Queue()
    p1 = multiprocessing.Process(target=t1.producer, args=(q,))
    c1 = multiprocessing.Process(target=t1.consumer, args=(q,))
    p2 = multiprocessing.Process(target=t1.producer, args=(q,))
    c2 = multiprocessing.Process(target=t1.consumer, args=(q,))

    p1.start()
    c1.start()
    p2.start()
    c2.start()

    p1.join()
    p2.join()