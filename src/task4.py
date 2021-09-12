#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def decorator_4(func):                             
    
    def inner_func(*args,**kwargs):  
        import time
        import logging
        
        try:
            eval(func(*args,**kwargs))
 
        except Exception as error:
            logging.basicConfig(filename= "Errors.log" ,format='%(asctime)s %(message)s',filemode='w')
            logger=logging.getLogger()
            logger.setLevel(logging.DEBUG)
            logger.warning(f'{error} in {func.__name__} Function')

    return inner_func


# '''
# import time
# import logging
# 
#     
# class decorator_4_class: 
#        
#     def __init__(self,func):
#         self.func = func
# 
#     
#      
#     def __call__(self,*args,**kwargs):
#         
#         try:
#             self.func(*args, **kwargs)
#  
#         except Exception as error:
# 
#             logger=logging.getLogger()
#             logger.setLevel(logging.DEBUG)
#             logger.warning(f'{error} in {self.func.__name__} Function') 
# '''  
