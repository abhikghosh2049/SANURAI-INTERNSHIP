def addi(x,y):
    print("addition",x+y)
def subs(x,y):
    print("substraction",x-y)
def multi(x,y):
    print("multiplication :",x*y)
def divi(x,y):
    if y==0:
     print("error")
    else:
       print("divison:",x/y)

print(" press 1 for addition")
print(" press 2 for substraction")
print(" press 3 for multiplication")
print(" press 4 for division")
ch=int(input("enter your choice:"))
a= float(input(" enter the first number:"))
b= float(input("enter the second number:"))
if ch==1:
 addi(a,b)
elif ch==2:
 subs(a,b)
elif ch==3:
  multi(a,b)
elif ch==4:
 divi(a,b)
else:
  print("invalid choice!!!")

         
         
  



