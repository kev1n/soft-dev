def diff21(n):
  if (n > 21):
    return (n-21)*2
  else:
    return 21-n

print(diff21(19)) #→ 2	
print(diff21(10)) #→ 11	
print(diff21(21)) #→ 0	
print(diff21(22)) #→ 2	
print(diff21(25)) #→ 8	
print(diff21(30)) #→ 18	
print(diff21(0))  #→ 21	
print(diff21(1)) #→ 20	
print(diff21(2)) #→ 19	
print(diff21(-1)) #→ 22	
print(diff21(-2)) #→ 23	
print(diff21(50)) #→ 58