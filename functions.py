def find_all_odds(lst):
    odds_list = []

    for element in lst:
        if element % 2 == 1:
            odds_list.append(element)

    return odds_list
