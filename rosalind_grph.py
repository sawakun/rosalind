#fin = open('hoge.txt', 'r')
fin = open('rosalind_grph.txt', 'r')
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

k = 3

result = []
for key, value in d.items():
  for key2, value2 in d.items():
    if key == key2:
      continue
    else:
      if value[len(value)-k:len(value)] == value2[0:k]:
          result.append(key + ' ' + key2)

for r in result:
  print r
