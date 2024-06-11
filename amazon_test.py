import requests
from bs4 import BeautifulSoup

query = input("enter item you want to search ")

url = "https://www.flipkart.com/search?q=" + query.replace(" ", "%20")
print(url)


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299",
    "Accept-Language": "en-US,en;q=0.5"
}

response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.content, "html.parser")

results = soup.findAll("div", {'class':"_13oc-S"})
# print(results)
lis=[]
for result in results:
    price= result.find("div", {"class":"_30jeq3 _1_WHN1"})
    title = result.find("div", {'class':"_4rR01T"}).text.strip()
    print(title)
    if price:
        price = price.text.strip()
    else:
        price = "N/A"
    lis.append(f"{title} - {price}")
    
print(lis)