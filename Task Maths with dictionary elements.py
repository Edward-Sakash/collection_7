
"""Task - Maths with dictionary elements
You're given two dictionaries. Both have the same keys a, b, c with their values being random numbers. You need to multiply the values with the same key value in the other dict and sum all results.

Input:
dict1 = {
  'a': 4,
  'b': 16,
  'c': 3
}

dict2 = {
  'a': 8,
  'b': 2,
  'c': 3
}
Output:
73"""

#Solution 1
# Define the two dictionaries
dict1 = {'a': 4, 'b': 16, 'c': 3}
dict2 = {'a': 8, 'b': 2, 'c': 3}

# Iterate over the keys in dict1, multiply the values for each key from both dicts, and sum the results
result = sum(dict1[key] * dict2[key] for key in dict1)

# Print the final result
print(result)

print("______________________________________________")

# Solution 2
# Define the two dictionaries
dict1 = {'a': 4, 'b': 16, 'c': 3}
dict2 = {'a': 8, 'b': 2, 'c': 3}

# Initialize a variable to store the sum
result = 0

# Iterate over the keys in dict1
for key in dict1:
    # Multiply the corresponding values from both dicts and add the result to the sum
    result += dict1[key] * dict2[key]

# Print the final result
print(result)

print("______________________________________________")


