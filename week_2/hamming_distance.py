pattern1= "CAGAAAGGAAGGTCCCCATACACCGACGCACCAGTTTA"
pattern2 = "CACGCCGTATGCATAAACGAGCCGCACGAACCAGAGAG"

def hamming_problem(pattern1,pattern2):
    count = 0
    for i,j in zip(pattern1,pattern2):
        if i != j:
            count +=1
    return count

print(hamming_problem(pattern1,pattern2))
