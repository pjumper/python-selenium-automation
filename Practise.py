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
