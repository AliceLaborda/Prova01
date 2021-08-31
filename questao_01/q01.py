pib = []

with open("./../dataset/pib_municipio_2010_a_2018.txt", "r", encoding="utf8") as file:
    file = file.readlines()

    for line in file[1:]: # O for pega a partir da segunda linha
        line = line.strip().split(";")

        if line[3] == "Manaus":
            pib.append(float(line[8])) # Se o segundo elemento da lista line for igual a "RO", ele vai adicionar o oitavo elemento na lista 'pib'
        

valorMedio = sum(pib) / len(pib) # Aqui é pego o valor médio dividindo a soma de todos os elementos pelo tamanho da lista

with open("./saida_q1.txt", "w") as file:
    file.write(f"{valorMedio:.2f}") # Aqui é escrito o resultado do valor médio com duas casas decimais

    print(valorMedio)
