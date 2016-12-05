import sys
import random

if not len(sys.argv) == 4:
    print("Usage: " + (sys.argv[0] + " depth length"))
    sys.exit(1)

level = int(sys.argv[2]) # depth k
length = int(sys.argv[3]) # length l (output)
markov_chain = {} # inicializa a cadeia de Markov como um dicionari vazio

# Abre o arquivo, le e remove as quebras de linha e espacos excessivos
input_file = open(sys.argv[1], "r")
corpus = input_file.read().replace('\n', ' ')
' '.join(corpus.split())

print(corpus)
