def solve(B: int, N: int, S: list) -> int:
    min_height = min(S)
    max_height = max(S)

    best_height = None
    min_danger = 100000
    min_cost = 100000

    for h in range(min_height, max_height + 1):
        danger = sum(abs(h - si) for si in S)
        cost = sum(h - si for si in S if h > si)

        # Alternative cost calculation:
        # cost = sum(max(0, h - si) for si in S)

        if cost <= B:
            if danger < min_danger or (danger == min_danger and cost < min_cost):
                best_height = h
                min_danger = danger
                min_cost = cost

    return best_height

def main():
    T = int(input())

    for _ in range(T):
        temp = input().split()
        B, N = int(temp[0]), int(temp[1])
        S = [int(x) for x in input().split()]

        print(solve(B, N, S))

if __name__ == '__main__':
    main()