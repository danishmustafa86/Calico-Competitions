t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    
    # Create inverse of arr1
    inv1 = [0] * (n + 1)
    for i in range(n):
        inv1[arr1[i]] = i + 1
    
    for _ in range(k):
        query = int(input())
        # Use inverse of arr1 to find position, then lookup in arr2
        pos = inv1[query] - 1
        result = arr2[pos]
        print(result)

