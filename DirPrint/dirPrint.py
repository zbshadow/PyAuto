####
# Program: dirPrint
# Author: B. Bayless
# Last Updated: 03FEB20
# Purpose: Print all files in current Dir
# Useage: Used to print a directory of files, reguardless of type.Weekly I have to print many files manually that I will need for the week.
# Other Useage: Used to print files for many reasons. Tweak to what you need.
####

import os

#Gets the scripts current directory
#only works in editor, externally returns the directory of pythons enviroment :(

dirLocation = os.path.dirname(os.path.realpath(__file__))

#Getting the files in the directory of the script
dirFiles = os.listdir(dirLocation)

#Removing script from array
dirFiles.remove('dirPrint.py')
print(dirFiles)

for x in dirFiles:
    os.startfile("{}\\{}".format(dirLocation,x), "print")