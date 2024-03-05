oi = "Hello Python"

print(oi[0:5]) #printa as 5 primeiras posições do array de caracteres.
print(oi[6:12]) #printa as ultimas 6 letras do array.
print(oi.strip()) #faz com que apareça sem espaços caso contenha no começo ou fim. Ex: " Hello Python   ".
print(oi.lower()) #string em minusculo.
print(oi.upper()) #string em maiusculo.
print(oi.replace("Hello", "I love")) #altera o trecho por outro.

o = oi.split() #divide a string por palavras, atribuido a uma nova variavel.
print(o) #printa a string dividida, atribuida na variavel "o".
print(o[1]) #printa a palavra em posição 1 da string dividida.
print("Tamanho da String 'oi': " + str(len(oi))) #mostra o tamanho da string (contando espaços)

res = "Python" in oi #verifica se uma string ESTÁ contida dentro da variavel com uma string
print(res) #atribuida e retorna verdadeiro ou falso. Sensivel a lower e upper.
res = "Python" not in oi #verifica se uma string NÃO ESTÁ contida dentro da variavel com uma
print(res) #string atribuida e retorna verdadeiro ou falso. Sensivel a lower e upper.

i = "python"
res = i in oi
print(res) #este print está retornando falso pela sensibilidade da comparação in em relação as strings.

res = i.lower() in oi.lower()
print(res) #retornando agora verdadeiro por conta da conversão lower em ambas variaveis ao compara-las.

cidade = "Salto"
dia = 20
mes = "Fevereiro"
ano = 2023
carta = "{}, {} de {} de {}" #coloca placeholders no formato pré definido por chaves

print(carta.format(cidade, dia, mes, ano))  #printa a variavel, substituindo os placeholders 

#\' \" \n (enter) \r (return?) \t (tab) \b (backspace)