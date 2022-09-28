#!/usr/bin/env python
# coding: utf-8

# # PYTHON BASICS – EXERCISE 

# 1. Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included). The numbers obtained should be printed in a comma-separated sequence on a single line. 
# Hints: Consider use range(#begin, #end) method 
# 

# In[19]:


for i in range(2000,3200,1):
    if i % 7 == 0 and i % 5 != 0:
        print (i, end = ",")
        


# In[ ]:





# 2. Write a program which can compute the factorial of a given numbers. The results should be printed in a comma-separated sequence on a single line. 
# Suppose the input is supplied to the program: 8 
# Then, the output should be: 40320 
# Hints: In case of input data being supplied to the question, it should be assumed to be a console input. 
# 

# In[38]:


num_for_factorial = int(input("enter the number : ", ))
f = 1
for i in range(1,num_for_factorial+1,1):
    f *= i    
print(f)


# In[ ]:





# 3. With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included) and then the program should print the dictionary. 
# Suppose the input is supplied to the program: 8 
# Then, the output should be: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64} 
# Hints: In case of input data being supplied to the question, it should be assumed to be a console input. Consider use dict() 
# 

# In[50]:


a = 5
b = {i :i*i for i in range(1,a+1,1)}
print(b)


# In[52]:


user_input = int(input('Please enter a integer :' ,))
dec = {}
for i in range(1, user_input + 1):
    dec[i] = i * i
print(dec)


# In[ ]:





# 4. Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number. 
# Suppose the input is supplied to the program: 34, 67, 55, 33, 12, 98 
# Then, the output should be: 
# ['34', '67', '55', '33', '12', '98'] 
# ('34', '67', '55', '33', '12', '98') 
# Hints: In case of input data being supplied to the question, it should be assumed to be a console input. tuple() method can convert list to tuple 
# 

# In[57]:


user_input = input("enter list : ", ).split(",")
print(user_input)

# converting list into tuple

T1 = tuple(user_input)
print(T1)


# In[59]:


user_input = list(map(str , input("enter list : ", ).split(",")))
print(user_input)

# converting list into tuple

T1 = tuple(user_input)
print(T1)


# In[ ]:





# 5. Define a class which has at least two methods: 
# getString: to get a string from console input 
# printString: to print the string in upper case. 
# Also please include simple test function to test the class methods. 
# Hints: Use __init__ method to construct some parameters 
# 

# In[92]:


class person:
    def __init__(self,a = 'I am bharat'):
        self.a = a
        print(self.a)
    def get_string(self):    
        #self.argu = argu
    #def print_string(self):
        print(self.a.upper())
        
            
a = person("tarun")        
a.get_string()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




