

def print_sum_and_mult(arr):
    sum_of_list = 0
    mult_of_list = 1
    for element in arr:
        sum_of_list += element
        mult_of_list *= element

    print(f'The original list: {arr}')
    print(f'Sum of all elements: {sum_of_list}')
    print(f'Multiplication of all elements: {mult_of_list}')

test_list = [1, 7, 3]
print_sum_and_mult(test_list)

def find_max_element(arr):
    max_index = 0
    max_num = arr[max_index]

    for i in range(1, len(arr)):
        if arr[i] > max_num:
            max_num = arr[i]
            max_index = i
    print(f'Max number: {max_num}')
    print(f'Max index: {max_index}')

test_list = [5, 32, 5, 4, 16, 17, 3]
find_max_element(test_list)

def sum_between_min_and_max(arr):
    if len(arr) <= 2:
        return 0
    min_item = max_item = 0
    min_index = max_index = 0
    i = 1
    while i < len(arr):
        if arr[i] > max_item:
            max_item = arr[i]
            max_index = i
        if arr[i] < min_item:
            min_item = arr[i]
            min_index = i
        i += 1

    return sum(arr[(min_index, max_index) + 1:max(min_index, max_index)])

test_list1 = [2, 1, 5, 7, 8, 4]
test_list2 = [2, 7, 5, 4, 1, 3]
test_list3 = [1, 2]

test_result1 = sum_between_min_and_max(test_list1)
test_result2 = sum_between_min_and_max(test_list2)
test_result3 = sum_between_min_and_max(test_list3)