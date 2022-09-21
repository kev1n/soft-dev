def string_bits(str):
  answer = ""
  counter = 0
  for c in str:
    if counter%2 == 0: #even check
      answer+=c
    counter+=1
  return answer

print(string_bits('Hello')) #→ 'Hlo'
print(string_bits('Hi')) #→ 'H'
print(string_bits('Heeololeo')) #→ 'Hello'
print(string_bits('HiHiHi')) #→ 'HHH'
print(string_bits('')) #→ ''
print(string_bits('Greetings')) #→ 'Getns'
print(string_bits('Chocoate')) #→ 'Coot'
print(string_bits('pi')) #→ 'p'
print(string_bits('Hello Kitten')) #→ 'HloKte'
print(string_bits('hxaxpxpxy')) #→ 'happy'