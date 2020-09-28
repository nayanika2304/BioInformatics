
import sys
import argparse
from itertools import product

def arrangements(k):
    result = product('ACGT', repeat = k)
    result = map(list, result)
    words = []
    for item in result:
        word = ''
        for letter in item:
            word += letter
        words.append(word)
    return(words)

# Hamming distance
def HammingDistance(p, q):
    dist = 0
    if len(p) != len(q):
        return('strings have unequal length!')
    else:
        for i in range(len(p)):
            if p[i] != q[i]:
                dist += 1
        return(dist)

# Generate the Neighborhood of a String
def main():

    #check number of arguments
    if len(sys.argv) != 2:
        print('Usage: python3 Neighborhood.py pattern d')
        sys.exit

    pattern = sys.argv[1]
    d = int(sys.argv[2])
    print(' ')
    print('pattern is: %s' % (pattern))
    print('maximum hamming distance is: %d' %(d))
    print(' ')

    def Neighbors(pattern, d):
        print('performing fucntion with: %s' %(pattern))
        if d == 0:
            return(pattern)
        if len(pattern) == 1:
            return('A, C, G, T')
        else:

            #obtain suffix
            suffix = pattern[1:len(pattern)]
            prefix = pattern[0]

            # recursive algorithm (repeat function for each suffix)
            suffixNeighbors = Neighbors(suffix, d)

            # eligible neighbors
            neighborsList = arrangements(len(suffix))
            eligibleList = []
            for neighbor in neighborsList:
                hamming = HammingDistance(suffix, neighbor)
                if hamming <= d and neighbor not in eligibleList:
                    eligibleList.append(neighbor)

            # concatenate prefix to eligible neighbors of suffix
            finalList = []
            for item in eligibleList:
                newItem = prefix + item
                if newItem not in finalList:
                    finalList.append(newItem)

            # concatenate A, C, T, G to suffix itself
            nucleotides = ['A', 'C', 'G', 'T']
            for nucleotide in nucleotides:
                newItem = nucleotide + suffix
                if newItem not in finalList:
                    finalList.append(newItem)

        finalList = ' '.join(str(item) for item in finalList)
        return(finalList)

    result = Neighbors(pattern, d)
    print(result)
    print('count:',len(result))

if __name__ == "__main__":
    main()

'''
# Iterative Approach

def immediateneighbor(pattern):
    neighborhood=[pattern]
    for i in range(len(pattern)):
        symbol=pattern[i]
        for nucleotide in 'ATGC':
            if nucleotide!=symbol:
                neighbor=pattern[:i]+nucleotide+pattern[i+1:]
                neighborhood.append(neighbor)
    return neighborhood

def iterativeneighbors(pattern, d):
    neighborhood=[pattern]
    for j in range(d):
        for string in neighborhood:
            neighborhood=neighborhood+immediateneighbor(string)
            neighborhood=list(set(neighborhood)) #duplicate removal
    return neighborhood
'''
