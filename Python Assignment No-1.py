#!/usr/bin/env python
# coding: utf-8
# Exercise-1  Simple Message: Store a message in a variable, and then print that message.
# In[3]:


var="Lets start to data science study"

print(var)


# In[5]:


# Exercise-2 Store a message in a variable and print that message. 
Then change the value of your variable to a new message and print the new message.


# In[9]:


var1="Data science course"
print(var)

## Replace

var2=var1.replace("Data science course","Data science Bootcamp")
print(var2)


# In[11]:


# Exercise-3 Store a person’s name in a variable and print a message to that person. Your message should be simple, such as, 
“Hello Eric, would you like to learn some Python today?”


# In[13]:


var='sam'

print("Hello",var,"would you like to learn some Python today")


# In[ ]:


# Exercise-4&5 Find a quote from a famous person you admire. Print the quote and the name of its author. 
Your output should look something like the following, including the quotation marks:
Albert Einstein once said, “A person who never made a mistake never tried anything new.”
5. Repeat Exercise 4, but this time store the famous person’s name in a variable called famous_person. 
Then compose your message and store it in a new variable called message. Print your message.


# In[14]:


var='Elon Musk'

print("{} once said,The first step is to establish that something is possible then probability will occur".format(var))


# In[ ]:


# Exercise-6 Write addition, subtraction, multiplication, and division operations that each result in the number 8. 
Be sure to enclose your operations in print statements to see the results. You should create four lines that look like this: 
    print (5 + 3)
Your output should simply be four lines with the number 8 appearing once on each line


# In[15]:


print(5+3)
print(4*2)
print(16/2)
print(12-4)


# In[ ]:


# Exercise-7 Store your favourite number in a variable. Then, using that variable, 
create a message that reveals your favourite number.
Print that message.


# In[16]:


var='8'

print("My Favourite number is {}".format(var))


# In[ ]:


# Exercise-9 Store the names of a few of your friends in a list called names. 
Print each person’s name by accessing each element in the list, one at a time.


# In[17]:


List_Friends=['sam','Vaibhav','Ravi']

print(List_Friends[0])
print(List_Friends[1])
print(List_Friends[2])


# In[ ]:


# Exercise-10 Start with the list you used in Exercise 9, but instead of just printing each person’s name, 
print a message to them. The text of each message should be the same, but each message should be personalized with the person’s
name


# In[20]:


for message in List_Friends:
    print("My best friend is",message)


# In[ ]:


# Exercise-11 Think of your favourite mode of transportation, such as a motorcycle or a car,
and make a list that stores several examples. Use your list to print a series of statements about these items, 
such as “I would like to own a Honda motorcycle.”


# In[38]:


Fav_trans=["Motorcycle","Car","Train","Airoplane"]
print("I like to Night riding on "+Fav_trans[0])
print("Mostly i prefer " +Fav_trans[1]+ " in Rainy season")
print("I had goes to Tirupati by " +Fav_trans[2])
print("I will use " +Fav_trans[3]+ ' for travelling to abroad')

