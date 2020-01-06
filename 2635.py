while True:
    try:
        palavras = []
        n = int(input())
        for _ in range(n):
            palavra = input()
            palavras.append(palavra)
        q = int(input())
        for _ in range(q):
            consulta, ocorrencias, tamanho = input(), 0, 0
            for palavra in palavras:
                if palavra.startswith(consulta):
                    ocorrencias += 1
                    if len(palavra) > tamanho:
                        tamanho = len(palavra)
            [print(ocorrencias, tamanho) if ocorrencias > 0 else print(-1)]
    except EOFError:
        break
