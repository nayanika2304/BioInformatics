def string_from_gapped_patterns(rp_list, k, d):
    read_1 = ""
    read_2 = ""

    # Add all first letters from LEFT and RIGHT sides
    # Do NOT include last line from both, LEFT and RIGHT sides
    for kmer in rp_list[:-1]:
        read_1 += kmer[0][0]
        read_2 += kmer[1][0]

    # Add ONLY last kmers (whole kmer) from both, LEFT and RIGHT sides.
    read_1 += rp_list[-1][0]
    read_2 += rp_list[-1][1]

    # Use the formula from the task description
    # k + d + k + n - 1      (n is the length of the list of pairs)
    str_length = k + d + k + len(rp_list) - 1

    # Store the length of the first read (length of read_1 is the same as read_2)
    read_length = len(read_1)

    # Store the difference between length of the read and
    # and a total expected length of combined reads (as per formula above/in the task)
    match_length = str_length - read_length


    # Search for overlap:
    # Here, just use 'match_length' to check if slices/parts
    # from read_1 and read_2 are the same, and if Yes, return
    # read_1 + only last characters from read_2, based on the 'match_length'

    if read_1[match_length:] == read_2[:-match_length]:
        return read_1 + read_2[-match_length:]

    return None

with open('dataset_6206_4.txt', 'r') as datafile:
    lines = datafile.readlines()
    args = lines[0].strip().split(" ")
    k = int(args[0])
    d = int(args[1])
    pairs = [[pair[0:k],pair[k+1:k+k+1]] for pair in lines[1:]]
    expected = lines[-1].strip()

print(string_from_gapped_patterns(pairs,k,d))

