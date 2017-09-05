import csv

requisitos = []
tmp = []

with open("requisitos_estacionamento.csv", 'r', encoding='utf-8') as f:
    records = csv.DictReader(f)
    for row in records:
         tmp.append(row)


for requisito in tmp:
    x = dict()
    x['codigo'] = requisito['Requisito']
    x['nome'] = requisito['Nome']
    x['descricao'] = requisito['Descrição']
    requisitos.append(x)

# print(requisitos)
for requisito in requisitos:
	print(requisito)