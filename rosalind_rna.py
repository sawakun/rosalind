s = 'AGAGGCTATTCAAATGTGAATGGGGCCAGCCCCCTGAAGAAGTCAGATCTCCGGCAGGCCTTCGCCGCACAACGATCGGGATCTTTGGCGCGAATTTTCTGACCGCCGCGGACAACACACGCGTGGTAGCTCTAGTCAAAGTGCTAATTCTGGCCTTTCGCCCACGTTGTGCGTTTTGTTTAAAGGCAGCACCTGGGGACGTCGTCGGCTTCGTCCAGCAATTAAGAGCCCTTAGGCTTTGTCCGACATACATCGTCGGTCTCTGCATCCGTTTCAGCATCTATTCGACGGTCAGTGAGCATTCTATATAAGTTACTGGTCCTACGCAACCGTTTCAATTCTCCTGGACTAGCCCGCCTTAAGTCGCAGTTGAGACGTCGCTCCTTTATTTGCCCGTCTGATTTATGGGAACTACGCGCAGAGATGTGGGTCTGTGAAACGGCCCCTGTAGTGCGATCGCACCGGATCCCGCCTGACAAATTATTTGATAGCACAAAAACCAACGAATGCACTTGTCCCGGTTAGGGCCCTTTGTACTGTTTCGCCTCACATAAATGGGAGCTTGTAGTTCGGCGCTCGCTTCCTTGAAACGTACATACAGGACAGTTTAAGCTTGCTCACATGCAAACTGTTTTGCCACTTATCAGACGAGTTAATAGGAGAAAGGCTCGAGAGGTTGGCGAAGTGTACAGGCTTACGACAACTGGTTGCCATACGGCGCCGTTTGCCGTCCATAGCTTAGAATTGGAACCACAGCCCTTCGGAAAGAGGCCCGAAGGTATTCAACCAGCGACTCATGCCGCCTATAGTTAGGGGGTAAAAGCATCACATCAACGTCACGCTCTATAAGGTAAAGCCTTGCCGTTTACTAGGATTTCTTCAGACGGTTCCAAAGAGCTGGCATCCGCCATAATTTAGGCAGGTGCGTTAGTGTGGAGGCTACTTGGAACGAT'
result = ''
for i in range(len(s)):
        if s[i:i+1] == 'T':
                result = result + 'U'
        else:
                result = result + s[i:i+1]
print result