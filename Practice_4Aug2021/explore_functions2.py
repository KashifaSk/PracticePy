# functions passed as arguments to other functions

def shout(text):
    return text.upper()

def whisper(text):
    return text.lower()

def greet(func):  #function assigned to func
    greeting = func("Hello World")
    print(greeting)

greet(shout)
greet(whisper)


def time(time):
    return time.upper()

def day(text):
    return text.lower()

def display(func):
    displaying = func("Hi Time and Date ")
    print(displaying)

display(time)
display(day)