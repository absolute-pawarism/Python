import random

def generate_birthday():
    # Generate a random birthday (day of the year)
    return random.randint(1, 365)

def has_duplicate(birthdays):
    # Check if there are duplicate birthdays in the list
    return len(birthdays) != len(set(birthdays))

def simulate_birthday_experiment(num_simulations):
    # Simulate the experiment multiple times to estimate the probability
    count_duplicates = 0

    for i in range(num_simulations):
        # Generate random birthdays for 23 students
        birthdays = [generate_birthday() for j in range(23)]

        # Check if there are any duplicate birthdays
        if has_duplicate(birthdays):
            count_duplicates += 1

    # Calculate the estimated probability
    probability = count_duplicates / num_simulations
    return probability

# Number of simulations
num_simulations = 2

# Run the simulation
estimated_probability = simulate_birthday_experiment(num_simulations)

# Print the result
print(f"Estimated probability of at least two students having the same birthday: {estimated_probability:.4f}")
