medidas = int(input())
alturas = [int(i) for i in input().split()]

def sobe(a, b):
    if a < b:
        return True

def desce(a, b):
    if a > b:
        return True

def padrao(lista):
    if lista[0] > lista[1]:
        return [desce, sobe]
    elif alturas[0] < alturas[1]:
        return [sobe, desce]
    else:
        return 0

def main():
    p = padrao(alturas)
    if p == 0:
        return p
    for i in range(medidas-1):
        if p[i%2](alturas[i], alturas[i+1]):
            pass
        else:
            return 0
    return 1

print(main())
