#!/usr/bin/env python
# coding: utf-8

# In[1]:


from time import perf_counter
from operator import itemgetter
from tabulate import tabulate
import contextlib
import io
import inspect


# In[2]:


from task1 import decorator_1
from task2 import decorator_2
from task3 import decorator_3
from task4 import decorator_4


# In[3]:


@decorator_4
@decorator_3
#@decorator_2
#@decorator_1
def quadratic_equation_solver(a,b,c):
    '''
    Solve a general quadratic equation.
    
    param a: Squared Coefficient of x squared
    param b: Linear Coefficient of x
    param c: Constant term
    '''
    
    from math import sqrt
    discriminante = b**2 - 4*(a*c)
    if discriminante > 0:
       print(f'Solutions are {-b/(2*a) + sqrt(discriminante)/(2*a)} and {-b/(2*a) - sqrt(discriminante)/(2*a)}')
    elif discriminante < 0:
       print(f'Solutions are {-b/(2*a)} + {sqrt(abs(discriminante))/(2*a)} i and {-b/(2*a)} - {sqrt(abs(discriminante))/(2*a)} i')
    else:
       print(f'Just one solution {-b/(2*a)}')


# In[4]:


@decorator_4
@decorator_3
#@decorator_2
#@decorator_1
def Fibonacci(number):
    '''
    Find the n Fibonacci number.
    
    param n: n-th Fibonacci number
    '''
    values = [0, 1]
  
    any(map(lambda _: values.append(sum(values[-2:])),range(2, number)))
  
    print(values[-1])


# In[5]:


@decorator_4
@decorator_3
#@decorator_2
#@decorator_1
def Is_prime(n):
    '''
    Find a list of the prime numbers below  n.
    
    param n: Upper boundary to find the prime numbers below.
    '''
    nums = list()
    if n == 1:
       print("No primes")
    else:
       nums = range(2,n+1)
       for i in range(2, n+1):
           nums = list(filter(lambda x: x == i or x % i, nums))
       print(nums)


# In[6]:


@decorator_4
@decorator_3
#@decorator_2
#@decorator_1
def Pascal_Triangle(n):
    '''
    Find the n-th row of the Pascal Triangle as a list.
    
    param n: n-th row of the Pascal Triangle.
    '''
    update = [1]
    y = [0]
    for x in range(n-1):
        update=[left+right for left,right in zip(update+y, y+update)]
    print(update)


# In[7]:


quadratic_equation_solver(1,1,1)


# In[8]:


Pascal_Triangle(2)


# In[9]:


Is_prime(19)


# In[11]:


Fibonacci("number")


# In[12]:


Fibonacci(4)


# In[ ]:




