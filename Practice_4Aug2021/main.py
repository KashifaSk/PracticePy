# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import requests
import datetime
import random
import os

file_obj = open("abc.txt","w")
file_obj.write("Hi")
file_obj.close()
file_obj = open("abc.txt","w")
list = ["Hello ", "Hi ", "Bye ","Shaey "]
file_obj.writelines(list)
file_obj.close()

file_obj = open("abc.txt","r")
print(file_obj.read())
file_obj.close()


