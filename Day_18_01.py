#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 18:32:01 2020
Polymorphism is the ability of an object to adapt the code to the type of the data it is processing.Here poly means many and morphi means forms.In Python polymorphism is one of the key concepts and we can say that it is a built-in feature. polymorphism helps us to describe an action regardless of the type of objects.

For example  When you describe how to move an object by pushing it, you may explain it using a box, but you expect the person you are addressing to be able to repeat the action even if you need to move a pen, or a book, or a bottle.
@author: venky
"""

class dog:
    def sound(self):
        print('bow bow')
        
        
class cat:
    def sound(self):
        print("meow")

#common interface
def makesound(animaltype):
    animaltype.sound()



#instance objects
catobj = cat()
dogobj = dog()
#passing objects
makesound(catobj)
makesound(dogobj)        