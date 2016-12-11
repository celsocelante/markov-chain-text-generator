# -*- coding: utf-8 -*-
import sys
import random

# Checagem de argumentos
if not len(sys.argv) == 4:
    print("Uso: " + (sys.argv[0] + " k l"))
    sys.exit(1)

k = int(sys.argv[2]) # depth k
l = int(sys.argv[3]) # length l (output)

if k <= 0:
    print("k precisa ser maior do que 0")
    sys.exit(1)

if k > l:
    print("l muito pequeno. Escolha um valor maior.")
    sys.exit(1)

markov_chain = {} # inicializa a cadeia de Markov como um dicionario vazio

# Abre o arquivo, le e remove as quebras de linha
try:
    input_file = open(sys.argv[1], "r")
    corpus = input_file.read().replace('\n', '')
    # corpus = input_file.read() # caso queira manter os \n no texto final
    corpus_len = len(corpus)
except (OSError, IOError) as e:
    print("Erro ao abrir o arquivo.")
    sys.exit(1)

# Caso o arquivo seja muito pequeno.
if corpus_len < k + 1:
    print("Arquivo muito pequeno. Tente outro maior.")
    sys.exit(1)

# Loop que popula a Cadeia de Markov
for i in range(0, corpus_len):
    # Quebra o texto em palavras de tamanho k
    end = i + k

    # Para o loop quando chega ao fim da string, para evitar violacao
    if end is len(corpus) + 1:
        break

    # Palavra de tamanho k
    word = corpus[i: end]

    try:
        # Adiciona a palavra e os proximos possiveis caracteres a cadeia
        # Ex.: 'th' => ['e', 'a', ' ', 'r', ' ', 'e']
        if word in markov_chain:
            list_chars = markov_chain[word]
            list_chars.append(corpus[end])
            markov_chain[word] = list_chars
        else:
            list_chars = []
            list_chars.append(corpus[end])
            markov_chain[word] = list_chars
    except IndexError as e:
        break

# Escolhe aleatoriamente o inicio da string final (estado da cadeia + possivel prox. caractere)
final_text = random.choice(markov_chain.keys())
final_text = final_text + random.choice(markov_chain[final_text])

# Gera os proximos estados ate atingir o tamanho final l e exibe a string
while len(final_text) < l:
    final_text = final_text + random.choice(markov_chain[final_text[-k:]])
print(final_text)
