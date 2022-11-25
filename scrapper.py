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
            time.sleep(5)
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
    email.send_keys("octaviodiego78@gmail.com") #!!!!!!!!
    
    
    #pssw
    pssw = driver.find_element_by_id('modalUserPassword')
    pssw.send_keys("Dp.103260")   #!!!!!!!!
    
    
    #log in
    driver.find_element_by_name("submit").click()

def pageScrapper(link):
    
    page = requests.get(link)
    soup = BeautifulSoup(page.text, 'html.parser')
    gettingLinksInfo(soup)

    

#-------------------------------------------- main ------------------------------------------- 

main_link = 'https://www.glassdoor.com.mx/Empleo/jalisco-negocios-internacionales-empleos-SRCH_IL.0,7_IS5737_KO8,32.htm?suggestCount=0&suggestChosen=false&clickSource=searchBtn&typedKeyword=&typedLocation=Jalisco%252C%2520Mexico&context=Jobs&dropdown=0'
driver = webdriver.Chrome(executable_path=r"C:\\chromedriver.exe")

#Log in funciton
logIn(driver)



text = []

#Scrapping the first page
pageScrapper(main_link)


#scrapping all pages
for i in range(0,numberOfPages(driver)):
    
    try:
        print('running page {}'.format(i+2))
        driver.find_element_by_xpath('//*[@id="MainCol"]/div[2]/div/div[1]/button[7]').click()
        time.sleep(5)
        pageScrapper(driver.current_url)
        print(len(text ))
        
        
        
    except Exception as e:
        print(e)
        print("Error in page {}".format(i+2))
        
        
df = pd.DataFrame(text,columns =['text'])
df.to_csv('majo.csv')

            
            
    
    