#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Basic Python Coding Practice Questions


# In[2]:


#1. Write a Python program to check if a number is even or odd
num = int(input("Enter the num"))
if num%2==0:
    print("Even")
else:
    print("False")


# In[3]:


#2. Write a Python program to find the largest among three numbers.
num1 = int(input())
num2 = int(input())
num3=int(input())
if num1>num2 and num1>num3:
    print("num1 larger")
elif num2>num1 and num2>num3:
    print("num2 is larger")
else:
    print("num3 is larger")


# In[14]:


#3. Write a Python function to check if a string is a palindrome.
word = input()
rev = word[::-1]
if rev==word:
    print("Palindrome")
else:
    print("nope")


# In[16]:


#4. Write a Python program to calculate the factorial of a number using recursion.

#recursion means the function calls itself
def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)
fact(5)


# In[24]:


#6. Write a Python function to check if a number is prime.
num = int(input())
for i in range(2,n):
    if num%i==0:
         flag = False
    else:
        flag = True
if flag:
    print("prime")
else:
    print("not prime")


# In[33]:


#7. Write a Python program to find the sum of all elements in a list
lst = list(map(int,input().split()))
sum_=0
for i in lst:
    sum_ = sum_+i
print(sum_)


# In[34]:


lst = list(map(int,input().split()))
print(sum(lst))


# In[41]:


#8. Write a Python program to reverse a string without using slicing.
string = input()
print("".join(reversed(string)))


# In[44]:


#9. Write a Python program to count the frequency of each character in a string
a = input()
count = 0
for i in a:
    count+=1
print(count)


# In[46]:


#10. Write a Python program to find the second largest number in a list
lst1 = list(map(int,input().split()))
max1 = max(lst1)
lst1.remove(max1)
max2 = max(lst1)
print(max2)


# In[54]:


lst2 = list(map(int,input().split()))
max_=lst2[0]
for i in lst2:
        if max_<i:
            max_=i
        else:
            continue
lst2.remove(max_)
max_=lst2[0]
for j in lst2:
        if max_<j:
            max_=j
        else:
            continue
print(max_)


# In[ ]:




