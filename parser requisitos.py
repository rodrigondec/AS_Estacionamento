import csv

requisitos = []
tmp = []

with open("requisitos_estacionamento.csv", 'r', encoding='utf-8') as f:
    records = csv.DictReader(f)
    for row in records:
         tmp.append(row)


for requisito in tmp:
    x = dict()
    x['codigo'] = requisito['Requisito'].replace('RF', '')
    x['nome'] = requisito['Nome'].replace('\n', '').replace(' ', '')
    x['descricao'] = requisito['Descrição']
    requisitos.append(x)

# print(requisitos)
with open("My.sysadl", "a") as myfile:
	myfile.write("\n")
	for requisito in requisitos:
		layout = "Requirement {0} ( {1} ) {{\n\ttext = \"{2}\"\n}}\n"
		myfile.write(layout.format(requisito['nome'], requisito['codigo'], requisito['descricao']))
