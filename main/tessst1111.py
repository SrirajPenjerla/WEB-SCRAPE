from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the WebDriver (Make sure to replace with your correct driver path)
driver = webdriver.Chrome()

def amazon_find(query):
    # Navigate to Amazon
    driver.get("https://www.amazon.in/")
    
    # Find the search box and enter the query
    search_box = driver.find_element(By.ID, "twotabsearchtextbox")
    search_box.send_keys(query)
    search_box.submit()
    
    # Wait for the results to load
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="s-main-slot"]')))

    # Extract titles and prices from the search results
    results = driver.find_elements(By.XPATH, '//div[@class="s-main-slot"]//div[@data-component-type="s-search-result"]')
    
    for result in results:
        try:
            # Extract title
            title = result.find_element(By.XPATH('.//span[@class="a-size-medium a-color-base a-text-normal"]')).text
            
            # Extract price
            price_whole = result.find_element(By.XPATH('.//span[@class="a-price-whole"]')).text
            price_fraction = result.find_element(By.XPATH('.//span[@class="a-price-fraction"]')).text
            
            price = f"{price_whole}.{price_fraction}" if price_whole and price_fraction else "N/A"
        except Exception as e:
            title = "N/A"
            price = "N/A"
        
        print(f"Title: {title}, Price: {price}")

# Example usage
query = "laptop"
amazon_find(query)

# Close the driver
driver.quit()
