array = [1, 2, 3, 4, 5]
reversed_array = []
k = int(input("How many times you wanna rotate : "))
reversed_array = array[-k:] + array[:-k]
print(reversed_array)