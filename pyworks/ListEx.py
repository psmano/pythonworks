#List Example

my_list = []
print("1st: " + str(my_list))

#list of integers
my_list = [1, 2, 3]
print(my_list)

#list of mixed datatypes
my_list = [1, "Hello", 3.4]
print(my_list)

#Nested list
my_list = ["mouse", [8, 4, 6], ['a', 'b']]
print(my_list)
my_list.append('5')
print(my_list)

my_list = ['p','r','o','b','e']
# Output: p
print(my_list[0])

# Output: o
print(my_list[2])

# Output: e
print(my_list[4])

# Error! Only integer can be used for indexing
# my_list[4.0]

# Nested List
n_list = ["Happy", [2,0,1,5]]

# Nested indexing

# Output: a
print(n_list[0][2])    

# Output: 5
print(n_list[1][3])

my_list = ['p','r','o','b','e']

# Output: e
print(my_list[-1])

# Output: p
print(my_list[-5])

for fruit in ['apple','banana','mango']:
    print("I like",fruit)