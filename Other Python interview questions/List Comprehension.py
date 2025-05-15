# Given a series [1,2,3,4], how can you find the even numbers without using a for loop in Python?

series = [1, 2, 3, 4, 5, 6, 7]

# list compre
series_even = [x for x in series if x % 2 == 0]
print(series_even)

# filter function with lambda
series_even_filter = list(filter(lambda x: x % 2 == 0, series))
print(series_even_filter)