def find_all_odds(lst):
    odds_list = []

    for element in lst:
        if element % 2 == 1:
            odds_list.append(element)

    return odds_list




def string_lengths(strings):
    lengths = []

    for string in strings:
        length = len(string)
        lengths.append(length)

    return lengths

def compare_lists(lst1=[], lst2=[]):
    lst1_set = set(lst1)
    lst2_set = set(lst2)
    set_intersection = lst1_set.intersection(lst2_set)

    return len(set_intersection)

def trim_list(lst, elements_to_trim):
    trimmed_list = []

    for idx in range(len(lst) - elements_to_trim):
        element = lst[idx]
        trimmed_list.append(element)

    return trimmed_list

def running_sums(numbers):
    sums = []

    current_sum = 0
    for number in numbers:
        current_sum += number
        sums.append(current_sum)

    return sums
