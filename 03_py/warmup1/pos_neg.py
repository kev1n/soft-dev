def pos_neg(a, b, negative):
  if (not negative): #english to code
    return (a < 0 and b > 0) or (a > 0 and b < 0)
  else:
    return a < 0 and b < 0

print(pos_neg(1, -1, False)) # → True	
print(pos_neg(-1, 1, False)) # → True	
print(pos_neg(-4, -5, True)) # → True	
print(pos_neg(-4, -5, False)) # → False	
print(pos_neg(-4, 5, False)) # → True	
print(pos_neg(-4, 5, True)) # → False	
print(pos_neg(1, 1, False)) # → False	
print(pos_neg(-1, -1, False)) # → False	
print(pos_neg(1, -1, True)) # → False	
print(pos_neg(-1, 1, True)) # → False	
print(pos_neg(1, 1, True)) # → False	
print(pos_neg(-1, -1, True)) # → True	
print(pos_neg(5, -5, False)) # → True	
print(pos_neg(-6, 6, False)) # → True	
print(pos_neg(-5, -6, False)) # → False	
print(pos_neg(-2, -1, False)) # → False	
print(pos_neg(1, 2, False)) # → False	
print(pos_neg(-5, 6, True)) # → False	
print(pos_neg(-5, -5, True)) # → True