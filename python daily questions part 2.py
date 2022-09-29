#!/usr/bin/env python
# coding: utf-8

# # # PYTHON BASICS – EXERCISE 

# 6. Write a program that calculates and prints the value according to the given formula: 
# Q = Square root of [(2 * C * D)/H] 
# Following are the fixed values of C and H: C is 50. H is 30. 
# D is the variable whose values should be input to your program in a comma-separated sequence. 
# Let us assume the following comma separated input sequence is given to the program: 100,150,180 
# The output of the program should be: 18, 22, 24 
# Hints: If the output received is in decimal form, it should be rounded off to its nearest value (for example, if the output received is 26.0, it should be printed as 26) 
# In case of input data being supplied to the question, it should be assumed to be a console input.
# 
# 

# In[6]:


import numpy as np
import math as mt


# In[18]:


d = list(map(int,input("enter the number :",).split(",")))
c = 50
h = 30 

for i in d:
    
    Q = mt.sqrt((2*c*i)/h)

    print(round(Q) , end = ",")


# In[ ]:





# 7. Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically. 
# Suppose the input is supplied to the program: without, hello, bag, world 
# Then, the output should be: bag, hello, without, world 
# Hints: In case of input data being supplied to the question, it should be assumed to be a console input. 
#  
# 

# In[75]:


a =input("enter words here : ", ).split(",") 

a.sort()
for i in a:
    if i == a[-1]:
        print(i, end = "")
    else:
        print(i , end = ",")


# In[ ]:





# 8. Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
# 
# Suppose the input is supplied to the program: Hello world 
# Practice makes perfect 
# Then, the output should be: HELLO WORLD 
# PRACTICE MAKES PERFECT 
# Hints: In case of input data being supplied to the question, it should be assumed to be a console input. 
# 
# 

# In[81]:


a =input("enter words here : ", ) 

print(a.upper())


# In[ ]:





# 9. Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically. 
# Suppose the input is supplied to the program: hello world and practice makes perfect and hello world again 
# Then, the output should be: again and hello makes perfect practice world 
# Hints: In case of input data being supplied to the question, it should be assumed to be a console input. We use set container to remove duplicated data automatically and then use sorted() to sort the data. 
# 

# In[94]:


a =set(input("enter words here : ", ).split(" ")) 

a = list(a)
a.sort()
for i in a:
    print(i , end = " ")

    


# In[ ]:





# 10. Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence. 
# Suppose the input is supplied to the program: 0100,0011,1010,1001 
# Then the output should be: 1010 
# Notes: Assume the data is input by console. 
# Hints: In case of input data being supplied to the question, it should be assumed to be a console input. 
# 

# In[107]:


a = list(map(int,input("enter 4 digit binary (0,1) numbers only :",).split(",")))


for i in a:
    if i%5 == 0 :
        print(i)
    else:
        pass


# In[ ]:




