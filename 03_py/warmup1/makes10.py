def makes10(a, b):
  #conditional block
  if a == 10 or b == 10:
    return True
  elif a+b == 10:
    return True
  else:
    return False

print(makes10(9, 10)) #→ True		
print(makes10(9, 9)) #→ False		
print(makes10(1, 9)) #→ True		
print(makes10(10, 1)) #→ True		
print(makes10(10, 10)) #→ True		
print(makes10(8, 2)) #→ True		
print(makes10(8, 3)) #→ False		
print(makes10(10, 42)) #→ True		
print(makes10(12, -2)) #→ True