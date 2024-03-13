class NPC: #Base, Pai, Super
    def __init__(self, nome, time, forca, municao):
        self.nome = nome
        self.time = time
        self.forca = forca
        self.municao = municao
        self.vivo = True
        self.energia = 100

    def info(self):
        print("Nome...: " + self.nome)
        print("Time...: " + str(self.time))
        print("Forca..: " + str(self.forca))
        print("Municao: " + str(self.municao))
        print("Vivo...: "+ ("Sim" if self.vivo else "Não"))
        print("Energia: " + str(self.energia))
        print("--------------------------")

class Soldado(NPC):
    def __init__(self, nome, time):
        self.forca = 200
        self.municao = 200
        super().__init__(nome, time, self.forca, self.municao)

class Guarda(NPC):
    def __init__(self, nome, time):
        self.forca = 100
        self.municao = 20
        super().__init__(nome, time, self.forca, self.municao)

class Elite(NPC):
    def __init__(self, nome, time):
        self.forca = 400
        self.municao = 500
        super().__init__(nome, time, self.forca, self.municao)
    def inf(self):
        super().info()

s1 = Guarda("Deadeye", 1)
s2 = Soldado("Soldado 76", 1)
s3 = Elite("Nascimento", 1)
s4 = Guarda("Reaper", 2)
s5 = Soldado("Rango", 2)
s6 = Elite("Shogun", 2)

s1.info()
s2.info()
s3.info()
s4.info()
s5.info()
s6.inf()