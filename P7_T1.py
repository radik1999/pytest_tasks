def sum_numbers(str_numbers):
    list_numbers = list(str_numbers.split())
    int_numbers = []
    for i in range(len(list_numbers)):
        int_numbers.append(int(list_numbers[i]))
    return sum(int_numbers)


def my_sum_numbers(str_numbers):
    return sum(map(int, str_numbers))
