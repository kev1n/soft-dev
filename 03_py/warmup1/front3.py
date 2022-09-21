def front3(str):
  if len(str) < 3:
    return str*3 #multiply the string
  return str[0:3]*3
	
print(front3('Java')) # → 'JavJavJav'	
print(front3('Chocolate')) # → 'ChoChoCho'	
print(front3('abc')) # → 'abcabcabc'	
print(front3('abcXYZ')) # → 'abcabcabc'	
print(front3('ab')) # → 'ababab'	
print(front3('a')) # → 'aaa'	
print(front3('')) # → ''