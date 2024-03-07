import os

os.system('cls')
"""
mtg = [["Arahbo", "Selesnya"], 
       ["Yuriko", "Dimir"], 
       ["Miirym", "Temur"]]

for x, y in mtg:
    print(x + ": " + y)


mtg = {"Arahbo":"Selesnya", 
       "Yuriko":"Dimir", 
       "Miirym":"Temur"}

novoc = input("Entre com o nome do card: ")
novacomb = input("Entre com a combinação de cor do card: ")

mtg[novoc] = novacomb

for x in mtg:
    print(x) #Chave
    print(mtg[x]) #Valor

for x, y in mtg.items():
    print("Card: " + x + "  Combinação: " + y)
"""

mtg = {
    "Arahbo":{
        "Combinação":"Selesnya",
        "CMC":"5"
    },
    "Yuriko":{
        "Combinação":"Dimir",
        "CMC":"3"
    },
    "Miirym":{
        "Combinação":"Temur",
        "CMC":"6"
    }
}

ncard = input("Entre com o nome do card: ")
ncomb = input("Entre com a combinação de cor do card: ")
ncmc = input("Entre com o CMC do card: ")

mtg[ncard] = {"Combinação":ncomb, "CMC":ncmc}

print(mtg)