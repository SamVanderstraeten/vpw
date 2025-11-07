lists = int(input())
for i in range(lists):
    n = int(input())

    list = []
    for _ in range(n):
        list.append(int(input()))
    list.sort()
    print((i+1), list[0], list[-1])