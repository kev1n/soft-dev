def string_splosion(str):
  answer = ""
  for index in range(len(str)+1): #range-len to loop through indexes
    answer+=str[0:index]
  return answer

print(string_splosion('Code')) #→ 'CCoCodCode'	
print(string_splosion('abc')) #→ 'aababc'	
print(string_splosion('ab')) #→ 'aab'	
print(string_splosion('x')) #→ 'x'	
print(string_splosion('fade')) #→ 'ffafadfade'	
print(string_splosion('There')) #→ 'TThTheTherThere'	
print(string_splosion('Kitten')) #→ 'KKiKitKittKitteKitten'	
print(string_splosion('Bye')) #→ 'BByBye'	
print(string_splosion('Good')) #→ 'GGoGooGood'	
print(string_splosion('Bad')) #→ 'BBaBad'