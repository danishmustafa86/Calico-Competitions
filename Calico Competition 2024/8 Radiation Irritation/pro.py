def solve_microwave():
    import math
    T = int(input().strip())
    results = []
    
    for _ in range(T):
        n, m = map(int, input().strip().split())
        
        # Option 1: Direct number sequence
        number_seq = "-".join(str(n))
        
        # Option 2: Using Add button
        add_presses = math.ceil(n / m)
        add_seq = "-".join(["Add"] * add_presses)
        
        # Choose the shortest, or lexicographically smallest if lengths are equal
        if len(number_seq.split("-")) < len(add_seq.split("-")):
            results.append(number_seq)
        elif len(number_seq.split("-")) > len(add_seq.split("-")):
            results.append(add_seq)
        else:
            results.append(min(number_seq, add_seq))
    
    # Print results
    print("\n".join(results))
