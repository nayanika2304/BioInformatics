pattern = 'GAATGC'
text = 'ACGTTGCATGTCGCATGATGCATGAGAGCT'
d = 3


def hamming_problem(pattern1,pattern2):
    count = 0
    for i,j in zip(pattern1,pattern2):
        if i != j:
            count +=1
    return count

def approx_pattern_matching(pattern,text,d):
    n = len(text)
    k = len(pattern)
    count = 0
    for i in range(n-k+1):
        match = text[i:i+k]
        if hamming_problem(match,pattern) <= d:
            count = count +1
    return count

print(approx_pattern_matching(pattern,text,d))
