n_of_measures = int(input())
rpm_list = [int(i) for i in input().split()]

for n in range(1, n_of_measures):
    if rpm_list[n-1] > rpm_list[n]:
        print(n+1)
        break
    if n == n_of_measures - 1:
        print(0)
