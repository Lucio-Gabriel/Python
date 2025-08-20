filmsSet = {"Batman", "Superman", "Baby Driver",
             "Esquadrão suicida", "Coringa", "Piratas do caribe"}

print(type(filmsSet))

# 1 - Buscar tamanho do set
print(len(filmsSet))

# 2 - True e 1 são considerados os mesmo valores
exampleSet = {"Inception", True, 1, 8.7}
print(exampleSet)

# 3 - Adicionar item de outro set
filmsSet.update(exampleSet)
print(filmsSet)

# 4 - Remover um item no set
filmsSet.remove(True)
filmsSet.remove(8.7)
print(filmsSet)