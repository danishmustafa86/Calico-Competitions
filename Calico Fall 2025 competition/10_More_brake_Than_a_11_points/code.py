t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    balance = [0] * (n + 1)
    
    for _ in range(m):
        u, v, w = map(int, input().split())
        balance[u] -= w
        balance[v] += w
    
    total_positive = 0
    positive_count = 0
    negative_count = 0
    
    for i in range(1, n + 1):
        if balance[i] > 0:
            total_positive += balance[i]
            positive_count += 1
        elif balance[i] < 0:
            negative_count += 1
    
    involved = positive_count + negative_count
    
    if involved == n:
        print(total_positive)
    else:
        print(involved)

