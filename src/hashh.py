from hashlib import sha1

class hashchunk:
    #function to create the hash and split the sufix hash from the prefix hash
    #use algorithm sha1 to satisfy the API
    def hashing(self,passwords:str)->str:
        self.hashed= sha1(passwords.encode()).hexdigest().upper()
        self.lenghthash = len(self.hashed)-1
        self.sufix = self.hashed[5:self.lenghthash+1]
    
    #function to split the prefixhash
    def spliting(self)->str:
        halfhash = self.hashed[0:5]
        return halfhash