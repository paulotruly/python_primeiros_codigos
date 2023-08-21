import operator

print("Digite um número:")
numero1 =int(input())

print("Digite um operador:")
operador = input()

print("Digite outro número:")
numero2 =int(input())

if operador == '+':
    resultado = numero1 + numero2 
    print(resultado)
elif operador == '-':
    resultado = numero1 - numero2
    print(resultado)
elif operador == 'x':
    resultado = numero1 * numero2
    print(resultado)
elif operador == '/':
    resultado = numero1 / numero2
    print(resultado)
else:
    print("Operador inválido!")
    
# //////////////////////////// #

dict_operadores = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv
}

print("Digite um número:")
a = int(input())

print("Digite um operador:")
operador = input()

print("Digite outro número:")
b = int(input())

print(dict_operadores[operador](a, b))



    
    