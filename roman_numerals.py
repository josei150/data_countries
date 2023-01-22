from typing import List, Tuple

roman_numbers: List[Tuple[str, int]] = [("I", 1), ("V", 5), ("X", 10), ("L", 50), ("C", 100), ("D", 500), ("M", 1000)]

def roman(number) -> str:
    new_list_numbers = []
    result_number: str = ""
    limit_up = 0
    limit_down = 0

    first_case = in_roman_numbers(number)

    if first_case:
        return first_case[0]

    while number >= 1:
        new_list_numbers = []
        
        if number // 1 < 10:
            result_number, number = search_roman_number(number, limit_up, limit_down, new_list_numbers, 1, result_number)
            if number == 0:
                break
        elif number // 10 < 10:
            result_number, number = search_roman_number(number, limit_up, limit_down, new_list_numbers, 10, result_number)
            if number == 0:
                break
        elif number // 100 < 10:
            result_number, number = search_roman_number(number, limit_up, limit_down, new_list_numbers, 100, result_number)
            if number == 0:
                break
        elif number // 1000 < 10:
            result_number, number = search_roman_number(number, limit_up, limit_down, new_list_numbers, 1000, result_number)
            if number == 0:
                break
    return result_number

    
def set_limits(number, limit_up, limit_down, new_list):
    """
    Returns a list of Roman numerals less than the entered value and one greater than it and also determines 
    the upper and lower bounds of that list according to the entered value
    """
    for index, number_in_list in enumerate(roman_numbers):
        if roman_numbers[index][1] < number:
            new_list.append(number_in_list)
            limit_down = number_in_list
            continue
        new_list.append(number_in_list)
        break
    limit_up: Tuple[str, int] = new_list[-1]
    return limit_up, limit_down, new_list

def search_roman_number(number, limit_up, limit_down, new_list, divisor, result_number):
    """
    Searches for the correct conversion of the entered number and returns a tuple of the number in Roman and 
    the remainder of its inner operation
    """
    
    new_number = (number // divisor) * divisor
    final_case = 0
    limit_up, limit_down, new_list_numbers = set_limits(number, limit_up, limit_down, new_list)
    first_case = in_roman_numbers(new_number)
    
    if first_case:
        result_number += first_case[0]
        final_case += first_case[1]
        if final_case == number:
            return result_number, 0
        else:
            return result_number, number % divisor

    if limit_up == first_case or limit_down == first_case:
        result_number += first_case[0]
        return result_number, number % divisor

    for i in new_list_numbers:
        if limit_up[1] - i[1] == new_number:
            result_number += i[0] + limit_up[0]
            return result_number, number % divisor

    new_list_numbers.reverse()
    for i in new_list_numbers:
        if new_list_numbers[0] == limit_down:
            break
        else:
            new_list_numbers.pop(0)

    while final_case != new_number:
        if new_list_numbers[0][1] + final_case <= new_number:
            result_number += new_list_numbers[0][0]
            final_case += new_list_numbers[0][1]
        else:
            new_list_numbers.pop(0)

        if final_case == new_number:
            return result_number, number % divisor

def in_roman_numbers(number) -> Tuple[str, int] or None:
    """
    Returns a tuple if the value is already in the tuple list, otherwise returns None
    """
    for n in roman_numbers:
        if number in n:
            return n

if __name__ == "__main__":
    print(roman(9))
    print(roman(225))
    print(roman(11))
    print(roman(5))
