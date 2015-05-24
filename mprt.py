import urllib2

# get protein code
# dev
#proteins = ["A2Z669", "B5ZC00", "P07204_TRBM_HUMAN", "P20840_SAG1_YEAST"]

# from file
f = open('mprt.txt')
proteins = f.readlines() 
f.close()

# get fasta
UNIPROT = "http://www.uniprot.org/uniprot/"

for protein in proteins:
  # get data
  req = urllib2.Request(UNIPROT + protein.rstrip()  + ".fasta")
  response = urllib2.urlopen(req)
  lines = response.readlines()
  motif = ''
  for line in lines:
    if line[0] != '>':
      motif += line.rstrip()

  # find N-glycosylation
  locations = []
  for i in range(len(motif) - 4):
    if motif[i] == 'N':
      if motif[i+1] != 'P':
        if motif[i+2] == 'S' or motif[i+2] == 'T':
          if motif[i+3] != 'P':
            locations.append(i+1)

  # output
  if len(locations) != 0:
    print protein.rstrip()
    for loc in locations:
      print loc,
    print ''
  
