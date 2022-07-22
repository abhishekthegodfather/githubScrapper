#!/usr/bin/env python
# coding: utf-8

# In[2]:


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from urllib.parse import urlparse
import pandas as pd
import time


# In[6]:


driver = webdriver.Firefox(executable_path=r'C:\Users\abhis\OneDrive\Desktop\scrapping_python\linkedin_scarp\geckodriver.exe')
driver.get('https://github.com/topics')

time.sleep(10)
lang = driver.find_elements(By.CSS_SELECTOR, "a>p.lh-condensed.text-center")
langArr = []
for i in lang:
    i = i.text
    langArr.append(i)
print(langArr)

time.sleep(10)
langCon = driver.find_elements(By.CSS_SELECTOR, "a>p.color-fg-muted.text-center")
langConArr = []
for i in langCon:
    i = i.text
    langConArr.append(i)
print(langConArr)

time.sleep(10)
langlinks = driver.find_elements(By.CSS_SELECTOR, "a.no-underline.d-flex.flex-column.flex-justify-center")
langlinksArr = []
for i in langlinks:
    i = i.get_attribute('href')
    langlinksArr.append(i)
print(langConArr)

lang_dict = {
    "Langauge" : langArr,
    "Short Description" : langConArr,
    "Langauge Topic Links" : langlinksArr
}

data = pd.DataFrame(lang_dict)
data.to_csv("Github_Topics.csv")


# # ISSUE FINDING

# In[21]:


def issue(url):
    driver = webdriver.Firefox(executable_path=r'C:\Users\abhis\OneDrive\Desktop\scrapping_python\linkedin_scarp\geckodriver.exe')
    driver.get(url)
    
    time.sleep(10)
    repos = driver.find_elements(By.CSS_SELECTOR, "h3.f3.color-fg-muted.text-normal.lh-condensed")
    reposArr = []
    for i in repos:
        i = i.text
        reposArr.append(i)
#     print(reposArr)
    
    time.sleep(10)
    star = driver.find_elements(By.CSS_SELECTOR, "span#repo-stars-counter-star")
    starArr = []
    for i in star:
        i = i.text
        starArr.append(i)
#     print(starArr)
    
    dict1 = {
        "Repositories" : reposArr,
        "stars" : starArr
    }
    
    data1 = pd.DataFrame(dict1)
    data1.to_csv('Repos.csv')
    
    findLink = driver.find_elements(By.CSS_SELECTOR, "li.d-inline-flex>a")
    findLinkArr = []
    for i in findLink:
        i = i.get_attribute('href')
        findLinkArr.append(i)
#     print(findLinkArr)
    
    arr = []
    for i in findLinkArr:
        urlP = urlparse(i)
        arr.append(urlP.path)
    # print(arr)
    arr2 = []
    for i in arr:
        if i.find('/issue') != -1:
            arr2.append("https://github.com"+str(i))
    print(arr2)
    
    for i in arr2:
        issue_finder(i)


# In[22]:


def issue_finder(url):
    driver = webdriver.Firefox(executable_path=r'C:\Users\abhis\OneDrive\Desktop\scrapping_python\linkedin_scarp\geckodriver.exe')
    driver.get(url)
    sam = driver.find_elements(By.CSS_SELECTOR, "a.Link--primary.v-align-middle")
    findLinkArr = []
    for i in sam:
        i = i.text
        findLinkArr.append(i)
    print(findLinkArr)
    
#     str2 = ""
#     for i in findLinkArr:
#         str2 += i+"\n"
#     with open('issue.txt', 'a') as file:
#         file.write(str2)


# In[23]:


for i in langlinksArr:
    issue(i)


# In[5]:





# In[ ]:




