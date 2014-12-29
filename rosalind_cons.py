#fin = open('hoge.txt', 'r')
fin = open('rosalind_cons.txt', 'r')
d = {}
key = ''
for line in fin:
        if line[0] == '>':
                key = line[1:].rstrip()
                continue
        if key != '':
                if d.has_key(key):
                        d[key] += line.rstrip()
                else:
                        d[key] = line.rstrip()

length = 0
for key, value in d.items():
        length = len(value)

a = [0] * length
c = [0] * length
g = [0] * length
t = [0] * length
for key, value in d.items():
        for i in range(len(value)):
                if value[i] == 'A':
                        a[i] += 1
                elif value[i] == 'C':
                        c[i] += 1
                elif value[i] == 'G':
                        g[i] += 1
                elif value[i] == 'T':
                        t[i] += 1

consensus = ''
for i in range(len(a)):
        key = max(a[i], c[i], g[i], t[i])
        if a[i] == key:
                consensus += 'A'
        elif c[i] == key:
                consensus += 'C'
        elif g[i] == key:
                consensus += 'G'
        elif t[i] == key:
                consensus += 'T'

print consensus
print 'A:',
for item in a:
        print item,
print ''
print 'C:',
for item in c:
        print item,
print ''
print 'G:',
for item in g:
        print item,
print ''
print 'T:',
for item in t:
        print item,
