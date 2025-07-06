import queue
import threading
import sys
import hashh
import API

locking = threading.Lock()
queues = queue.Queue()
password = list()
modhash = list()
oghash= list()
threads = list()
hashobj = hashh.hashchunk()
api = API.APIs()

class managing:

    def reading_passwords(self,passwords:list)-> None:
        for r in passwords:
            queues.put(r)

    def returninghash(self):
        global password, modhash,oghash
        self.lenghtqueue = queues.qsize()

        for h in range(self.lenghtqueue):
             FIFO = queues.get()
             
             if(FIFO is not None):
                with locking:
                    hashobj.hashing(FIFO)
                    data = hashobj.spliting()
                    modhash.append(data)
                    oghash.append(hashobj.sufix)
                    #print(oghash)
                
        
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

def main()-> None:
    while True:
        try:
            insert = input("insert a password you want to search or q to continuous and ctr+c to quit:")
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

    for _ in range(5):
     queues.put(None)

    for thread in threads:
        thread.join()

def singlethread()->None:
    countinghash = len(password)
    counted =0

    while(counted !=countinghash):
        api.requesting(modhash[counted])

        result = api.search(oghash[counted])

        if(result):
            print(f"\n password were exposed once:{password[counted]}")
        
        else:
            print(f"password hash does not seems to be on the API")
        counted+=1
main()
singlethread()