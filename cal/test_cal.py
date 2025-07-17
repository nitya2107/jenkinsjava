import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Set up the WebDriver (Chrome in this case)
driver = webdriver.Chrome()

def test_addition():
    driver.get("http://localhost:8000/index.html")  # Accessing the web app hosted locally
    time.sleep(1)

    # Input 2 + 3
    driver.find_element(By.XPATH, "//button[text()='2']").click()
    driver.find_element(By.XPATH, "//button[text()='+']").click()
    driver.find_element(By.XPATH, "//button[text()='3']").click()
    driver.find_element(By.XPATH, "//button[text()='=']").click()
    time.sleep(1)

    result = driver.find_element(By.ID, "result").get_attribute('value')
    assert result == '5', f"Expected 5 but got {result}"

def test_subtraction():
    driver.get("http://localhost:8000/index.html")
    time.sleep(1)

    # Input 5 - 3
    driver.find_element(By.XPATH, "//button[text()='5']").click()
    driver.find_element(By.XPATH, "//button[text()='-']").click()
    driver.find_element(By.XPATH, "//button[text()='3']").click()
    driver.find_element(By.XPATH, "//button[text()='=']").click()
    time.sleep(1)

    result = driver.find_element(By.ID, "result").get_attribute('value')
    assert result == '2', f"Expected 2 but got {result}"

def test_clear():
    driver.get("http://localhost:8000/index.html")
    time.sleep(1)

    # Input and Clear
    driver.find_element(By.XPATH, "//button[text()='2']").click()
    driver.find_element(By.XPATH, "//button[text()='+']").click()
    driver.find_element(By.XPATH, "//button[text()='3']").click()
    driver.find_element(By.XPATH, "//button[text()='C']").click()
    time.sleep(1)

    result = driver.find_element(By.ID, "result").get_attribute('value')
    assert result == '', f"Expected '' but got {result}"

# Run the tests
try:
    test_addition()
    test_subtraction()
    test_clear()
    print("All tests passed!")
except AssertionError as e:
    print(f"Test failed: {e}")
finally:
    driver.quit()

