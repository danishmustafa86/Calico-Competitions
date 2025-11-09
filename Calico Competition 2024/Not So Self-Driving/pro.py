# Read input
T = int(input())  # Number of test cases
results = []

for _ in range(T):
    # Read the speed and distance
    v, x = map(float, input().split(":"))
    
    # Handle the case where speed is 0
    if v == 0:
        results.append("SAFE")
        continue
    
    # Calculate time to collision
    time_to_collision = x / v
    
    # Determine the output based on the criteria
    if time_to_collision <= 1:
        results.append("SWERVE")
    elif time_to_collision <= 5:
        results.append("BRAKE")
    else:
        results.append("SAFE")

# Print all results
print("\n".join(results))
