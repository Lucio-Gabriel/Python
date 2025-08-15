movieName = "Top Gun"

movieDescription = """
    Top gun maverick é um filme de aviação e aventura,
    muito consagrado na indústria 
"""

print(movieName.upper()) # string maiscula
print(movieName.lower()) # string minusculo
print(movieName.capitalize()) # Primeira letra maiscula
print(movieName.title()) # Primeira letra maiscula
print(movieName.center(10, '-')) # Retorna string centralizada com caractere de preenchimento
print(movieName.find("u")) # Retorna indice de caractere
print(movieName.find("o")) # Conta caracteres
print(movieName.replace("Top", "Matrix")) # Altera um elemento para outro
print(movieDescription.split(','))
