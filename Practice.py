#Practice Coding

def is_almost_palindrome(s):
    for i in range(len(s)):
        current_str = s[:i] + s[i + 1:]
        if current_str == current_str[::-1]:
            return True
    return False


test_pos = "radkar"
test_neg = "radario"
result_pos = is_almost_palindrome(test_pos)

def find_missing_number(arr1, arr2):
    arr1.sort()
    arr2.sort()

    for i in range(len(arr2) - 1):
         if arr1[i] != arr2[i]:
            return arr1[i]

    return arr1[-1]

test_arr1 = [2, 3, 1, 4]
test_arr2 = [4, 1, 3]
result = find_missing_number(test_arr1, test_arr2)
print(result)

    #for num1, num2 in zip(arr1, arr2):
        #if num1 != num2:
         #   return num1


def find_sum(arr):
    