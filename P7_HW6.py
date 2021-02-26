##Написати функцію is_prime, яка приймає 1 аргумент - число від 0 до 1000,
##і повертає True, якщо воно просте, і False - в іншому випадку.

def is_prime(number):
    list_numbers = []
    for i in range(1000):
        list_numbers.append(i)

    count_divisors = []
    while number in list_numbers:
        for i in range(1, 1000):
            if number % i == 0:
                count_divisors.append(i)
        if len(count_divisors) == 2:
            return True
        else:
            return False
    else:
        return False


