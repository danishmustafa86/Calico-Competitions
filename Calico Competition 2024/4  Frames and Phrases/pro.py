# Read number of test cases
T = int(input().strip())

results = []

for _ in range(T):
    # Read the phrase
    phrase = input().strip()
    # Split into words
    words = phrase.split()
    # Find the length of the longest word
    max_length = max(len(word) for word in words)
    # Create the top and bottom border
    border = "*" * (max_length + 2)
    
    # Build the framed text
    framed_text = [border]
    for word in words:
        framed_text.append(f"*{word.ljust(max_length)}*")
    framed_text.append(border)
    
    # Append result to results list
    results.append("\n".join(framed_text))

# Print each framed phrase with a blank line between test cases
print("\n\n".join(results))
