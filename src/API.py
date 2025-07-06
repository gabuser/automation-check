from requests import get

class APIs:
    #function to consume the API
    #this function use http communication to request data from the endpoint especified
    def requesting(self,slice:str)->None:
        response= get(f"https://api.pwnedpasswords.com/range/{slice}")
        
        #break the response from API in lines in a sequential order and put it into a list of strings
        self.organizing = response.text.splitlines()
        counting = 0
        self.lenght = len(self.organizing)-1
        self.formated =list()

        while(counting!= self.lenght):
                #get the individual values from the list, one by one until the -n values
                removing_numbers= self.organizing[counting]
                
                #this will format, removing the numbers that come from the response
                formating = removing_numbers.split(":")[0].strip()
                
                #the new formated will be put into a new list of strings with numbers removed
                self.formated.append(formating)
                counting+=1
        
        #this will sort the list for the binary search to works
        self.sorting = sorted(self.formated)
    
    #this function use binary search to fetch all the sufix hash coming from the API
    #reduce the complexity of searching data one by one.
    def search(self,mainhash:str)-> bool:
        self.initial = 0
        self.ending = len(self.sorting)-1
        
        while(self.initial <=self.ending):
            startpoint = (self.initial+self.ending)//2
            value=self.sorting[startpoint]

            if(value == mainhash):
                return True
            
            if(value < mainhash):
                self.initial = startpoint+1
            
            else:
                self.ending = startpoint-1
