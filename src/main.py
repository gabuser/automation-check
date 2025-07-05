import queue
import threading
import sys
import hashh

locking = threading.Lock()
queues = queue.Queue()
password = list()
hashed = list()
threads = list()
hashobj = hashh.hashchunk()

class managing:

    def reading_passwords(self,passwords:list)-> None:
        for r in passwords:
            queues.put(r)

    def returninghash(self):
        global password, hashed
        self.lenghtqueue = queues.qsize()

        for h in range(self.lenghtqueue):
             FIFO = queues.get()
             
             if(FIFO is not None):
                with locking:
                    hashobj.hashing(FIFO)
                    data = hashobj.spliting()
                    hashed.append(data)
                    print(self.lenghtqueue)
                
        
class Provinding(threading.Thread, managing):

    def __init__(self) -> None:
        threading.Thread.__init__(self)

    def run(self):
        self.reading_passwords(password)

class consuming(threading.Thread, managing):
    
    def __init__(self):
        threading.Thread.__init__(self)
    
    def run(self):
        self.returning = self.returninghash
        self.returning()

while True:
    try:
        insert = input("insert a password you want to break it or q and ctr+c to quit:")
        if(insert == 'q'):
            break

        else:
            dspace = insert.replace(" ", "")
            password.append(dspace)

    except KeyboardInterrupt:
         sys.exit()

for _ in range(1):
        producer = Provinding()
        producer.start()
        threads.append(producer)

for _ in range(5):
        consumer = consuming()
        consumer.start()
        threads.append(consumer)

for thread in threads:
        thread.join()
