soad = {0: 'PROXYCITY', 1: 'P.Y.N.G.', 2: 'DNSUEY!', 3: 'SERVERS', 4: 'HOST!', 5: 'CRIPTONIZE', 6: 'OFFLINE DAY', 7: 'SALT', 8: 'ANSWER!', 9: 'RAR?', 10: 'WIFI ANTENNAS'}

c = int(input())

for _ in range(c):
    x, y = [int(i) for i in input().split()]
    print(soad[x+y])
