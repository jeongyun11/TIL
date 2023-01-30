# 10101. count? dict? 
numbers = [int(input()) for i in range(3)]

result = 'Scalene'

if sum(numbers) != 180 :
    result = 'Error'
else  :
    for number in numbers : 
        if numbers.count(number) == 3 :
            result = 'Equilateral'
            break

        elif numbers.count(number) == 2 :
            result = 'Isosceles'
            break

print(result)