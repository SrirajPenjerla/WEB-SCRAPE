from bs4 import BeautifulSoup
import requests
import lxml

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299",
    "Accept-Language": "en-US,en;q=0.5"}

def amazon_find(query):
    url = "https://www.amazon.in/s?k=" + query.replace(" ", "+")
    # print(url)
    response = requests.get(url, headers=headers)
    lis=[]
    soup = BeautifulSoup(response.content, "html.parser")
    links = soup.findAll("a",{"class":"a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal"})
    link_lis=[]
    print(links)
    for link in links:
        print(link.get('href'))
        link_lis.append(link.get('href'))
    print(link_lis)
    for link in link_lis:
        new_page= requests.get("https://www.amazon.in"+link,headers=headers)
        print(new_page)
        new_soup=BeautifulSoup(new_page.content,"html.parser")
        title= new_soup.find('span',attrs={'class':'a-size-large product-title-word-break'}).text.strip()
        print(title)
        price= new_soup.find('span',attrs={'class':'a-price-whole'}).text
        print(price)
        lis.append(f"{title} - ₹{price}.")
    return (lis)
        


    # lis=[]
    # print(lis)
    # for result in results:
    #     l=[]
    #     title=["",]
    #     price= result.find("span", {"class":"a-price-whole"})
    #     title .append(result.findAll( "span",{"class":"a-size-medium a-color-base a-text-bold a-text-normal"}).text)
    #     # for i in l:
    #     #     title.concat(i.text)
    #     if price:
    #         price = price.text.strip()
    #     else:
    #         price = "N/A"
    #     print(f"{title} - ₹{price}")
    #     lis.append(f"{title} - ₹{price}.")
    # return(lis)
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
    # results = soup.findAll("div", {'class':"_13oc-S" or "_4ddWXP"})
    results = soup.findAll("div", {'class':"yKfJKb row"})
    lis=[]
    for result in results:
        price= result.find("div", {"class":"Nx9bqj _4b5DiR" })
        title = result.find("div", {'class':"KzDlHZ"}).text.strip()
    #print(title)
        if price:
            price = price.text.strip()
        else:
            price = "N/A"
        
        lis.append(f" {title} - {price}.")
    return(lis)

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
    
