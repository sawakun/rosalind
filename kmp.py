fin = open('hoge.txt', 'r')
#fin = open('rosalind_kmp.txt', 'r')
d = {}
key = ''
for line in fin:
        if line[0] == '>':
                key = line[1:].rstrip()
                continue
        if key != '':
                if d.has_key(key):
                        d[key] = d[key] + line.rstrip()
                else:
                        d[key] = line.rstrip()

length = 0
s = ''
for key, value in d.items():
        s = value
        print key
        print value
        length = len(value)
print '012345678901234567890'

result = [0] * length
for k in range(len(s)):
        if k == 0: 
                continue
        for j in range(1,k):
                print 'j, k=', j, k
                print 's[j:k]', s[j:k]
                print 's[0:k-j]', s[0:k-j]
                for i in range(1,len(s[j:k])):
                        print 'i=', i
                        print s[j:k][0:i] 
                        print s[0:k-j][0:i]
                        if s[j:k][0:i] != s[0:k-j][0:i]:
                                if i-1 > result[k]:
                                        result[k] = i-1
                                break

for r in result:
        print r,
