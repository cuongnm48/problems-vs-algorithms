def get_min_max(ints):
    if not ints:  
        return None, None

    min_number = max_number = ints[0]

    for number in ints[1:]:
        if number < min_number: 
            min_number = number
        elif number > max_number: 
            max_number = number

    return min_number, max_number

# Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print("Pass" if ((0, 9) == get_min_max(l)) else "Fail")

l = [-5, -2, -10, -3, -7]  
print("Pass" if ((-10, -2) == get_min_max(l)) else "Fail")

l = [5, 2, 8, 2, 5, 9, 8, 2]  
print("Pass" if ((2, 9) == get_min_max(l)) else "Fail")

print("Pass" if ((None, None) == get_min_max([])) else "Fail")

print("Pass" if ((10, 10) == get_min_max([10])) else "Fail")