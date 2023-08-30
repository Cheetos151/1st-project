print('for adding press 1,for subtracting press 2')
print('for multiplication press 3,for divison press 4,\nfor powers press 5,for square root press 6,\nfor factorial press 7.')      
def fact(n):
   if n==0 or n==1:
      return 1
   else:
      return n*fact(n-1)     

keep_going='y'
while(keep_going=='y'):
 x=int(input('choose a function:'))
 if(x==1):
    a=eval(input('put a no.:'))
    b=eval(input('put a no.:'))
    p=a+b
    print('the result is:',p)
 elif(x==2):
    a=eval(input('put a no.:'))
    b=eval(input('put a no.:'))
    m=a-b
    print('the result is:',m)
 elif(x==3):
    a=eval(input('put a no.:'))
    b=eval(input('put a no.:'))
    g=a*b
    print('the result is:',g)
 elif(x==4):
    a=eval(input('put a no.:'))
    b=eval(input('put a no.:'))
    d=a/b
    print('the result is:',d)
 elif(x==5):
   a=eval(input('put a no:'))
   b=eval(input('put a power:'))
   d=a**b
   print('the result is :',d)
 elif(x==6):
   a=eval(input('put a no:'))
   b=a**0.5
   print('the root is:',b)     
 elif(x==7):
   a=eval(input('enter a no.:'))
   print(fact(a))



