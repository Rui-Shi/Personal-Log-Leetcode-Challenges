# Example 1: Basic Lambda Function
# While you can assign a lambda to a variable, this is often just for demonstration.
# The primary power of lambdas comes from their inline use.

# A lambda function that adds 10 to an input number
add_ten = lambda x: x + 10
result1 = add_ten(5)
print(f"Example 1 (add_ten): {result1}") # Output: 15

# A lambda function that multiplies two numbers
multiply = lambda x, y: x * y
result2 = multiply(7, 3)
print(f"Example 1 (multiply): {result2}") # Output: 21

print("-" * 30)

# Example 2: Using Lambda with map()
# The map() function applies a given function to each item of an iterable (e.g., a list)
# and returns a map object (which can be converted to a list or other iterable).

numbers_list = [1, 2, 3, 4, 5]

# Using lambda to square each number in the list
squared_numbers = list(map(lambda x: x**2, numbers_list))
print(f"Example 2 (map to square numbers): {squared_numbers}") # Output: [1, 4, 9, 16, 25]

# Using lambda to convert a list of strings to uppercase
words = ["hello", "world", "python"]
uppercase_words = list(map(lambda word: word.upper(), words))
print(f"Example 2 (map to uppercase): {uppercase_words}") # Output: ['HELLO', 'WORLD', 'PYTHON']

print("-" * 30)

# Example 3: Using Lambda with filter()
# The filter() function constructs an iterator from elements of an iterable
# for which a function returns true.

numbers_list_for_filter = [10, 15, 20, 25, 30, 35, 40]

# Using lambda to filter out numbers greater than 25
filtered_numbers = list(filter(lambda x: x > 25, numbers_list_for_filter))
print(f"Example 3 (filter greater than 25): {filtered_numbers}") # Output: [30, 35, 40]

# Using lambda to filter for even numbers
even_numbers = list(filter(lambda x: x % 2 == 0, numbers_list_for_filter))
print(f"Example 3 (filter even numbers): {even_numbers}") # Output: [10, 20, 30, 40]

print("-" * 30)

# Example 4: Using Lambda with sorted() (or list.sort())
# The sorted() function (and the list.sort() method) can take a `key` argument.
# This key is a function that's called on each element before making comparisons.
# Lambdas are very convenient for defining simple key functions.

# List of tuples (name, age)
people = [("Alice", 30), ("Bob", 25), ("Charlie", 35), ("Diana", 28)]

# Sort by age (the second element of each tuple)
sorted_by_age = sorted(people, key=lambda person: person[1])
print(f"Example 4 (sorted by age): {sorted_by_age}")
# Output: [('Bob', 25), ('Diana', 28), ('Alice', 30), ('Charlie', 35)]

# Sort by name (the first element of each tuple)
sorted_by_name = sorted(people, key=lambda person: person[0])
print(f"Example 4 (sorted by name): {sorted_by_name}")
# Output: [('Alice', 30), ('Bob', 25), ('Charlie', 35), ('Diana', 28)]

# Sort a list of strings by their length
fruits = ["banana", "apple", "kiwi", "cherry", "elderberry"]
sorted_by_length = sorted(fruits, key=lambda fruit: len(fruit))
print(f"Example 4 (sorted by length): {sorted_by_length}")
# Output: ['kiwi', 'apple', 'banana', 'cherry', 'elderberry']

print("-" * 30)

# Example 5: Lambda with a Conditional Expression (ternary operator)
# Lambdas can use Python's conditional expression syntax: `value_if_true if condition else value_if_false`

# Check if a number is even or odd
check_parity = lambda num: "Even" if num % 2 == 0 else "Odd"
print(f"Example 5 (check_parity of 4): {check_parity(4)}")   # Output: Even
print(f"Example 5 (check_parity of 7): {check_parity(7)}")   # Output: Odd

# Assign a category based on value
categorize_value = lambda val: "High" if val > 50 else ("Medium" if val > 20 else "Low")
print(f"Example 5 (categorize 75): {categorize_value(75)}") # Output: High
print(f"Example 5 (categorize 30): {categorize_value(30)}") # Output: Medium
print(f"Example 5 (categorize 10): {categorize_value(10)}") # Output: Low

print("-" * 30)

# Example 6: Lambda with no arguments
# Though less common, lambdas can also take no arguments.

get_greeting = lambda: "Hello, Lambda!"
print(f"Example 6 (no arguments): {get_greeting()}") # Output: Hello, Lambda!
