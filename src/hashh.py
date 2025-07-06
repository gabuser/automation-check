from hashlib import sha1

class hashchunk:
    def hashing(self,passwords:str)->str:
        self.hashed= sha1(passwords.encode()).hexdigest().upper()
        self.lenghthash = len(self.hashed)-1
        self.sufix = self.hashed[5:self.lenghthash+1]

    def spliting(self)->str:
        halfhash = self.hashed[0:5]
        return halfhash

#print(hashing('ola mundo'))