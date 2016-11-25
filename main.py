import sys
import random

if not len(sys.argv) == 4:
    print("Usage: " + (sys.argv[0] + " depth length"))
    sys.exit(1)

level = int(sys.argv[2]) # depth k
length = int(sys.argv[3]) # length l (output)

input_file = open(sys.argv[1], "r")

print(length)
