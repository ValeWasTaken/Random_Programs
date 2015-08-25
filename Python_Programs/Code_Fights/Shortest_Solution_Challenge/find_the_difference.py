def compareSumOfDigits(N):
  e = 0
  o = 0
  for x in N[::]:
    x = int(x)
    if x % 2 == 0:
      e += x
    else:
      o += x
  return o - e
