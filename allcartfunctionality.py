from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Initialize the WebDriver (make sure you have installed the appropriate WebDriver for your browser)
driver = webdriver.Chrome()  # Assuming Chrome WebDriver is used, download from https://sites.google.com/a/chromium.org/chromedriver/

# Open JioMart website
driver.get("https://www.jiomart.com/")

# Function to test search functionality
def test_search(search_query):
    search_box = driver.find_element_by_id("search")
    search_box.clear()
    search_box.send_keys(search_query)
    search_box.send_keys(Keys.RETURN)
    time.sleep(2)  # Wait for the page to load

    # Verify if search results are displayed
    assert "Search results for" in driver.page_source, f"Failed to search for '{search_query}'"

# Function to test add to cart functionality
def test_add_to_cart(product_name):
    product_locator = f"//div[contains(@class, 'category-item')]//div[contains(@class, 'product-name') and contains(text(), '{product_name}')]"
    add_to_cart_button = driver.find_element_by_xpath(f"{product_locator}/ancestor::div[contains(@class, 'category-item')]//button[contains(@class, 'cart')]")
    add_to_cart_button.click()
    time.sleep(2)  # Wait for the product to be added to cart

    # Verify if product is added to cart
    assert "Added to cart" in driver.page_source, f"Failed to add '{product_name}' to cart"

# Function to test billing functionality
def test_billing():
    # Go to cart page
    cart_icon = driver.find_element_by_xpath("//a[contains(@href, 'checkout/cart')]")
    cart_icon.click()
    time.sleep(2)  # Wait for cart page to load

    # Proceed to checkout (assuming there is a checkout button or flow)
    checkout_button = driver.find_element_by_xpath("//button[contains(@class, 'checkout-btn')]")
    checkout_button.click()
    time.sleep(2)  # Wait for checkout page to load

    # Fill billing information (assuming form fields exist)
    # Example:
    # billing_name = driver.find_element_by_id("billing-name")
    # billing_name.send_keys("Your Name")

    # Continue with payment (assuming there is a payment button)
    # payment_button = driver.find_element_by_xpath("//button[contains(@class, 'payment-btn')]")
    # payment_button.click()
    # time.sleep(2)  # Wait for payment to process

    # Verify if order is successfully placed (assuming there is a confirmation message or page)
    # assert "Order placed successfully" in driver.page_source, "Failed to place order"

try:
    # Test scenarios
    test_search("toothpaste")
    test_add_to_cart("Colgate Toothpaste")
    test_billing()
    print("All tests passed successfully!")

finally:
    # Close the browser window
    driver.quit()
