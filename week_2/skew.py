text = "TAAAGACTGCCGAGAGGCCAACACGAGTGCTAGAACGAGGGGCGTAAACGCGGGTCCGAT"

def skew(text):
    n = len(text)
    num = 0
    result = [num]
    test = {"G":1,"C":-1,"A":0,"T":0}
    for i in range(0,n):
        num += test[text[i]]
        result.append(num)
    return str(result).lstrip("[").rstrip("]").replace(",","")
print(skew(text))
#
# In a 5' -> 3' direcction, OriC will be located at the point when Skew (GC difference) changes from decreasing to increasing (in the above example, at ~4000000 as @Irene_Zhang suggested.
#     In a 3' -> 5' direction, OriC will be located at the point when Skew changes from increasing to decreasing (in the above example  at ~2000000 position).
