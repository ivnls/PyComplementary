texto = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."

def medir_chars_text(text):
    chars = 0
    for letter in text:
        chars += 1
    return chars

print(medir_chars_text(texto))
print("\n")


def pesquisar_palavra(text, palavra):
    words = text.split(" ")
    list_of_indexes = []
    for index, word in enumerate(words):
        if word.lower() == palavra.lower():
            list_of_indexes.append(index)
    if len(list_of_indexes) == 0:
        return "Não Encontrado"
    else:
        for a in list_of_indexes:
            print(a, end=' ')
        return f" <-- Nestas posições a palavra '{word} foi encontrada'"
        
    

print(pesquisar_palavra(texto, "been"))
        

























    
