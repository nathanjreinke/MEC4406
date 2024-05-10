# File: Introduction.py
# Author: Nathan Reinke
# Date: 10 May 2024
#
# A short program to satisfy the requirements of the warm-up exercise for MEC4406

# Write in python that prints your name, and then counts up to your favourite number squared.

name = "Nathan Reinke"
print (name)

fav_num = 17
for i in range (0,fav_num*fav_num):
    i = i+1
    print (i)


# Update the code to contain a class Engineers, with a fixed class attribute skill equal to "problem solver", and initial 
# attributes name, type and years of experience. Create two different engineers (objects) and print out their attributes.

# Creates class called Engineers and initialises attributes 
class Engineers:
    def __init__(self,name,type,years_of_experience):
        self.name = name
        self.type = type
        self.experience = years_of_experience
        self.skill = "Problem Solver"
    
    # Creates methods to return attributes
    def getName(self):
        return self.name
    
    def getType(self):
        return self.type
    
    def getExp(self):
        return self.experience
    
    def getSkill(self):
        return self.skill

# Creates two engineer objects and assigns attributes
engineer1 = Engineers("Nathan","Mechatronic",0)
engineer2 = Engineers("Henry","Mechanical",6)

# Calls methods individually to retrieve the objects attributes
print (engineer1.getName())
print (engineer1.getType())
print (engineer1.getExp())
print (engineer1.getSkill())

# Uses the vars function to teturn a list of the changeable attributes and their value for each object
print (vars(engineer1))
print (vars(engineer2))

# Also change your name to be the reverse. I.e. Jim becomes Mij

i=len(name)-1           # declares variable i to be the length of string "name" less 1 due to indexing starting from 0
reversename = ""        # declares variable reverse name as blank string 

# While loop that reverses the order of the "name" string by taking each indexed character from highest to lowest and concatenating the result
while i>=0:
    reversename = reversename + name[i]
    i=i-1
print (reversename)