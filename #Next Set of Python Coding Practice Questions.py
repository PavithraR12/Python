#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Next Set of Python Coding Practice Questions


# In[11]:


#1. Write a Python program to check if a year is a leap year.
yr = int(input())
if yr%4==0:
    print("leap")
else:
    print("nope")


# In[20]:


#2. Write a Python function to count vowels in a string.
def vowels(string):
    count=0
    vow = "aeiouAEIOU"
    for i in string:
        if i in vow:
            count+=1
        else:
            continue
    print(count)
vowels("rajalakshmi")


# In[26]:


#3. Write a Python program to merge two lists and remove duplicates.
lst1 = list(map(int,input().split()))
lst2 = list(map(int,input().split()))
emp =[]
for i in lst2:
    lst1.append(i)
print(lst1)
print(set(lst1))


# In[36]:


#4. Write a Python program to sort a list of tuples by the second element.
tup = [(1,2),(4,5),(0,2)]
print(sorted(tup,key=lambda x:x[1]))  


# In[51]:


#5. Write a Python program to find the GCD (Greatest Common Divisor) of two numbers.
num1 = int(input())
num2 = int(input())
for i in range(1,1000):
    if num1%i==0 and num2%i==0:
        s = i
print(s)


# In[5]:


# 6. Write a Python function to flatten a nested list.
data =[1,[2,[3,4],5],6]
def flatten(data):
    emp=[]
    for i in data:
        if isinstance(i,list):
            emp.extend(flatten(i))
        else:
                emp.append(i)
    return emp
flatten(data)


# In[6]:


#7. Write a Python program to find all the unique elements in a list
lst = list(map(int,input().split()))
emp1 =[]
for i in lst:
    if i not in emp1:
        emp1.append(i)
    else:
        continue
print(emp1)
        


# In[25]:


#8. Write a Python function to check if a list is a palindrome.
lst1 = list(map(int,input().split()))
def pali(lst1):
    rev=[]
    for i in reversed(lst1):
        rev.append(i)
    rev    
    if lst1==rev:
        print("Palindrome")
    else:
        print("nope")
pali(lst1)


# In[38]:


#9. Write a Python program to read a file and count the number of lines.
with open("Basic Level.txt","r") as file:
    count=0
    for line in file:
        count+=1
print(count)


# In[46]:


#10. Write a Python program to implement a simple calculator (add, subtract, multiply, divide).
n1 = int(input())
n2 = int(input())
choice = input()

if choice=='+':
    print(n1+n2)
elif choice=='-':
    print(n1-n2)
elif choice=='*':
    print(n1*n2)
elif choice=='/':
    print(n1/n2)
else:
    print("ERROR")


# In[ ]:




