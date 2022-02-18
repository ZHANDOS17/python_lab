from itertools import permutations
string = input()
def permutation(string):
    words = [''.join(p) for p in permutations(string)]
    print(words)
permutation(string)