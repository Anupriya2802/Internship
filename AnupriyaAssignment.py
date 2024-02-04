#!/usr/bin/env python
# coding: utf-8

# # ASSIGNMENT OF REGULAR EXPRESSION

# In[3]:


import regex as re


# In[4]:


Text = "python Exercise,PHP exercise."
print(re.sub("[, .]",".",Text))           QUESTION NUMBER - 1


# In[3]:


import pandas as pd                   QUESTION NUMBER -  2


# In[6]:


data = {'SUMMARY':["hello,world!","XXXX test","123four,five:;six..."]}
df=pd.DataFrame(data)


# In[11]:


df = df['SUMMARY'].str.replace('[^a-zA-Z\s]','', regex=True)      QUESTION NUMBER  - 3
print(df)


# In[13]:


import regex as re       QUESTION NUMBER - 3      


# In[16]:


Text = "Apj abdul kalam was an aerospace scientist also known as the miisileman of india"
pattern = re.compile(r'\b\w{4}\b')
matches = re.findall(pattern,Text)
print(matches)


# In[18]:


import regex as re    QUESTION NO-4    


# In[19]:


Text ="APJ abdul kalam was an aerospace scientist also known as the missileman of india"
pattern = re.compile(r'\b\w{3,5}\b')
matches = re.findall(pattern,Text)
print(matches)


# In[41]:


import regex as re            QUESTION NUMBER = 5


# In[19]:


