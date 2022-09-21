def missing_char(str, n):
  return str[0:n] + str[n+1:len(str)] #len(str) includes everything to the end, or -1

print(missing_char('kitten', 1)) # →'ktten'	
print(missing_char('kitten', 0)) # →'itten'	
print(missing_char('kitten', 4)) # →'kittn'	
print(missing_char('Hi', 0)) # →'i'	
print(missing_char('Hi', 1)) # →'H'	
print(missing_char('code', 0)) # →'ode'	
print(missing_char('code', 1)) # →'cde'	
print(missing_char('code', 2)) # →'coe'	
print(missing_char('code', 3)) # →'cod'	
print(missing_char('chocolate', 8)) # →'chocolat'