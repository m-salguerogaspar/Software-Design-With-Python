#!/usr/bin/env python
# coding: utf-8

# In[1]:


from time import perf_counter
from operator import itemgetter
from tabulate import tabulate
import contextlib
import io
import inspect

ExeTimeDic = dict()

class decorator3: 
        
     def __init__(self,func):
        self.func = func
        self.count = 0
    
     
     def __call__(self,*args,**kwargs):
        
        self.count+= 1
        with contextlib.redirect_stdout(io.StringIO()) as fun:
            self.start = perf_counter()
            self.func(*args, **kwargs)
            self.end = perf_counter()
            self.time = self.end-self.start
        self.out = fun.getvalue()
        global ExeTimeDic
        ExeTimeDic[self.func.__name__] = self.time

        if len(ExeTimeDic.keys()) == 4:
           s_f = sorted(ExeTimeDic.values())
           reverse = dict((v,k) for k,v in ExeTimeDic.items())
           table = [[reverse[s_f[0]],1,s_f[0]],[reverse[s_f[1]],2,s_f[1]],[reverse[s_f[2]],3,s_f[2]],[reverse[s_f[3]],4,s_f[3]]]
           print(tabulate(table, headers=["PROGRAM","RANK","TIME ELAPSED"]))
        else:
           pass
        
        file= open(self.func.__name__ + ".txt","w+")
        file.write( f'{self.func.__name__} has been called {self.count} times and the execution time was {self.time} \nDESCRIPTION:\nName :{self.func.__name__} \nType: {type(self.func)} \nSign:{inspect.signature(self.func)} \nArgs: positional {args} \nkey=worded {kwargs} \nDoc :{self.func.__doc__} \nSource:{inspect.getsource(self.func)} \nOutput:{self.out}') 


# In[2]:


from time import perf_counter
from operator import itemgetter
from tabulate import tabulate
import contextlib
import io
import inspect

ExeTimeDic = dict()                             

def decorator_3(func):                             
    
    counter = 0
    
    def inner_func(*args,**kwargs):  
                
        nonlocal counter
        counter += 1
        with contextlib.redirect_stdout(io.StringIO()) as fun:
            start = perf_counter()
            func(*args,**kwargs)
            end = perf_counter()
            time = end-start
        out = fun.getvalue()
        
        global ExeTimeDic
        ExeTimeDic[func.__name__] = time

        if len(ExeTimeDic.keys()) == 4:
           s_f = sorted(ExeTimeDic.values())
           reverse = dict((v,k) for k,v in ExeTimeDic.items())
           table = [[reverse[s_f[0]],1,s_f[0]],[reverse[s_f[1]],2,s_f[1]],[reverse[s_f[2]],3,s_f[2]],[reverse[s_f[3]],4,s_f[3]]]
           print(tabulate(table, headers=["PROGRAM","RANK","TIME ELAPSED"]))
        else:
           pass
        
        file= open(func.__name__ + ".txt","w+")
        file.write( f'{func.__name__} has been called {counter} times and the execution time was {time} \nDESCRIPTION:\nName :{func.__name__} \nType: {type(func)} \nSign:{inspect.signature(func)} \nArgs: positional {args} \nkey=worded {kwargs} \nDoc :{func.__doc__} \nSource:{inspect.getsource(func)} \nOutput:{out}') 
                
    return inner_func

