while True:
    try:
        n, d = [int(x) for x in input().split()]
        datas = []
        for _ in range(d):
            data, *pessoas = [x for x in input().split()]
            pessoas = [int(pessoas[i]) for i in range(n)]
            if sum(pessoas) == n:
                datas.append(data)
        if datas == []:
            print('Pizza antes de FdI')
        else:
            print(datas[0])
    except EOFError:
        break
