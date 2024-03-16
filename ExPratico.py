import os

cards = []

class Card:
    nome = ""
    custo = 0
    atk = 0
    res = 0
    onbf = False
    def __init__(self, nome, custo, atk, res):
        self.nome = nome
        self.custo = custo
        self.atk = atk
        self.res = res
    def etb(self):
        self.onbf = True
    def ltb(self):
        self.onbf = False
    def info(self):
        print("Nome........................: " + self.nome)
        print("Custo de Mana...............: " + str(self.custo))
        print("Ataque e Resistencia basicos: " + str(self.atk) + "/" + str(self.res))
        
        print("Em campo....................: " + ("Sim" if self.onbf else "Não"))

def Menu():
    os.system('cls') or None
    print("1 - Novo Card")
    print("2 - Informações do Card")
    print("3 - Excluir Card")
    print("4 - Colocar Card em campo")
    print("5 - Retirar Card do campo")
    print("6 - Listar Cards")
    print("7 - Sair")
    print("Qtd de Cards: " + str(len(cards)))

    opt = input("Digite uma opcao: ")
    return opt

def NovoCard():
    os.system('cls')
    print("ID do card: " + str(len(cards)))
    n = input("Digite o nome do Card............: ")
    c = input("Entre com o custo de mana do Card: ")
    a = input("Entre com o ataque base..........: ")
    r = input("Entre com a resistencia base.....: ")
    card = Card(n, c, a, r)
    cards.append(card)
    print("Card adicionado com sucesso!")
    os.system('pause')

def infos():
    os.system('cls')
    n = input("Digite o numero do card a ser consultado: ")
    try:
        cards[int(n)].info()
        os.system('pause')
    except:
        print("O card não existe na lista!")
        os.system('pause')

def excluir():
    os.system('cls')
    n = input("Digite o numero do card a ser excluido: ")
    try:
        print(cards[int(n)].nome + " excluido com sucesso!")
        os.system('pause')
        del cards[int(n)]
    except:
        print("O card não existe na lista ou já foi excluido!")
        os.system('pause')

def enterbf():
    os.system('cls')
    n = input("Digite o numero do card a ser colocado em campo: ")
    try:
        cards[int(n)].etb()
        print(cards[int(n)].nome + " colocado em campo!")
        os.system('pause')
    except:
        print("O card não existe na lista!")
        os.system('pause')

def leavebf():
    os.system('cls')
    n = input("Digite o numero do card a ser retirado de campo: ")
    try:
        cards[int(n)].ltb()
        print(cards[int(n)].nome + " retirado do campo!")
        os.system('pause')
    except:
        print("O card não existe na lista!")
        os.system('pause')

def listar():
    os.system('cls')
    p = 0
    for c in cards:
        print(str(p) + " - " + c.nome)
        p=p+1
    os.system('pause')

ret = Menu()

while(ret != 7):
    if ret == "1":
        NovoCard()
    elif ret == "2":
        infos()
    elif ret == "3":
        excluir()
    elif ret == "4":
        enterbf()
    elif ret == "5":
        leavebf()
    elif ret == "6":
        listar()
    elif ret == "7":
        print("Encerrando programa!")
        os.system('pause')
        break
    else:
        print("Opção invalida!")
        os.system('pause')
    ret = Menu()

os.system('cls') or None
print("Programa encerrado!")
os.system('cls')