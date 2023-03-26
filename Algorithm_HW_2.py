#Homework for Algorithm 2 class

def split_half(x):
    length = len(x)
    half = length // 2
    add = 0
    if length % 2:
        add = 1
    left = x[:half + add]
    right = x[half + add:]
    return right + left


test_even = "abcdef"
test_odd = "abcdefg"

result_even = split_half(test_even)
print(result_even)
result_odd = split_half(test_odd)
print(result_odd)

def unique_char(s):
    chars = set()

    for char in s:
        if char in chars:
            return False
        else:
            chars.add(char)

    return True

test_pos = "timer"
test_neg = "tirer"
result_positive = unique_char(test_pos)
print(result_positive)
result_neg = unique_char(test_neg)
print(result_neg)

