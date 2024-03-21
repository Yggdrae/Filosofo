import os
import colorama
import datetime

def main():
    print(colorama.Fore.LIGHTBLUE_EX + "1- Cadastrar Cliente")
    print("2- Consultar Cliente")
    print("3- Excluir Cliente")
    print("4- Sair" + colorama.Fore.RESET)
    opc = int(input("Entre com a operação desejada: "))
    return opc

class Cliente:
    nome = ""
    nasc= 31/12/99
    CPF = ""
    datain = ""
    def __init__(self, nome, nasc, CPF, datain):
        self.nome = nome
        self.nasc = nasc
        self.CPF = CPF
        self.ativo = True
        self.datain = datain
        self.dataout = False
    def info(self):
        print("Nome: " + self.nome)
        print("Data de Nascimento: " + str(self.nasc))
        print("CPF: " + str(self.CPF))
        print("Data de Cadastro: " + str(self.datain))
        print("Usuario ativo: " + ("Sim" if self.ativo else "Não"))
        if self.dataout:
            print("Data de Exclusão: " + str(self.dataout))
    def desativa(self):
        self.ativo = False
        self.dataout = datetime.datetime.now()

clientes = []

op = 0

while op != 4:
    os.system('cls')
    op = main()

    if op == 1:
        os.system('cls')
        print("ID do Cliente: #" + str(len(clientes)))
        n = input("Digite o nome do cliente.....................: ")
        nasc = input("Digite a data de nascimento (DDMMYYYY).......: ")
        nasc = '{}/{}/{}'.format(nasc[:2], nasc[2:4], nasc[4:])
        c = input("Digite o CPF (Somente Numeros)...............: ")
        if len(c) < 11:
            c = c.zfill(11)
        c = '{}.{}.{}-{}'.format(c[:3], c[3:6], c[6:9], c[9:])
        d = datetime.datetime.now()
        cliente = Cliente(n, nasc, c, d)
        clientes.append(cliente)
    elif op == 2:
        os.system('cls')
        n = input("Digite o ID do cliente: #")
        try:
            clientes[int(n)].info()
            os.system('pause')
        except:
            print("ID não encontrado!")
            os.system('pause')
    elif op == 3:
        os.system('cls')
        n = input("Digite o ID do cliente a ser desativado: #")
        try:
            clientes[int(n)].desativa()
            print("Cliente desativado com sucesso!")
            os.system('pause')
        except:
            print("ID não encontrado!")
            os.system('pause')