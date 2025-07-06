import queue
import threading
import sys
import hashh
import API
#reserved variable to be used
locking = threading.Lock()
queues = queue.Queue()
password = list()
prefixhash = list()
sufixhash= list()
threads = list()
hashobj = hashh.hashchunk()
api = API.APIs()

#class called managing to manage operations of write and reading, both methods will be called by the threads
class managing:

    #this function will be using one thread to put the incoming data in the FIFO data structure to be organized
    def reading_passwords(self,passwords:list)-> None:
        for r in passwords:
            queues.put(r)
    
    #this function will be returning the prefixhash(the first 5 characters from the hash) and sufixhash(rest of the hash)
    #it will be using 4 threads to do these operations, but one thread running at a time due to GIL from the python
    def returninghash(self):
        global password, prefixhash,sufixhash
        self.lenghtqueue = queues.qsize()

        for h in range(self.lenghtqueue):
             FIFO = queues.get()
             
             if(FIFO is not None):
                with locking:
                    hashobj.hashing(FIFO)
                    data = hashobj.spliting()
                    prefixhash.append(data)
                    sufixhash.append(hashobj.sufix)
                    #print(oghash)
                
#class to initialize the producer thread, will manage the input data as mentioned       
class Provinding(threading.Thread, managing):

    def __init__(self) -> None:
        threading.Thread.__init__(self)

    def run(self):
        self.reading_passwords(password)

#class to initialize the consumer thread, it will receiving data from the producer to make write operations.
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
    
    #manually pool thread creations
    for _ in range(1):
        producer = Provinding()
        producer.start()
        threads.append(producer)

    for _ in range(5):
        consumer = consuming()
        consumer.start()
        threads.append(consumer)
    
    #sentinel to tell the threads when to stop, if not specified, the thread will wait for incoming data.
    for _ in range(5):
     queues.put(None)
    
    #wait all the threads to be done
    for thread in threads:
        thread.join()

#function that run a single thread to make operations of request data from API and consuming data from API
def singlethread()->None:
    countinghash = len(password)
    counted =0

    while(counted !=countinghash):
        api.requesting(prefixhash[counted])

        result = api.search(sufixhash[counted])

        if(result):
            print(f"\n password were exposed once:{password[counted]}")
        
        else:
            print(f"password hash does not seems to be on the API list")
        counted+=1
main()
singlethread()