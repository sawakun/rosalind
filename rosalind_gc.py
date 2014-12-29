#fin = open('hoge.txt', 'r')
fin = open('rosalind_gc.txt', 'r')
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

gc = {}
for key, value in d.items():
        count = 0
        for i in range(len(value)):
                if value[i] == 'G' or value[i] == 'C':
                        count = count + 1
        gc[key] = float(count) / len(value) * 100.0

max_value = 0.0
max_key = ''
for key, value in gc.items():
        if value > max_value:
                max_value = value
                max_key = key

print max_key
print('%.6f' % gc[max_key])

