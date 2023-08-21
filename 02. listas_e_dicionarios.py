perifericos = [
'Mouse', 'Teclado', 'Monitor', 'Monitor' ]

print(perifericos)
print(perifericos[1])

# Remover itens duplicados
perifericos = list(set(perifericos))
print(perifericos)

# Adicionar valor em uma lista
perifericos.append('Webcam')
print(perifericos)

perifericos.insert(0, 'Headset')
print(perifericos)

# //////////////////////////// # 

dic_perifericos = {
    'Entrada': 'Mouse',
    'Saída': 'Monitor'
}

print(dic_perifericos)

dic_perifericos.pop('Entrada')
print(dic_perifericos)

dic_perifericos['Entrada'] = 'Teclado'
print(dic_perifericos)

dic_perifericos['Entrada'] = ['Teclado', 'Mouse']
dic_perifericos['Saída'] = ['Monitor', 'Caixa de som']
print(dic_perifericos)

print(dic_perifericos['Entrada'])
print(dic_perifericos['Entrada'][0])