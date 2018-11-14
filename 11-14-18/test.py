# list1 = [1, 5, 3, 6, 7]
# list2 = [3, 6, 9, 10, 2]
# list3 = []

# for n1 in list1:
#     sum = 0
#     for n2 in list2:
#         sum += n1 * n2
#     list3.append(sum)

# print(list3)

def factorNumber(n):
    
    factors = []

    for i in range(1, n):
        if n % i == 0:
            factors.append(i)
    
    return factors

print(factorNumber(50))