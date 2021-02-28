# 1
def fizz_buzz(number):
    if number == 0:
        return str(number)
    if number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
    else:
        return str(number)


# 2
def count_profit(data):
    return int(data.get('sell_price') * data.get('inventory') - data.get('cost_price') * data.get('inventory'))


# 4
def square_area(radius):
    return radius ** 2 + radius ** 2


# 5
def list_of_multiples(number, length):
    my_list = [number * i for i in range(1, length + 1)]
    return my_list


# 6
def date_formatted(date):
    new_date = date.replace("/", "")
    i = len(new_date) - 1
    rev_date = ""
    while i >= 0:
        rev_date += new_date[i]
        i -= 1
    return rev_date


# 7
def check_lines(l1, l2):
    a1, b1, a2, b2 = l1[0], l1[1], l2[0], l2[1]
    if a1 * b2 - a2 * b1 == 0:
        return True
    else:
        return False


# 8
def vol_shell(r1, r2):
    import math
    R = abs(r1)
    r = abs(r2)
    if R < r:
        R, r = r, R
    v_betw_sph = 4 / 3 * math.pi * (R ** 3 - r ** 3)
    if v_betw_sph >= 0:
        return round(v_betw_sph, 3)


# 9
def identify_student(name):
    GUEST_LIST = {
        "Randy": "Germany",
        "Karla": "France",
        "Wendy": "Japan",
        "Norman": "England",
        "Sam": "Argentina"
    }

    if name in GUEST_LIST:
        return "Hi! I'm {}, and I'm from {}.".format(name, GUEST_LIST[name])
    else:
        return "Hi! I'm a guest."


# 10
def stupid_addition(param1, param2):
    if type(param1) == int and type(param2) == int:
        str_param = str(param1) + str(param2)
        return str_param
    elif type(param1) == str and type(param2) == str:
        sum_param = int(param1) + int(param2)
        return sum_param
    else:
        return None


# 11
def is_repdigit(number):
    if number < 0:
        return False
    elif number == 0:
        return True
    else:
        str_number = str(number)
        list_number = list(str_number)
        count_number = list_number.count(list_number[0])
        if count_number == len(list_number):
            return True
        else:
            return False


# 12
def concat(*n):
    full_list = []
    for item in n:
        for i in range(len(item)):
            full_list.append(item[i])
    sort_full_list = sorted(full_list)
    return sort_full_list
