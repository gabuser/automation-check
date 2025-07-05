from requests import get

response =get(f"https://api.pwnedpasswords.com/range/18a98")
listas = []
listas = response.text.split("\n")

listas2 = [c.replace("\n \r :","") for c in listas]
print(listas2)
#18a98