items = ["example(.com)","hr@fliprobo(.com)","github(.com)","Hello(Data science world)","Data(scientist)"]
for item in items:
    Pattern = re.compile(r"?\([^])+\)"
        print( re.sub(pattern," ",item))
                                    
 


# In[18]:


import regex as re


# In[ ]:


sample text = 


# In[44]:


import regex as re      QUESTION NO-7


# In[45]:


Text = "ImportanceOfRegularExpressionPython"
matches = re.findall("[A-Z][^A-Z]*" , Text)
print(matches)


# In[87]:


import regex as re   QUESTION NO-8


# In[88]:


def insert_space(text):
    pattern = r'(d+)([A-Za-z]+)'                   question no-8
    result = re.sub(pattern,r'\1\2',text)
    return result


# In[89]:


text = "RegularExpression1IsAn2ImportantTopic3InPython"
output = insert_spaces(text)
print(output)


# In[76]:


import regex as re      QUESTION NUMBER =  9


# In[67]:


string="RegularExpression1IsAn2ImportantTopic3Inpython"      
words = re.findall("[A-Z][a-z]*",string)
print(' ' .join(words))


# In[92]:


import regex as re    question no -11


# In[ ]:


string = ("enter a string")
X = re.search("[^0-9a-Za-z_]+",text)
if x:
    print("found a match")
else:
    print("not matched")


# In[ ]:


import regex as re
my_string = input("enter a string")
my_number = input("enter a number")
m = re.match(my_number,my_string)
if m:                                      QUESTION NO =12
    print("its match")            
else:
    ("no match found")


# In[ ]:


import regex as re
my_IP = input("enter a string")
my_clean IP =re.sub('\.0*,'.',my_Ip)    question no 13
print(my_clean Ip)                    


# In[38]:


import regex as re                QUESTION NUMBER 14


# In[41]:


text = " On august 15th 1947  that India was declared independent from British colonialism,and the reins of control were handed over to the leaders of the country"
pattern = "([a-zA-Z]+) (\d+[a-z]+) (\d+)"
matches = re.search(pattern,text)
print(matches)                            


# In[101]:


string="The quick brown fox jumps over the lazy dog"
m=re.search("\dog\fox\horse",string)
if m:
    print("its match")               question no-15
else:
    print("no match")


# In[102]:


string=" The quick brown fox jumps over the lazy dog"
m=re.search("fox",string)
if m:
    print("its match")              question no - 16
else:
    print("no match")


# In[103]:


import regex as re


# In[107]:


string="python exercises,PHP exercises,c# exercises"
pattern="exercises"
x = re.findall(pattern,string)
if x:
    print("it\s a match",len(x))           question no-17
else:
    print("no match found")


# In[1]:


import regex as re         QUESTION NO = 18


# In[2]:


text = "python exercise,PHP exercise,c# exercise"
pattern = "exercise"
for match in re.finditer(pattern,text):
    s = match.start()
    e = match.end() 
    print('found "%s" at %d:%d' % (text[s:e],s,e))


# In[108]:


import regex as re


# In[109]:


date = "2018-03-31"         question no19
y=re.split("-",date)
new_date = "-".join(y[::-1])
print(new_date)


# In[110]:


import regex as re


# In[112]:


text= "01.12 0132.123 2.31875 145.8 3.01 27.25 0.25"
pattern = re.compile(r'\d+\.\d{1,2}')
x=re.findall(pattern,text)           question no -20
print(x)


# In[3]:


import regex as re          


# In[11]:


price = "Apple costs RS 50 ,'RS 60 for each pineapple 120','RS 150 per watermelon"
for msg in price:
    matches = re.findall("\d+",msg)
    print(matches)


# In[43]:


import regex as re        QUESTION NUMBER = 22


# In[49]:


input_string = "My marks in each semester are: 947,896,926,524,734,950,642"
numeric_values = re.findall(r'\d+',input_string)
numeric_values=[int(value) for value in numeric_values] 
max_value = max(numeric_values)                         
print(max_value)                   


# In[115]:


import regex as re


# In[64]:


import regex as re    QUESTION NUMBER = 23


# In[65]:


string = "RegularExpressionAnIsImportantTopicInPython"
words = re.findall("[A-Z][a-z]*",string)
print(' '. join((words)))
 


# In[120]:


import regex as re
pattern=r'[A-Z][a-z]+'
Text="This is a sample Text with multiple matches"              question no 24
matches= re.findall(pattern,text)
print(matches)


# In[121]:


import regex as re


# In[125]:


sentence="Hello hello world world"
def remove_duplicates(sentence):
 pattern=r'\b(\w+)(\s+\1\b)+'                     question no-25
 result=re.sub(pattern,r'\1',sentence)
 output=remove_duplicates(sentence)
 print(output)


# In[126]:


import regex as re 


# In[ ]:


def check_string(string):
    pattern = r'\w$'
    match= re.search(pattern,string)
    if match:
        return true
    else:                                      question no 26
        return false


# In[127]:


import regex as re       QUESTION NUMBER = 27


# In[75]:


def extract_hastages(text):
    text =' RT @kapil: #Doltiwal I mean #Xyzabc is "hurt" by #Demonetization as the same has rendered USELESS <ed><U+00A0><U+00BD><ed><U+00B1><U+0089>"acquired funds" NO wo'
    hastages = re.findall(r'#\w+',text)
    hastags=extract_hastages(text)
    print(hastages)


# 

# In[70]:


import regex as re      QUESTION NUMBER= 28


# In[80]:


input_text="@jags123456 Bharat band on 28??<ed><U+00A0><U+00BD><U+0082>Those who are protesting #demonetization are all diffrent party leaders"
pattern = r"<U\+\w{4>}"
output_text=re.sub(pattern ,'',input_text)
print(output_text)


# In[131]:


import regex as re     QUESTION NUMBER = 29


# In[82]:


text = "Ron was born on 12-09-1992 and he was admitted to school 15-12-1999." 
pattern = r'\d{2}-\d{2}-\d{4}'
A = re.findall(pattern,text)
print(A)                        


# In[83]:


import regex as re      QUESTION NUMBER = 30


# In[85]:


def remove_words(strings):
    pattern = re.compile(r'\b\w{2,4}\b')
    modified_string = re.sub(pattern,'',string)
    

sample_text = "The following example creates an ArrayList with a capacity of 50 elements.4 element are then added to the ArrayList and the Arraylist is trimmered accordingly."
expected_output = "following example creates ArrayList a capacity element. 4 elements added ArrayList trimmed accordingly."

result = remove_words(sample_text)
print(result == expected_output) #True


# In[ ]:




