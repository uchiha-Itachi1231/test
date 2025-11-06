# Algorithm: "Greet the user and tell them their age next year"

# Step 1: Get the user's name
user_name = input("Hi, what is your name? ")

# Step 2: Get their current age
current_age_str = input("How old are you? ")
current_age = int(current_age_str) # Convert the text to a number

# Step 3: Calculate their age next year
age_next_year = current_age + 1

# Step 4: Print the result to the screen
print(f"Hello {user_name}, next year you will be {age_next_year} years old!