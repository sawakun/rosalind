s = 'AGCAATAGAGCCCATTAATGACATGGAGGCACCGAAAACGCCTTACTGCAGATGGCCATCTAGAACCCTTCATACTCATCTTCAAGATCTACCCAATTGTGAGGCTGATCGGTTGAACCGGGAGTCCCCTACTCAGAAGGCGTATAATCGTGAAGTCTTGGTTTCAATGCATACCGTCGACATGCGATGGTTTTTACAATTATCGTGAGCAAGGGGGGATTTGATACAGATATAGGTAATACAGAATATGCGGAATTTGGTTGCACTGTCCAGGGCCCAGTAAACGCATGCCGTGGCTGGTCAGCTGAATTCACGATCGCAGAGACGTAGCTAGGATGGATCTCCTTCCGTCGGTCTACGATGAAGGCCCTTAGTGCCCCCAATTTTCAGTGGAAGATCGATATGCCTCGGATTAACGCCACTCTCCCAAACAATTCGATTCCTTTGAAGGAGTCACGGACATAGGGCTTTTGGAAACAGAGTTCGCTGATCATTTCCGTACAAAGAGTCGCAACACAATATAGCGCGGTCTGCAACAGCACAGTGCACGTTAAGACTTAGGACAAGCCCAGGGCCTATGAACTAGAGTTGCGCACGGTAGCCCTATAAGACTGCGACTGCAGTCGCCCCTGAAGACGTAAGGCGTGCGCTAAAATACAGTAGCGAGCAAGGATACTTTGCGAAAATTAGTATTACCAGATTCCCAACTCAGTAAACATTAACAATTGCGTTCAATGCAGACAATCAAAATGTCCTGCTTTAGTATATCTAAGTGATAACAGTTATTGGCTCACCTTAGGAACGTTACGTCAATTCACGGGGTTGCCCAATAGTAACCGATATTTTGAGGGCATAAGGAGTTTCTGGTACCATGAGATTAGATGGGTAGGAGCCGGGGCCAGGCCCTTAGCAAGATGTCTAAAAAATGGGACTGTTCTTGTAAGAGTAGGGTCGGGTATAAA'
result = ''
for i in range(len(s)):
        if s[len(s)-i-1:len(s)-i] == 'T':
                result = result + 'A'
        if s[len(s)-i-1:len(s)-i] == 'A':
                result = result + 'T'
        if s[len(s)-i-1:len(s)-i] == 'G':
                result = result + 'C'
        if s[len(s)-i-1:len(s)-i] == 'C':
                result = result + 'G'
print result