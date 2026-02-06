aantal_tests = int(input())
for t in range(aantal_tests):
    print(t, end=" ")
    window_size = int(input())
    total_amounts = int(input())
    lijst = [int(x) for x in input().split(" ")]
    for i in range(total_amounts-window_size+1):
        print(sum(lijst[i:i+window_size]), end=" ")
    print()