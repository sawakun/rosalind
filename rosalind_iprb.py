#k = 2
#m = 2
#n = 2

k = 15 
m = 26 
n = 18
total = (k + m + n) * (k + m + n - 1) / 2 * 4
allele = m * (m - 1) / 2 + n * (n - 1) / 2 * 4 + m * n * 2

print '%.5f' % (1.0 - float(allele) / total)

