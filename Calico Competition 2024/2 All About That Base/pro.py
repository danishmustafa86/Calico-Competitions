base_pair = {
    'A': 'T',
    'T': 'A',
    'C': 'G',
    'G': 'C'
}

T = int(input())  
results = []

for _ in range(T):
    dna = input().strip()
    # Converting DNA string to its complement
    complementary = ''.join(base_pair[base] for base in dna)
    results.append(complementary)

print("\n".join(results))
