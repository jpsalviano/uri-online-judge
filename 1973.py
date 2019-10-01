estrelas = int(input())
carneiros = [int(i) for i in input().split()]

class Estrela():

    def __init__(self, n, carneiros):
        self.n = n
        self.carneiros = carneiros

for n in range(estrelas):
    Estrela(n, carneiros[n])
