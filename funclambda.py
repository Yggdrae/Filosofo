#soma = lambda a,b: a+b
#print(soma(int(input("Digite o valor de A: ")), int(input("Digite o valor de B: "))))

#print((lambda a,b,c:a*b+c)(int(input("Digite o valor de A: ")), int(input("Digite o valor de B: ")), int(input("Digite o valor de C: "))))

r = lambda x,func:x+func(x)
res = r(2, lambda x:x*x)
print(res)