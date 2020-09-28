def number_to_pattern(num, k):
    number_to_symbol = {0: 'A', 1: 'C', 2: 'G', 3: 'T'}
    if k == 1:
        return number_to_symbol[num]
    prefix_index = num // 4
    r = num % 4
    symbol = number_to_symbol[r]
    prefix_pattern = number_to_pattern(prefix_index, k - 1)
    return prefix_pattern + symbol


print(number_to_pattern(7719, 8))
