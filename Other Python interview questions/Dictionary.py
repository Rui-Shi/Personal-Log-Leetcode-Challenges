# How do I define a dictionary in python, for example if I have two lists, 
# u=['apple','orange','peach'], v=[1,2,3] how to initial the dictionary?

u = ['apple','orange','peach']
v = [1,2,3]

my_dict = {}

for i in range(len(u)):
    my_dict[u[i]] = v[i]
    
print(my_dict)