def sum_of_square(number):
    sum = 0
    for i in range(1,number+1):
        sum = i**2 + sum
    return sum
def sqaure_of_sum(number):
    sum = 0 
    for i in range(1,number+1):
        sum = i + sum
    return sum**2
difference = abs(sum_of_square(100)-sqaure_of_sum(100))
print(difference)