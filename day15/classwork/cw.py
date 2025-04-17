#N1

def filter_divisible(i, n):
    result = [] 
    for num in i :
        if num % n == 0:  
            result.append(num)  
    return result

# მაგალითი
numbers = [1, 23, 165, 2, 3, 92, 10, 34, 911]
divider = 3
filtered_numbers = filter_divisible(numbers, divider)
print(filtered_numbers)
#N2
def reverse_list(l):
    return l[::-1]