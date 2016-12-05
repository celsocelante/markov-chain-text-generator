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

testando = "testando"

for i in range(0, len(corpus)):
    # Quebra o texto em palavras de tamanho k e adiciona a cadeia
    end = i + k
    if end is len(corpus) + 1:
        break
    print corpus[i: end]

#print(corpus)
