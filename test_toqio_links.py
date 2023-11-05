from selenium import webdriver
from selenium.webdriver.common.by import By

def test_check_all_links_home_page():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://toqio.co/")

    # Find all links on the page
    
    all_links = driver.find_elements(By.TAG_NAME, 'a')

    # Collect href attributes

    hrefs = [link.get_attribute('href') for link in all_links]

    # Check each href for validity
    
    for href in hrefs:
        if href:
            try:
                driver.get(href)
                assert "error" not in driver.page_source.lower(), f"Link '{href}' is broken."
            except Exception as e:
                print(f"Error accessing link '{href}': {e}")
    driver.quit()



