from requests import get
counting =0
formated = list()
class APIs:

    def requesting(self,slice:str)->None:
        RESPONSE = get(f"https://api.pwnedpasswords.com/range/{slice}")
        self.organizing = RESPONSE.text.split("\n")
        self.lenght = len(self.organizing)

        while(counting !=self.lenght):
            formating = RESPONSE.text.split(":")[counting]
            formated.append(formating)
            counting+=1

    def search(self,oghash:str)-> bool:
        self.initial = 0
        self.ending = len(formated)-1

        while(self.initial <=self.ending):
            startpoint = (self.initial+self.ending)//2
            value=sorted(formated[startpoint])

            if(value == oghash):
                return True
            
            if(value < oghash ):
                self.initial+=1
            
            else:
                self.ending-=1
        
    """a = response.text.split("\n")
    tam = len(a)
    listas = []
    while counting != tam:
        formating = response.text.split(":")[counting]
        listas.append(formating)

        counting+=1
#print(a[tam])
#print(listas[0][tam].replace(ult, ""))
#18a98
print(a[tam-1])
print(listas[tam-1])"""