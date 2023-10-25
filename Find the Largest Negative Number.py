'''def find_largest_missing_negative(numbers):
    numbers.sort
    
    for i in numbers:
        if i == list:
            list -= 1
        else:
            return list
    return list

numbers = [-3, -2, -4, -5, -7]

result = find_largest_missing_negative(numbers)
print(result)'''


'''
def find_largest_negative(numbers):
    largest_negative = None
    
    for num in numbers:
        if num < 0 and (largest_negative is None or num > largest_negative):
            largest_negative = num
    
    return largest_negative

# Example usage:
my_list = [-1, -4, -6, -3]
largest_negative = find_largest_negative(my_list)

if largest_negative is not None:
    print("The largest negative number is:", largest_negative)
else:
    print("No negative numbers found in the list.")'''


'''
def find_largest_negative(numbers):
    largest_negative = None
    
    for num in numbers:
        if num < 0:
            if largest_negative is None or num > largest_negative:
                largest_negative = num
    
    return largest_negative

# Example usage:
my_list = [10, -5, -8, 15, -20, -3]
largest_negative = find_largest_negative(my_list)

if largest_negative is not None:
    print("The largest negative number is:", largest_negative)
else:
    print("No negative numbers found in the list.")'''









