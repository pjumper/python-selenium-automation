
def even_odd(arr: list):
    next_even = 0
    next_odd = len(arr) - 1
    while next_even < next_odd:
        if arr[next_even] % 2 == 0:
            next_even += 1
        else:
            arr[next_even], arr[next_odd] = arr[next_odd], arr[next_even]
            next_odd -= 1

    return arr

test_list = [5, 3, 4, 6, 10, 9, 11]
print(test_list)
test_result_list = even_odd(test_list)
print(test_result_list)
print(test_list)


def plus_one(arr:list):
    arr[-1] += 1
    for i in reversed(range(1, len(arr))):
        if arr [i] != 10:
            break
        arr[i] = 0
        arr[i - 1] += 1
    if arr[0] == 10:
        arr[0] = 1
        arr.append(0)
    return arr


test_digit1 = [1, 2, 3]
test_digit2 = [1, 9, 9]
test_digit3 = [9, 9, 9]

print(plus_one(test_digit1))
print(plus_one(test_digit2))
print(plus_one(test_digit3))
