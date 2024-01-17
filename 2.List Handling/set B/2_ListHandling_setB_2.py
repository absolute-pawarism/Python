import random

def generate_birthday():
    return random.randint(1, 365)

def has_duplicate(birthdays):
    return len(birthdays) != len(set(birthdays))

def simulate_birthday_experiment(num_simulations): 
    count_duplicates = 0
    for i in range(num_simulations):
        birthdays = [generate_birthday() for j in range(23)]
        if has_duplicate(birthdays):
            count_duplicates += 1
    probability = count_duplicates / num_simulations
    return probability
num_simulations = 100
estimated_probability = simulate_birthday_experiment(num_simulations)
print(f"Estimated probability of at least two students having the same birthday: {estimated_probability:.4f}")
