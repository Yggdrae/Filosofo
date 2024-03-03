print("Olá Mundo")

x = ["Carro", 1, 4, True] #List
x[1] = x[1] + x[2] #Os valores em uma Lista podem ser reatribuidos
print(x) #Printa todos valores dentro da Lista
print(x[0]) #Printa o valor na posição 0 da Lista

x = ("Carro", 1, 4, False) #Tupla
#Os valores em uma Tupla NÃO PODEM ser reatribuidos
print(x) #Printa todos valores dentro da Tupla
print(x[3]) #Printa o valor na posição 3 da Tupla

x = { #Dict
    "Nome":"Victor",
    "Faculdade":"FATEC-Id",
    "Curso":"ADS"
}
x["Nome"] = "Victor Nicacio" #Os valores das chaves em uma Dict podem ser reatribuidos
print(x) #Printa todas as chaves/valores dentro da Dict
print(x["Faculdade"]) #Printa o valor da chave especificada

x = {1, 2, 3, 1, 3} #Set
print(x) #Ao printar um set, valores repetidos serão descartados no print

print("Valor: " + str(x)) #O comando "str()" foi usado para fazer uma conversão do Set em string,
#visto que ao tentar concatenar uma string com o set, é gerado um erro, necessitando assim da conversão.