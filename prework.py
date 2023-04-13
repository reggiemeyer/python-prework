# Question #1
# Write a function to print "hello_USERNAME!" USERNAME is the input of the function.

def hello_name(user_name):
    print("Hello, " + user_name + "!")

hello_name("Reggie")

# Question #2
# Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing

def first_odds(number):
    return [x for x in range(0, number) if x % 2 == 1]
first_odds(100)

# Questions #3
# Please write a Python function, max_num_in_list to return the max number of a given list.

def max_num_in_list(a_list):
    max = a_list[0]
    for a in a_list:
        if a > max:
            max = a
    return max
print(max_num_in_list([1,5,3,6,9,2,3]))

# Question #4
# Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. The return should be boolean Type (true/false)

def is_leap_year(a_year):
    leap = False

    if a_year % 400 == 0:
        leap = True
    elif a_year % 4 == 0 and a_year % 100 !=0:
        leap = True
    return leap

print(is_leap_year(1999))

# Question #5
# Write a function to check to see if all numbers in list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers.

def is_consecutive(a_list):
    a_list = sorted(a_list)
    if a_list:
        return a_list == list(range(a_list[0], a_list[-1] + 1))
    else:
        return False
    
a_list = [1,2,3,4,7]
print(is_consecutive(a_list))
