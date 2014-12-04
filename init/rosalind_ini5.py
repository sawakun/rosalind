fin = open('rosalind_ini5.txt', 'r')
fout = open('output.txt', 'w')
i = 0
for line in fin:
        if i % 2 == 1:
                fout.write(line)
        i = i + 1
