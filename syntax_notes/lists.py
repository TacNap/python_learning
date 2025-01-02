# Python Lists
# Taken from https://developers.google.com/edu/python/lists
# To be transformed into Obsidian Note

# Declaration
colours = ['red', 'green', 'blue'] # List Literal

# Assignment
    # When a variable is assigned a list, it does not copy.
    # It will point the variable to the same memory location.
b = colours
print(b)
colours[0] = 'something else'
print(b)

# Accessing Elements
print(colours[0]) # red


print(len(colours)) # 3

# Iterating Through Lists
# for & in Keywords
squares = [1, 4, 9, 16]
sum = 0
for num in squares:
    sum += num
print(sum) # 30

# Loop with Indices
for i in range(0,4):
    print(squares[i])
    
# Check if value exists in list
list = ['cataniel', 'jacksoncrabs', 'spoghetti']
if 'cataniel' in list:
    print('wahoo!')
    
# List Methods
# Note that most of these perform the function in place. They do not return a copy of the list.
nums = [1, 3, 4, 5, 5, 5]
nums_two = [7, 8, 9]

nums.append(6)
nums.remove(5) # Removes first instance match. Throws error if element not present
print(nums.pop(3)) # Removes and returns the element from index [3]
nums.insert(1, 2) # Replaces index[1], pushes current [1] to [2]
nums.extend(nums_two) # Appends separate list
nums.sort() # Sorts the list in place. Other functions are preferred.

if 2 in nums:
    print(nums.index(2)) # Returns the index of a given element. Returns an error if element does not exist

print(nums)
strings = ["one","two"]
print(len(strings))













