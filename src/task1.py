#!/usr/bin/env python
# coding: utf-8

# In[1]:


def decorator_1(func):                             # Using Decorators to show the running time
    
    from time import perf_counter
    counter = 0
    
    def inner_func(*args,**kwargs):  
        
        nonlocal counter
        counter += 1
        start = perf_counter()
        func(*args,**kwargs)
        end = perf_counter()
        print(f'The Function {func.__name__} has been called {counter} times and the execution time was {end-start}')
           
    return inner_func

