"""Python program to check if the given input string is a palindrome or not using a slice operator"""

#method1
myStr = input("enter a string")
if str(myStr) == str(myStr)[::-1]:
    print("Palindrome")
else:
  print("Not a Palindrome")





#method2
string = input("Please enter your own String : ")
str1 = ""

for i in string:
    str1 = i + str1  
print("String in reverse Order :  ", str1)

if(string == str1):
   print("This is a Palindrome String")
else:
   print("This is Not a Palindrome String")



"""Mom
Madam
Rubber
Dad
"""   
