#AA-AA 1
#AA-Aa 1
#AA-aa 1
#Aa-Aa 0.75
#Aa-aa 0.5
#aa-aa 0
ev = [2.0, 2.0, 2.0, 1.5, 1.0, 0.0]
input = '1 0 0 1 0 1'
input = '16778 17904 16086 18589 18916 19307'
populations =  input.split(' ')
result = 0.0
for i in range(len(populations)):
  result += float(populations[i]) * ev[i]
print result
