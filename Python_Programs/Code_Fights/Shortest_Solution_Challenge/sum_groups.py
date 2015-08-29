def SumGroups(a):
  l = 1
  for x in a[1:]:
    x %= 2
    l += (a[0] + l + ~x) % 2 * -~x - x
  
  return l
# Note: Not my solution, just a clever one I saw and wanted to remember.
