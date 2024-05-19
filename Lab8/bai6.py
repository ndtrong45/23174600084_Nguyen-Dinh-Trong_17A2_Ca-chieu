numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print(odd_numbers)  

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  

cubed_numbers = list(map(lambda x: x**3, numbers))
print(cubed_numbers) 

even_cubed_numbers = list(map(lambda x: x**3, filter(lambda x: x % 2 == 0, numbers)))
print(even_cubed_numbers)  

odd_squared_numbers = list(map(lambda x: x**2, filter(lambda x: x % 2 != 0, numbers)))
print(odd_squared_numbers)  