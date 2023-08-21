print("Olá, qual é o seu nome?")

nome = input()

print(f"Seu nome é {nome}")

print("Qual é a sua idade?")

# //////////////////////////// # 

idade = int(input())

if idade >= 18:
    print("Você é maior de idade")
elif idade < 18:
    print("Você é menor de idade")
    
# //////////////////////////// # 

print("Digite o seu usuário:")
usuario = input()

print("Digite a sua senha:")
senha = input()

if usuario == 'Paulo' and senha == '2004':
    print("Login efetuado com sucesso!")
else:
    print("Nome de usuário ou senha incorreta!")
    
# //////////////////////////// # 

print("Informe o animal:")
animal = input()

if animal in ('Cachorro', 'Gato', 'Pássaro', 'Hamster'):
    print("O animal é doméstico!")
else: 
    print("O animal é selvagem!")