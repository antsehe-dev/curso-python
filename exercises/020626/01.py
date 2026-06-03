# Create a Python program that identifies all numbers between 100 and 300 
# (inclusive) that are divisible by 7 but not multiples of 5. The identified 
# numbers should be displayed in a single line, separated by commas


init = 100
final = 300
result_numbers = []

for i in range (init,final+1):
    if i%7 == 0 and i%5 != 0:
        result_numbers.append(i)

print(result_numbers)       