from math import sqrt

elements = {'fire': [200, 20, 30, 50], 'water': [300, 10, 25, 40],
             'earth': [400, 25, 55, 70], 'air': [100, 18, 38, 60]}

t = int(input())

def main():
    a = str()
    for _ in range(t):
        # retangulo inimigo
        # largura, altura, lados esquerdo e debaixo
        w, h, left, bottom = [int(i) for i in input().split()]
        # lados direitos e de cima
        right, top = left + w, bottom + h
        # circulo da magia
        # elemento, nivel, coordenadas do centro, raio, iguala dano a 0
        e, l, cx, cy = [x if i == 0 else int(x) for i, x in enumerate(input().split())]
        r, damage = elements[e][l], 0
        # verifica se distancia entre centro e lados verticais e menor ou igual ao raio
        for vertical_side in [left, right]:
            if distance_point_vertical_line(cx, vertical_side) <= r or cx in range(left, right + 1): 
                # positivo
                # verifica se distancia entre centro e lados horizontais e menor ou igual ao raio
                for horizontal_side in [top, bottom]:
                    if distance_point_horizontal_line(cy, horizontal_side) <= r or cy in range(bottom, top + 1):
                        # positivo
                        damage = elements[e][0] # muda o valor do dano de 0 para o previsto em elements
        print(damage)

def distance_point_vertical_line(point_x, line):
    # calcula distancia entre x do ponto e reta vertical (x = c)
    # args: coordenada x do ponto, valor de x da reta vertical
    distance = abs(point_x - line)
    return distance

def distance_point_horizontal_line(point_y, line):
    # calcula distancia entre y do ponto e reta horizontal (y = c)
    # args: coordenada y do ponto, valor de y da reta horizontal
    distance = abs(point_y - line)
    return distance

main()
