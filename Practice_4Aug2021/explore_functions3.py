# functions returning other functions
#return functions from other functions

def create_adder(x):
    def adder(y):
        print(y)
        return x+y
    return adder

add_15 = create_adder(15)

print(add_15(10))


