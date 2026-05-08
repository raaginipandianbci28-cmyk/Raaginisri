def transform_numbers(numbers):
    transformed_list = [x**2 if x % 2 == 0 else x**3 for x in numbers]
    return tuple(transformed_list)
my_list = [1, 2, 3, 4, 5]
result_tuple = transform_numbers(my_list)
print(result_tuple)
