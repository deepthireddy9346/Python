#!/usr/bin/env python
# coding: utf-8

# # variables and literals

# In[23]:


x = 5 # int literal
x = 'hi' # string  literal


# In[2]:


x = 5
print(id(x),x)
x = 'hi'
print(id(x),x)
x = True
print(id(x),x)


# In[3]:


id('hi')


# In[4]:


#print = 5 #uncomment to see the errorlol
#print('hello') #uncomment to see the error


# In[5]:


import keyword
from keyword import kwlist
print(kwlist)


# In[6]:


print(kwlist)


# In[7]:


len(kwlist)


# In[8]:


x=2
y=4
print(x)
y


# In[9]:


a,b,c = 10,20,30
print(a,b,sep='*',end= '5')
print(c)


# In[10]:


x = "hi"
y = "good morning"
z = "everyone"
print(x,y,z)


# # arithematic operators

# x=2
# y=3
# x^y

# In[11]:


x,y =(5,6)
print(x+y) # addition
print(x-y) # subraction
print(x*y) # multiplication
print(x/y) # division
print(x**y) # exponent
print(x%y) #modulas
print(x//y) #floor division


# In[12]:


5//3


# # comparision operators

# In[13]:


x,y = 10,15
print(x==y) #equal to
print(x!=y) # not equal to
print(x<y) #lessthan
print(x>y) # greater than
print(x<=y) #less than or equal to
print(x>=y) #greater than or equal to


# In[14]:


x,y = 'hi','hello'
print(x==y)


# # identity operators

# In[15]:


a ='hi'
b ='hi'
c =[1,2,3]
d =[1,2,3]
print(a==b)
print(c==d)
print(a is b)
print(c is d)
print(id(c),id(d))
print(id(a),id(b))
print(a is not b)
print(c is not d)


# # logical operators
# and
# or
# not

# In[16]:


a="its raining today"
b="im not sick today"
print(a>b and a<b)
print(a<b and a>b)
print(a>b or a<b)
print(a>b!=a<b)


# # membership operator

# In[17]:


'1' in '123'


# In[18]:


print(1 not in [1,2,3])
print(1 in [1,2,3])


# # bitwise operators

# In[19]:


print(5&7) #bitwise and
print(5|7) #bitwise or
print(5^7) #bitwise xor
print(~7) #bitwise not
print(~-1) #bitwise not


# ## left shift

# In[20]:


print(3<<2) #left shift


# ## right shift

# In[21]:


print(3>>2)


# # assignment operators
# *var opr = value
# 
# *arith = value

# In[22]:


a = 2
a<<=2
print(a)
#print(a=a+2)
#a+=2
#print(a)

