'''
How many patterns are there in the text
'''

text="CGCGATACGTTACATACATGATAGACCGCGCGCGATCATATCGCGATTATC"
pattern = "CGCG"


def pattern_count(text, pattern):
    count = 0
    for i in range(len(text) - len(pattern) + 1):
        if text[i:i + len(pattern)] == pattern:
            count = count + 1
    return count


print(pattern_count(text, pattern))

