# Conditional programming, loops and functions (Homework)


# Write a function with an undefined number of parameters that returns the sum of integer or float parameters
def add_int_float(*args, **kwargs):
    count = 0
    for parameter in args:
        if "float" in str(type(parameter)) or "int" in str(type(parameter)):
            count += parameter
    return count


# Test case 1: int_float_sum(1, 5, -3, 'abc', [12, 56, 'cad']) => return 3 (1 + 5 - 3)
print("sum of integer or float parameters =", add_int_float(1, 5, -3, 'abc', [12, 56, 'cad']))

# Test case 2: int_float_sum() => return 0
print("sum of integer or float parameters =", add_int_float())

# Test case 3: int_float_sum(2, 4, 'abc', param_1=2) => return 6
print("sum of integer or float parameters =", add_int_float(2, 4, 'abc', param_1=2))

# Test case 4: int_float_sum('abc', 1.4, 2, 4) => return 7.4
print("sum of integer or float parameters =", add_int_float('abc', 1.4, 2, 4), "\n")

# Write a recursive function with an integer parameter that returns:
# sum of all numbers from [0, n]
# sum of even numbers from [0, n]
# sum of odd numbers from [0. n]

# define a list that will hold the 3 sums from the recursive function:
# index 0 => sum of all numbers from [0, n]
# index 1 => sum of even numbers from [0, n]
# index 2 => sum of odd numbers from [0. n]
my_list = [0, 0, 0]


def return_sum(n):
    global my_list
    if n == 0:
        return my_list

    if n % 2 == 0:
        my_list[1] += n
    else:
        my_list[2] += n

    my_list[0] += n
    return_sum(n - 1)
    return my_list


# Test case: input parameter 5 => expected list with elements [15, 6, 9]
print("Return values from the recursive function:", return_sum(5))


# Write a function that reads a value from the keyboard and returns the value if it's an integer, otherwise returns 0
def print_user_input():
    user_input = 0
    try:
        user_input = int(input("Enter a value from the keyboard: "))
    except ValueError:
        pass
    return user_input
