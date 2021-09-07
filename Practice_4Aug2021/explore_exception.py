
a = 10
b = 5
print("prog starts")

try:
   result = a/b
   print(result)
   no = int(input("enter number "))
   print(no)

except Exception as e: #this covers all types of errors, there is no need for separate ZeroDivion, ValueError
   print("error:",e)

except ZeroDivisionError as v:
    print(v)

except ValueError as v:
    print(v)
finally:
    print("last line, ends")