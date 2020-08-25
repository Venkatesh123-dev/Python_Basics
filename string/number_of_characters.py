"""Write a Python program to count the number of characters (character frequency) in a string. """

def char_frequency(str1):
    dict = {}
    for i in str1:
        keys = dict.keys()
        if i in keys:
            dict[i] += 1
        else:
            dict[i] = 1
    return dict
print(char_frequency('google.com'))






from collections import Counter


string = 'google'
counter = Counter(string)
print(counter)
