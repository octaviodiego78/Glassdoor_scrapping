# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 19:09:21 2022

@author: octav
"""

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import pandas as pd



def gettingLinksInfo(soup):
    for card in soup.select('.p-0.job-search-key-kgm6qi li'):
            link='https://www.glassdoor.com' + card.a.get('href')
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626 Safari/537.36'}
            page = requests.get(link,headers=headers)
            soup = BeautifulSoup(page.text, 'html.parser')
            div = soup.find(id="JobDescriptionContainer").text
            text.append(div)
        


def numberOfPages(driver):
    pages = driver.find_element_by_xpath('//*[@id="MainCol"]/div[2]/div/div[2]').text
    pages = pages[-2:]
    pages = int(pages)
    return pages


def logIn(driver):
        
    #opening page
    driver.get(main_link)
    time.sleep(5)
    
    #login
    driver.find_element_by_xpath('/html/body/header/nav[1]/div/div/div/div[5]/button').click()
    
    #email
    email = driver.find_element_by_id('modalUserEmail')
    email.send_keys("Your mail here") #!!!!!!!!
    
    
    #pssw
    pssw = driver.find_element_by_id('modalUserPassword')
    pssw.send_keys("Your password here")   #!!!!!!!!
    
    
    #log in
    driver.find_element_by_name("submit").click()

def pageScrapper(link):
    
    page = requests.get(link)
    soup = BeautifulSoup(page.text, 'html.parser')
    gettingLinksInfo(soup)

    

#-------------------------------------------- main ------------------------------------------- 

main_link = 'https://www.glassdoor.com/Job/united-states-business-intelligence-analyst-jobs-SRCH_IL.0,13_IN1_KO14,43.htm?includeNoSalaryJobs=true&pgc=AB4AAIEAAAAAAAAAAAAAAAAAAd1sTGwAAwAAAQAA'
driver = webdriver.Chrome(executable_path=r"C:\\chromedriver.exe")

#Log in funciton
logIn(driver)



text = []

#Scrapping the first page
pageScrapper(main_link)


#scrapping all pages
for i in range(0,numberOfPages(driver)):
    
    try:
    
        driver.find_element_by_xpath('//*[@id="MainCol"]/div[2]/div/div[1]/button[7]').click()
        time.sleep(5)
        pageScrapper(driver.current_url)
        
        
        
    except Exception as e:
        print(e)
        print("Error in page {}".format(i+1))
        
        
df = pd.DataFrame(text,columns =['text'])
df.to_csv('df.csv')

            
            
    
    