def not_string(str):
  firstthree = str[0:3] #subindexing
  if not firstthree == "not":
    return "not " + str
  else:
    return str

print(not_string('candy')) # → 'not candy'	
print(not_string('x')) # → 'not x'	
print(not_string('not bad')) # → 'not bad'	
print(not_string('bad')) # → 'not bad'	
print(not_string('not')) # → 'not'	
print(not_string('is not')) # → 'not is not'	
print(not_string('no')) # → 'not no'