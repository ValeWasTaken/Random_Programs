'''
Encryption challenge in Python 3.4
Required code: 
      def Encryption(Message, k):
Goal: "Encrypt" the message with a ceasar cipher.
Example:
  >> Encryption("Ab", 1) = "Bc"
  >> Encryption("z", 2) = "b"
Solve with as few characters as possible.
Characters used in solution: 116
'''

def Encryption(m, k):
    e = []
    a = []
    for c in m:
        e.append(ord(c))
    for x in e:
        x = int(x)
        x += k
        if x > 122:
            x -= 26
        a.append(chr(x))
    return ''.join(a)
