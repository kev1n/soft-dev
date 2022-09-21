def near_hundred(n):
  #one liner
  return (abs(100-n) <= 10) or (abs(200-n) <= 10)

print(near_hundred(93)) #→ True	
print(near_hundred(90)) #→ True	
print(near_hundred(89)) #→ False	
print(near_hundred(110)) #→ True	
print(near_hundred(111)) #→ False	
print(near_hundred(121)) #→ False	
print(near_hundred(-101)) #→ False	
print(near_hundred(-209)) #→ False	
print(near_hundred(190)) #→ True	
print(near_hundred(209)) #→ True	
print(near_hundred(0)) #→ False	
print(near_hundred(5)) #→ False	
print(near_hundred(-50)) #→ False	
print(near_hundred(191)) #→ True	
print(near_hundred(189)) #→ False	
print(near_hundred(200)) #→ True	
print(near_hundred(210)) #→ True	
print(near_hundred(211)) #→ False	
print(near_hundred(290)) #→ False