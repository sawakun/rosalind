# read FASTA
#fin = open('hoge.txt', 'r')
fin = open('rosalind_orf.txt', 'r')
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

for value in d.values():
  dna = value
  break
#print dna

# transcript
rna = ''
for i in range(len(dna)):
  if dna[i] == 'T':
    rna += 'U'
  else:
    rna += dna[i]
#print rna

# codon_table
codon_table = {
    'UUU':'F',     'CUU':'L',     'AUU':'I',     'GUU':'V',
    'UUC':'F',     'CUC':'L',     'AUC':'I',     'GUC':'V',
    'UUA':'L',     'CUA':'L',     'AUA':'I',     'GUA':'V',
    'UUG':'L',     'CUG':'L',     'AUG':'M',     'GUG':'V',
    'UCU':'S',     'CCU':'P',     'ACU':'T',     'GCU':'A',
    'UCC':'S',     'CCC':'P',     'ACC':'T',     'GCC':'A',
    'UCA':'S',     'CCA':'P',     'ACA':'T',     'GCA':'A',
    'UCG':'S',     'CCG':'P',     'ACG':'T',     'GCG':'A',
    'UAU':'Y',     'CAU':'H',     'AAU':'N',     'GAU':'D',
    'UAC':'Y',     'CAC':'H',     'AAC':'N',     'GAC':'D',
    'UAA':'Stop',  'CAA':'Q',     'AAA':'K',     'GAA':'E',
    'UAG':'Stop',  'CAG':'Q',     'AAG':'K',     'GAG':'E',
    'UGU':'C',     'CGU':'R',     'AGU':'S',     'GGU':'G',
    'UGC':'C',     'CGC':'R',     'AGC':'S',     'GGC':'G',
    'UGA':'Stop',  'CGA':'R',     'AGA':'R',     'GGA':'G',
    'UGG':'W',     'CGG':'R',     'AGG':'R',     'GGG':'G'
    }

# annotation
start = 'AUG'

annot = []
for i in range(len(rna)):
  if rna[i] == start[0]:
    if i < (len(rna)-len(start)+1):
      annot.append(i)

orfs = []
for i in annot:
  if rna[i:i+len(start)] == start:
    orfs.append(i)

#for orf in orfs:
#  print orf,
#print ''

# transcript
result = []
for orf in orfs:
  protein = ''
  while orf + 3 < len(rna):
    codon = rna[orf:orf+3]
    amino = codon_table[codon]
    if amino == 'Stop':
      break
    else:
      protein += amino
    orf += 3
  result.append(protein)
  
for r in result:
  print r

