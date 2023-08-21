# FOR

mensagem = input("Digite sua mensagem: ")
repeticao = int(input("Quantas vezes deve ser repetida?")) +1

for repeticao in range(1, repeticao):
    print(f"{repeticao} - {mensagem}")
    
# //////////////////////////// #

# WHILE

numero = 0
resultado = 0

while True:
    numero = int(input("Digite um número: "))
    
    resultado += numero
    print(f"O resultado é {resultado}")
    
    if input("Deseja adicionar outro número? S/N").upper() == 'S':
        pass
    else: 
        break
    