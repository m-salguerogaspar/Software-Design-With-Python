#!/usr/bin/env python
# coding: utf-8

# In[1]:


def decorator_2(func):                             # Using Decorators to show the running time
    
    from time import perf_counter
    import inspect
    import contextlib
    import io
    counter = 0
    
    def inner_func(*args,**kwargs):  
                
        nonlocal counter
        counter += 1
        with contextlib.redirect_stdout(io.StringIO()) as fun:
            start = perf_counter()
            func(*args,**kwargs)
            end = perf_counter()
        out = fun.getvalue()
                
        print(f'{func.__name__} has been called {counter} times and the execution time was {end-start} \nDESCRIPTION:\nName :{func.__name__} \nType:{type(func)} \nSign:{inspect.signature(func)} \nArgs: positional {args} \nkey=worded {kwargs} \nDoc :{func.__doc__} \nSource:{inspect.getsource(func)} \nOutput:{out}')
           
    return inner_func

