def add(a):
  c = list(a)
  for i in range(1, len(c) * 2, 2):
    c.insert(i, 'E')
  return c

def prnt(st):
  for i in st:
    print(i, end = "")

a = 'rfr'.upper()
st = add(a)
prnt(st)
print('NCE')