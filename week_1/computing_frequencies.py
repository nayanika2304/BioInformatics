def pattern_to_number(pattern):
    if len(pattern) == 0:
        return 0
    symbol_to_number = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
    n = len(pattern)
    prefix = pattern[:n - 1]

    symbol = pattern[n - 1]
    return 4 * pattern_to_number(prefix) + symbol_to_number[symbol]


def computing_frequencies(text, k):
    frequency_array = []
    n = len(text)
    for i in range(4 ** k):
        frequency_array.append(0)
    for i in range(n - k + 1):
        pattern = text[i:i + k]
        j = pattern_to_number(pattern)
        frequency_array[j] = frequency_array[j] + 1
    result = ""
    for item in frequency_array:
        result = result + " " + str(item)
    return result

pattern="CGGCGTTGGAGTGGAAAA"
print(pattern_to_number(pattern))
#print(computing_frequencies(pattern,7))


#PatternToNumber(AGT) = 4 · PatternToNumber(AG) + SymbolToNumber(T) = 8 + 3 = 11
# where SymbolToNumber(symbol) is the function transforming symbols A, C, G, and T into the respective integers 0, 1, 2, and 3.

# patternToNumber = ATGCAA
# A=0 C=1 G=2 T=3
# 032100
# (4^5 *0=0)+(4^4 *3=768)+(4^3 *2=128)+(4^2 *1=16)+ (4^1 *0=0)+ (4^0 *0=0)=912

#numberToPattern
# To go backward from a base-anything number, you divide the final number (5437 in this case) by the base, 4,  k = 7 times, keeping track of the remainder: ﻿﻿
#
#
# 5437 / 4 = 1359 R 1
# 1359 / 4 = 339 R 3
# 339 / 4 = 84 R 3
# 84 / 4 = 21 R 0
# 21/4 = 5 R 1
# 5/4 = 1 R 1
# 1/4 = 0 R 1
# Take the remainders from the bottom up and you get:
#
# 1110331, corresponding lexicographically to ﻿CCCAGGC
#
# Similarly we can look at ﻿going backward from 912 (from previous question) to ATGCAA (k = 6) in the same way:
#
# 912/4 = 228 R 0
# 228/4 = 57 R 0
# 57/4 = 14 R 1
# 14/4 = 3 R 2
# 3/4 = 0 R 3
# 0/4 = 0 R 0
# Bottom up we get 032100 corresponding to ATGCAA.
