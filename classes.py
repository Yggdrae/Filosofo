class Card:
    CMC=0
    OnBF=False
    comb=""
    def __init__(self, cmc, bf, comb): #método construtor do objeto da classe
        self.CMC = cmc
        self.OnBF = bf
        self.comb = comb
    def mostrar(self):
        print("Card CMC.....: " + str(self.CMC))
        estado = "Sim" if self.OnBF else "Não" #Fazer uma 
        print("Está em campo: " + estado)
        print("Guilda.......: " + self.comb)
        print("-----------------------")
    def etb(self):
        self.OnBF = True
    def ltb(self):
        self.OnBF = False
    def atacar(self):
        if(self.OnBF):
            print("Atacando!")
        else:
            print("Está fora do campo!")


yuriko=Card(3, False, "Dimir") #Esse tipo de declaração usando o def __init__ dentro da classe, é util para se definir os valores
arahbo=Card(5, False, "Selesnya") # <--- dessa forma ao invés de declarar da forma como está comentado abaixo. 
winota=Card(4, True, "Boros")

yuriko.etb()
yuriko.atacar()
yuriko.mostrar()
arahbo.atacar()
arahbo.mostrar()
winota.ltb()
winota.atacar()
winota.mostrar()

"""yuriko.CMC = 3
yuriko.OnBF = False
yuriko.comb = "Dimir"

arahbo.CMC = 5
arahbo.OnBF = False
arahbo.comb = "Selesnya"

winota.CMC = 4
winota.OnBF = True
winota.comb = "Boros"

print("Card CMC: " + str(yuriko.CMC))
if yuriko.OnBF == True:
    print("Está no campo de batalha")
else:
   print("Não está no campo de batalha")
estado = "Sim" if yuriko.OnBF else "Não"
print("Está em campo: " + estado)
print("Guilda: " + yuriko.comb)"""
