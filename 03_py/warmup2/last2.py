def last2(str):
  last2 = str[-2:]
  counter = 0
  for c in range(len(str)-2): #subtract 2 to prevent out of bounds
    if str[c:c+2] == last2:
      counter+=1
  return counter

print(last2('hixxhi')) #→ 1	
print(last2('xaxxaxaxx')) #→ 1	
print(last2('axxxaaxx')) #→ 2	
print(last2('xxaxxaxxaxx')) #→ 3	
print(last2('xaxaxaxx')) #→ 0	
print(last2('xxxx')) #→ 2	
print(last2('13121312')) #→ 1	
print(last2('11212')) #→ 1	
print(last2('13121311')) #→ 0	
print(last2('1717171')) #→ 2	
print(last2('hi')) #→ 0	
print(last2('h')) #→ 0	
print(last2('')) #→ 0