#!/usr/bin/env python
# coding: utf-8

# In[122]:


import random
print("Random Password Generator")
#function to generate the random password
def passgen(n,U,L,N):
    c=''
    cc=''
    for i in range(n):
        if n1.upper()=="Y":
            c+=random.choice(U)
        if n2.upper()=="Y":
            c+=random.choice(L)
        if n3.upper()=="Y":
            c+=random.choice(N)
    for i in range(n):
        cc+=random.choice(c)
    return cc

#takes input length for password
n=int(input("Choose The Length Of The Password"))
if n>=5:
    n1=input(r"Want to Include Uppercase characters ?\n(Y/N)")
    n2=input(r"Want to Include Lowercase characters ?\n(Y\N)")
    n3=input(r"Want to Include digits ?\n(Y\N)")
else:
    print("Password length should be greater than 5")
    
    
# list comprehensions for alphabets, digits and special chars
U=[("%c"%i) for i in range(65,91)]
L=[("%c"%i) for i in range(97,123)]
N=[str(x) for x in range(0,10)]

#checking to meet aleast one character type requirement
if n1.upper()=='N' and n2.upper()=="N" and n3.upper()=="N":
    print("Select atleast one character type")
else:
    print(passgen(n,U,L,N))

