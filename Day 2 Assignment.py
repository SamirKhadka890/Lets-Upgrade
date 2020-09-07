#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Strings


# In[2]:


ram = "this is string"
print(ram.title())


# In[3]:


print(ram.upper())


# In[4]:


print(ram.lower())


# In[6]:


first_name = "Samir"
last_name = "Khadka"
print(first_name+" "+last_name)


# In[7]:


print(first_name+" "+last_name.lstrip())


# In[8]:


#list


# In[15]:


alphabets = ['a','b','c','d','e','f','g','h']
print(alphabets)


# In[16]:


print(alphabets[0:3])


# In[17]:


alphabets[2] = 's'
print(alphabets)


# In[18]:


alphabets.append('i')
print(alphabets)


# In[24]:


del alphabets[0]
alphabets


# In[26]:


alphabets.pop()
alphabets


# In[27]:


alphabets.sort()
alphabets


# In[29]:


#Sets


# In[62]:


st = {"Samir","Shirjan",1,2,3,5,'a'}
st


# In[63]:


type(st)


# In[64]:


st.add(4)
st


# In[65]:


st1={4, 5, 'Samir'}
st1.issubset(st)


# In[66]:


st1.isdisjoint(st)


# In[67]:


st


# In[72]:


st.clear()


# In[73]:


#Tuple


# In[74]:


tup=('Samir','@',1,'Microsoft')
tup


# In[75]:


tup.count('@')


# In[76]:


tup.index(1)


# In[77]:


#Dictonary


# In[78]:


user ={'name':'Samir Khadka','age':'21','number':'37387565228','email':'samidsvs@gmail.com'}
user


# In[82]:


user.items()


# In[83]:


user.keys()


# In[84]:


user.values()


# In[85]:


user['name']


# In[87]:


user.pop("name")


# In[88]:


user


# In[90]:


user["school"]="Sunshine"
user


# In[93]:


type(user)


# In[ ]:




