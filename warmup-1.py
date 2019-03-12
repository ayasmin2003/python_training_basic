def monkey_trouble(a_smile, b_smile):
    return (a_smile and b_smile) or (not a_smile or not b_smile)
print(monkey_trouble(True, True))
print(monkey_trouble(False, False))
print(monkey_trouble(True, False))

def sum_double(a, b):
    return a+b if a !=b else (a+b) *2
print (sum_double(3,3))

def diff21(n):
  if n <=21:
   return (21-n)
  else:
   return (n-21) * 2
print (diff21(20))
print (diff21(23))
# print (diff21(25))

#def parrot_trouble(talking, hour):
#return talking and not (7 =< hour <= 20)

def makes10(a,b):
    return a == 10 or b == 10 or (a+b) == 10
print (makes10(9, 10))


def pos_neg(a, b, negative):
    if negative:
        return (a<0 and b<0)
    else:
     return not (a <0 and b>0) or (a>0 or b<0)
print (pos_neg(1, -1, False))
print (pos_neg(-1, 1, False))
print (pos_neg(-4, -5, True))

def missing_char(str, n):
  phase1 = str[:n]
  phase2 = str[(n+1):]

  return (phase1 + phase2)
print(missing_char('kitten', 1) )
print(missing_char('kitten', 0))
print(missing_char('kitten', 4))

'''Given a string, we'll say that the front is the first 3 chars of the string. 
If the string length is less than 3, the front is whatever is there. 
Return a new string which is 3 copies of the front.'''


