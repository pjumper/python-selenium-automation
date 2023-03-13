def sum_of_digits(number: int):
    result = 1
    for i in range(2, number + 1):
        result += i

    print(f"Sum of digits {number} is {result}")

test_number = 8
sum_of_digits(test_number)

def max_number(n: int):
    result = max(n)

    print(f"Max number is {result} ")

test_max = (46, 125, 48)
max_number(test_max)

def count_digits(num):
    even_numbers = 0
    odd_numbers = 0
    for digit in str(num):
        if int(digit) % 2 == 0:
            even_numbers += 1
        else:
            odd_numbers += 1

    print(f"Even Number:  {even_numbers}")
    print(f"Odd Number:  {odd_numbers}")

num = 801309
count_digits(num)

