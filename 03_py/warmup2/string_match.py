def string_match(a, b):
  counter = 0
  length = 0
  short = ""
  long = ""
  #find out which is the short string and which is the long one
  if len(a) > len(b):
    length = len(b)
    short = b
    long = a
  else:
    length = len(a)
    short = a
    long = b

  if length < 2:
    return 0
  for i in range(length - 1):
    if short[i:i+2] == long[i:i+2]: #can safely do comparisions now
      counter+=1
  return counter

print(string_match('xxcaazz', 'xxbaaz'))# → 3		
print(string_match('abc', 'abc'))# → 2		
print(string_match('abc', 'axc'))# → 0		
print(string_match('hello', 'he'))# → 1		
print(string_match('he', 'hello'))# → 1		
print(string_match('h', 'hello'))# → 0		
print(string_match('', 'hello'))# → 0		
print(string_match('aabbccdd', 'abbbxxd'))# → 1		
print(string_match('aaxxaaxx', 'iaxxai'))# → 3		
print(string_match('iaxxai', 'aaxxaaxx'))# → 3