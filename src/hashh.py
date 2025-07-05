from hashlib import sha1

class hashchunk:
    def hashing(self,passwords:str)->str:
        self.hashed= sha1(passwords.encode()).hexdigest()

    def spliting(self)->str:
        halfhash = self.hashed[0:5]
        return halfhash

#print(hashing('ola mundo'))