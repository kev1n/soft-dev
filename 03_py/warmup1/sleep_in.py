def sleep_in(weekday, vacation):
  #We feel like it could be one conditional but we can't seem to figure it out
  if weekday and vacation:
    return True
  elif weekday and not vacation:
    return False
  elif not weekday and vacation:
    return True
  else:
    return True

print(sleep_in(False, False)) #→ True		
print(sleep_in(True, False)) #→ False	
print(sleep_in(False, True)) #→ True	
print(sleep_in(True, True)) #→ True	