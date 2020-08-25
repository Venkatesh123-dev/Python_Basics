"""Reverse a String in Python"""


#method1
def reverse(s):
  str = ""
  for i in s:
    str = i + str
  return str

print(reverse('venky'))




#method2
def reverse(string):
    string = string[::-1]
    return string

print(reverse('hello'))

#method3
def reverse(string):
    string = "".join(reversed(string))
    return string

print(reverse('hello'))

