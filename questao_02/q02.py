with open("./../dataset/pib_municipio_2010_a_2018.txt", "r", encoding="utf8") as file:
    file = file.readlines()

    content = []
    names = []


    # Armazena os nomes dos municípios na lista 'names'
    for line in file[1:]:
        line = line.strip().split(";")

        if line[0] == "2010":
            if line[2] not in names:
                names.append(line[2])


    # Percorre a lista 'names' e adiciona em uma lista todos os pibs desse determinado município
    for name in names:
        pib = []

        for line in file[1:]:

            line = line.strip().split(";")

            if line[0] == "2010":
                if line[2] == name:

                    pib.append(float(line[8]))


        # Adiciona na lista 'content' um dicionario com o nome do município e a média do seu pib
        content.append({
            "name": name,
            "pib": sum(pib) / len(pib)
        })

muted = True


# Ordena a lista 'content' pelo valor do pib
while muted:
    muted = False

    for index in range(1, len(content)):
        if content[index]["pib"] > content[index - 1]["pib"]:
            content[index], content[index - 1] = content[index - 1], content[index]
            muted = True


# Salva a lista 'content' na saída em txt com a posição, nome e a média do pib de cada município
with open("./saida_q2.txt", "w") as file:

    aux = []

    for index, element in enumerate(content):

        pos = "0" + f"{index + 1}"

        aux.append(f"{pos[-2:]}º -> Nome: {element['name']}; PIB: {element['pib']:.2f}")

    file.write("\n".join(aux))
