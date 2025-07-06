from requests import get
#ormated = list()
class APIs:

    def requesting(self,slice:str)->None:
        response= get(f"https://api.pwnedpasswords.com/range/{slice}")
        self.organizing = response.text.splitlines()
        counting = 0
        self.lenght = len(self.organizing)-1
        self.formated =list()

        while(counting!= self.lenght):
                removing_numbers= self.organizing[counting]
                formating = removing_numbers.split(":")[0].strip()
                self.formated.append(formating)
                counting+=1

        self.sorting = sorted(self.formated)

    def search(self,oghash:str)-> bool:
        self.initial = 0
        self.ending = len(self.sorting)-1
        
        while(self.initial <=self.ending):
            startpoint = (self.initial+self.ending)//2
            value=self.sorting[startpoint]

            if(value == oghash):
                return True
            
            if(value < oghash ):
                self.initial = startpoint+1
            
            else:
                self.ending = startpoint-1
