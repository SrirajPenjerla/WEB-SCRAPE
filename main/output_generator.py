from bs4 import BeautifulSoup
import requests
# import lxml
# import re
import time
# import lxml
# import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299",
    "Accept-Language": "en-US,en;q=0.5"}

def amazon_find(query):
    url = "https://www.amazon.in/s?k=" + query.replace(" ", "+")
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "lxml")
    results = soup.findAll("div", {'data-component-type':'s-search-result'})
    lis=[]
    print(lis)
    for result in results:
        price= result.find("span", {"class":"a-price-whole"})
        # title=query.upper()
        # title = soup.find("span", attrs={"id":'productTitle'})
        # title=title.string.strip()
        title = result.find("span", {"class":"a-size-medium a-color-base a-text-normal"}).text.strip()
        # result.find("span", title = re.compile(query).text.strip())
        if price:
            price = price.text.strip()
        else:
            price = "N/A"
        
        lis.append(f"{title} - ₹{price}.")
    return(lis)
# class="a-size-medium a-color-base a-text-normal"
# def amazon_find(query):
#     url = "https://www.amazon.in/s?k=" + query.replace(" ", "+")
#     response = requests.get(url, headers=headers)
#     soup = BeautifulSoup(response.content, "lxml")
#     results = soup.findAll("div", {'data-component-type':'s-search-result'})
#     lis=[]
#     for result in results:
#         price= result.find("span", {"class":"a-price-whole"})
#         # title = result.find("span", {"class":"a-size-medium a-color-base a-text-normal"}).text.strip()
#         # if title is NULL:
#         #     title=query
        
#         title=query
        
#         if price:
#             price = price.text.strip()
#         else:
#             price = "N/A"
        
#         lis.append(f"{title} - ₹{price}.")
#     return(lis)



def flipkart_find(query):
    url = "https://www.flipkart.com/search?q=" + query.replace(" ", "%20")
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "lxml")
    results = soup.findAll("div", {'class':"yKfJKb row"or"cPHDOP col-12-12"or"nt6sNV JxFEK3 _48O0EI"or"_13oc-S" or "_4ddWXP" })
    lis=[]
    for result in results:
        price= result.find("div", {"class":"Nx9bqj _4b5DiR" })
        title = result.find("div", {'class':"KzDlHZ" or "s1Q9rs"}).text.strip()
    #print(title)
        if price:
            price = price.text.strip()
        else:
            price = "N/A"
        
        lis.append(f" {title} - {price}.")
    return(lis)

#if __name__=='__main__':
#     while(1):
#         query = input("enter item you want to search ").lower()
#         num=int(input("press    1 ------> amazon    2-------> flipkart  \n"))
#         if num==1:
#             results=amazon_find(query)
#             print('\n'.join(results))
#         elif num==2:
#             results=flipkart_find(query)
#             print('\n'.join(results))
#         else:
#             print("no such number")
    
def flipkart_find(query):
    driver=webdriver.Chrome()
    driver.get(url="https://www.flipkart.com")
    sbox=driver.find_element(By.NAME, "q")
    sbox.send_keys(query)
    sbox.send_keys(Keys.RETURN)
    time.sleep(2)
    results=driver.find_elements(By.XPATH, '//div[@class="tUxRFH"]')
    lis=[]
    for result in results:
        title=result.find_element(By.XPATH, './/div[@class="KzDlHZ"]').text
        price=result.find_element(By.XPATH, './/div[@class="Nx9bqj _4b5DiR"]').text
        lis.append(f" {title} - {price}.")
        print(lis)
    return lis


def amazon_find(query):
    driver=webdriver.Chrome()
    driver.get(url="https://www.amazon.in")
    sbox=driver.find_element(By.XPATH,'//*[@id="twotabsearchtextbox"]')
    sbox.send_keys(query)
    sbox.send_keys(Keys.RETURN)
    time.sleep(2)
    results=driver.find_elements(By.XPATH,'//div[@data-component-type="s-search-result"]')
    lis=[]
    for result in results:
        title=result.find_element(By.XPATH,'.//h2/a/span').text
        price=result.find_element(By.XPATH,'.//span[@class="a-price-whole"]').text
        lis.append(f" {title} - {price}.")
        print(lis)
    return lis



# overriding

def amazon_find(query):
    driver=webdriver.Chrome()
    driver.get(url="https://www.amazon.in")
    sbox=driver.find_element(By.XPATH,'//*[@id="twotabsearchtextbox"]')
    sbox.send_keys(query)
    sbox.send_keys(Keys.RETURN)
    time.sleep(2)
    results=driver.find_elements(By.XPATH,'//div[@data-component-type="s-search-result"]')
    lis=[]
    time.sleep(4)
    try:
        for result in results:
            title=result.find_element(By.XPATH,'.//h2/a/span').text
            price=result.find_element(By.XPATH,'.//span[@class="a-price-whole"]').text
            lis.append(f" {title} - ₹ {price}.")
            i+=1
            print(lis)
    except:
        for result in results:
            title=result.find_element(By.XPATH,'.//span[@class="a-size-base-plus a-color-base a-text-normal"]').text
            price=result.find_element(By.XPATH,'//span[@class="a-price-whole"]').text
            lis.append(f" {title} - ₹ {price}.")
            print(lis)

    return lis

def flipkart_find(query):
    driver=webdriver.Chrome()
    driver.get(url="https://www.flipkart.com")
    sbox=driver.find_element(By.NAME, "q")
    sbox.send_keys(query)
    sbox.send_keys(Keys.RETURN)
    time.sleep(2)
    results=driver.find_elements(By.XPATH,'//div[@class="_75nlfW"]')
    lis=[]
    time.sleep(2)
    try:
        for result in results:
            title=result.find_element(By.XPATH, './/div[@class="KzDlHZ"]').text
            price=result.find_element(By.XPATH, './/div[@class="Nx9bqj _4b5DiR"]').text
            lis.append(f" {title} - {price}.")
            print(lis)
    except:
        for result in results:
            title=result.find_element(By.XPATH, './/a[@class="wjcEIp"]').text
            price=result.find_element(By.XPATH, './/div[@class="Nx9bqj"]').text
            lis.append(f" {title} - {price}.")
            print(lis)

    return lis