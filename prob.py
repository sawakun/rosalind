from math import *

#s = 'ACGATACAA'
#A = '0.129 0.287 0.423 0.476 0.641 0.742 0.783'
s = 'AGTGCCGCTTGTGCCGCTCGAGGCCGCAAACTAAAATAGGGTATTGGTGGGATCAACCGTCCAGTGAGGAGTAACGGGGCGATAAATTC'
A = '0.083 0.114 0.180 0.227 0.298 0.369 0.442 0.478 0.531 0.597 0.640 0.677 0.725 0.779 0.847 0.902'

result = []
for gc in A.split(' '):
        r = 1.0
        for i in range(len(s)):
                if s[i] == 'G' or s[i] == 'C':
                        r *= float(gc)/2
                else:
                        r *= (1 - float(gc))/2
        result.append(log10(r))

for r in result:
        print '%.3f' % r,
