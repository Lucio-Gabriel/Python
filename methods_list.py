filmsList = ["Batman", "Superman", "Baby Driver",
             "Esquadrão suicida", "Coringa", "Piratas do caribe"]

# 1 - Tamaho da lista
print(len(filmsList))

# 2 - Recuperar um item da lista pelo nome
print(filmsList.index("Batman"))

# 3 - Adicionar item ao final da lista
filmsList.append("Capitão america")
print(filmsList)

# 4 - Ordena a lista
filmsList.sort()
print(filmsList)

# 5 - Copiar os itens de uma lista para outra
filmsCopy = filmsList.copy()
filmsCopy.remove("Baby Driver")
print(filmsCopy)

# 6 - Remove todos os itens da lista
filmsList.clear()
print(filmsList)