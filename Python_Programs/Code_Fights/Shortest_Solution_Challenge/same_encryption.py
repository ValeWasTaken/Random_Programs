'''
Same Encryption challenge in Python 3.4
Required code: 
      def SameEncryption(FirstString, SecondString):
Goal: 
    Take the first and the last letters of the word;
    Replace the letters between them with their number;
    Replace this number with the sum of it digits until a single digit is obtained.
    Determine if two strings share the same encryption answer.
Example:
  >> "EbnhGfjklmjhgz"
  >> E12z
  >> E3z
Solve with as few characters as possible.
Characters used in solution: 209
'''
def SameEncryption(FirstString, SecondString):
    a = []
    for s in [FirstString, SecondString]:
        n = len(s) - 2
        f = s[:1]
        l = s[-1:]
        n = sum(int(x) for x in str(n)[::])
        a.append('{0}{1}{2}'.format(f,n,l))
    print(a)
    if a[0] == a[1]:
        return 'YES'
    else:
        return 'NO'
