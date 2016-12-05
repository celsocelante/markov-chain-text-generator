import sys
import random

# Chocagem de argumentos
if not len(sys.argv) == 4:
    print("Usage: " + (sys.argv[0] + " depth length"))
    sys.exit(1)

k = int(sys.argv[2]) # depth k
l = int(sys.argv[3]) # length l (output)
markov_chain = {} # inicializa a cadeia de Markov como um dicionari vazio

# Abre o arquivo, le e remove as quebras de linha e espacos excessivos
input_file = open(sys.argv[1], "r")
corpus = input_file.read().replace('\n', ' ')
' '.join(corpus.split())

for i in range(0, len(corpus)):
    # Quebra o texto em palavras de tamanho k e adiciona a cadeia
    end = i + k

    # Para o loop quando chega ao fim da string, para evitar violacao
    if end is len(corpus) + 1:
        break

    # Palavra de tamanho k
    word = corpus[i: end]

    try:
        # Adiciona a palavra e os proximos caracteres a cadeia
        if markov_chain.has_key(word):
            list_chars = markov_chain[word]
            list_chars.append(corpus[end])
            markov_chain[word] = list_chars
        else:
            list_chars = []
            list_chars.append(corpus[end])
            markov_chain[word] = list_chars
    except IndexError as e:
        break

final_text = random.choice(markov_chain.keys())
final_text = final_text + random.choice(markov_chain[final_text])

# Gera os proximos estados ate atingir o tamanho final l
while len(final_text) < l:
    final_text = final_text + random.choice(markov_chain[final_text[-k:]])

print final_text
