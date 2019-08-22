# 1541

# o texto desse problema é >>> MUITO RUIM <<<

while True:
    valores_input = input()
    if valores_input == '0':
        break
    lado_1, lado_2, porcentagem = [int(i) for i in valores_input.split()]
    area_do_projeto = lado_1 * lado_2
    area_do_terreno = area_do_projeto / (porcentagem / 100)
    lado_do_terreno = area_do_terreno**(1/2)
    print(int(lado_do_terreno))
