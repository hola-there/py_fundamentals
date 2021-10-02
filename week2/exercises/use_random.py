# Name: Ola B.
# Email: code@olab.dev
# Exercise 13 of Week 2
import random

# Generates a random integer inclusively between first argument to second argument
print(random.randint(6, 12))

# Get a random choice from a tuple
example_tuple_prompts = ("Haha", "Ah you choose me huh",
                         "Would've been easier to use this instead of the match case")
print(random.choice(example_tuple_prompts))

# Get a random choice from a list
example_list_prompts = ["Haha", "Ah you choose me huh",
                        "Would've been easier to use this instead of the match case"]
print(random.choice(example_list_prompts))

# Shuffle a list
print("The list before shuffling")
print(example_list_prompts)
random.shuffle(example_list_prompts)
print("The list after shuffling")
print(example_list_prompts)
