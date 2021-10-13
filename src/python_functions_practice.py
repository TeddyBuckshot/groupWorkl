def return_10():
    return 10

def add(num1, num2):
    sum = num1 + num2
    return sum

def subtract(num1, num2):
    sum = num1 - num2
    return sum

def multiply(num1, num2):
    res = num1*num2
    return res

def divide(num1, num2):
    res = num1/num2
    return res

def length_of_string(string):
    return len(string)

def join_string(string1, string2):
    return string1 + string2

def add_string_as_number(string1, string2):
    res = int(string1) + int(string2)
    return res

def number_to_full_month_name(num):
    
    months = [
        "January", 
        "February", 
        "March", 
        "April", 
        "May", 
        "June", 
        "July", 
        "August", 
        "September", 
        "October", 
        "November", 
        "Decemeber"]

    return months[num-1]

def number_to_short_month_name(num):

    months = [
        "January", 
        "February", 
        "March", 
        "April", 
        "May", 
        "June", 
        "July", 
        "August", 
        "September", 
        "October", 
        "November", 
        "Decemeber"]

    res = months[num-1]
    return res[0:3]

def vol_cube(length):
    return length ** 3

def reverse(string):
    return string[::-1]\

def far_con_cels(temp):
    return (temp -32) * 0.5556

