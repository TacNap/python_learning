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
nums = [1, 2, 3, 4, 5]
nums.append(6)
nums.insert(2, 2.5) # Takes index[2], pushes current [2] to [3]

nums_two = [7, 8, 9]
nums.extend(nums_two) # Appends separate list


print(nums)
print(nums_two)












