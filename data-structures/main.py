# Data Structures (Homework)

# Declare a list that contains the elements 7, 8, 9, 2, 3, 1, 4, 10, 5, 6 (keep this order)
numb_list = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]

# Display the initial list, sorted ascending (the form of the initial list must be kept)
sorted_list_asc = numb_list.copy()
sorted_list_asc.sort()
print("List sorted ascending:", sorted_list_asc)

# Display the initial list, sorted descending (the for of the initial list must be kept)
sorted_list_desc = numb_list.copy()
sorted_list_desc.sort(reverse=True)
print("List sorted descending:", sorted_list_desc)

# Display a list that contains the even numbers from the sorted list (using slice)
print("List of even elements:", sorted_list_asc[1::2])
print("List of even elements:", sorted_list_desc[::2])

# Display a list that contains the odd numbers from the sorted list (using slice)
print("List of odd elements:", sorted_list_asc[::2])
print("List of odd elements:", sorted_list_desc[1::2])

# Display a list that contains the multiples of 3 (using slice)
print("List of 3's multiple:", sorted_list_asc[2::3])
print("List of 3's multiple:", sorted_list_desc[1::3])


