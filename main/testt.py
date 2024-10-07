from bs4 import BeautifulSoup
import requests
import time
# import lxml
# import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299",
#     "Accept-Language": "en-US,en;q=0.5"}
# headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36', "Upgrade-Insecure-Requests": "1","DNT": "1","Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8","Accept-Language": "en-US,en;q=0.5","Accept-Encoding": "gzip, deflate"}
# def amazon_find(query):
#     url = "https://www.amazon.in/s?k=" + query.replace(" ", "+")
#     response = requests.get(url,headers=headers,timeout=5)
#     # print(response.status_code)
#     soup = BeautifulSoup(response.content, "lxml")
#     results = soup.findAll("div", {"data-component-type":"s-search-result"})
#     lis=[]
#     print(results)
#     for result in results:
#         price= result.find("span", {"class":"a-price-whole"})
#         title = result.findAll("span", {"class":"a-size-medium a-color-base a-text-normal"})
#         # if title is NULL:
#         #     title=query
        
#         # title=query
#         if price:
#             price = price.text.strip()
#         else:
#             price = "N/A"
        
#         lis.append(f"{title} - ₹{price}.")
#     return(lis)


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
        try:
            title=result.find_element(By.XPATH,'.//h2/a/span').text
            price=result.find_element(By.XPATH,'.//span[@class="a-price-whole"]').text
        except:
            title=result.find_element(By.XPATH,'.//span[@class="a-size-base-plus a-color-base a-text-normal"]').text
            price=result.find_element(By.XPATH,'.//span[@class="a-price-whole"]').text

        lis.append(f" {title} - {price}.")
    #     print(lis)
    # if not lis:
    #     for result in results:
            
    #         lis.append(f" {title} - {price}.")
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
    time.sleep(4)
    try:
        for result in results:
            title=result.find_element(By.XPATH,'.//h2/a/span').text
            price=result.find_element(By.XPATH,'.//span[@class="a-price-whole"]').text
            lis.append(f" {title} - {price}.")
            i+=1
            print(lis)
    except:
        for result in results:
            title=result.find_element(By.XPATH,'.//span[@class="a-size-base-plus a-color-base a-text-normal"]').text
            price=result.find_element(By.XPATH,'//span[@class="a-price-whole"]').text
            lis.append(f" {title} - {price}.")
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
    

    
if __name__=='__main__':
    while(1):
        query = input("enter item you want to search ").lower()
        num=int(input("press    1 ------> amazon    2-------> flipkart  \n"))
        if num==1:
            results=amazon_find(query)
            print('\n'.join(results))
        elif num==2:
            results=flipkart_find(query)
            print('\n'.join(results))
        else:
            print("no such number")
    
