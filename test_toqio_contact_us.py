from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By

mock_form_data = {
"first_name": "Aziz",
"last_name": "Bardi",
"email": "bardiaziz@blackwave.trading",
"phone": "658521970",
"company": "Aziz ltd",
"headquarters": "Spain",
"baas_provider": "Railsr",
"offer_service": "UK",
"hear_about_us": "Event",
}


def contact_us_form_submission(first_name, last_name, email, phone, company, headquarters, baas_provider, offer_service, hear_about_us ):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://toqio.co/")
    
    # Navigate to the Contact Us page
    contact_us_link = driver.find_element(By.CSS_SELECTOR, ".btn-pink")
    contact_us_link.click()
    driver.switch_to.window(driver.window_handles[1])

    # Fill in the contact form
    first_name_input = driver.find_element(By.NAME,"firstname")
    last_name_input = driver.find_element(By.NAME,"lastname")
    email_input = driver.find_element(By.NAME,"email")
    phone_input = driver.find_element(By.NAME,"phone")
    company_input = driver.find_element(By.NAME,"company")
    headquarters_input = driver.find_element(By.NAME,"location_of_headquarters")
    baas_provider_input = driver.find_element(By.NAME,"do_you_currently_have_a_baas_provider_")
    offer_service_input = driver.find_element(By.NAME, "where_would_you_like_to_offer_your_services_")
    hear_about_us_input = driver.find_element(By.NAME, "how_did_you_hear_about_us_")


    first_name_input.send_keys(first_name)
    last_name_input.send_keys(last_name)
    email_input.send_keys(email)
    phone_input.send_keys(phone)
    company_input.send_keys(company)
    headquarters_input.send_keys(headquarters)
    baas_provider_input.send_keys(baas_provider)
    offer_service_input.send_keys(offer_service)
    hear_about_us_input.send_keys(hear_about_us)

    # Check the "Agree to receive emails" checkbox
    
    js_code = "arguments[0].scrollIntoView();"
    footer = driver.find_element(By.TAG_NAME, 'footer')

    # Execute the JS script

    driver.execute_script(js_code, footer)

    agree_checkbox = driver.find_element(By.NAME, "LEGAL_CONSENT.subscription_type_46630711")
    agree_checkbox.send_keys(Keys.SPACE)
    
    subscribe_checkbox = driver.find_element(By.NAME, 'LEGAL_CONSENT.subscription_type_13029907')
    subscribe_checkbox.send_keys(Keys.SPACE)

    time.sleep(2)

    # Submit the form
    
    submit_button = driver.find_element(By.XPATH, "//input[@type='submit']")
    submit_button.click()

    return driver

# Test Execution for first name

def test_contact_us_form_first_name_invalid():
    mock_form_data["first_name"] = "john,"
    driver = contact_us_form_submission(**mock_form_data)
    first_name_input = driver.find_element(By.NAME,"firstname")
    errors = first_name_input.find_element(By.XPATH,"./../..").find_elements(By.CLASS_NAME,"hs-error-msgs")
    driver.quit()
    assert len(errors) >=1 


def test_contact_us_form_first_name_valid():
    mock_form_data["first_name"] = "john"
    driver = contact_us_form_submission(**mock_form_data)
    first_name_input = driver.find_element(By.NAME,"firstname")
    errors = first_name_input.find_element(By.XPATH,"./../..").find_elements(By.CLASS_NAME,"hs-error-msgs")
    driver.quit()
    assert len(errors) == 0


# Test Execution for last name

def test_contact_us_form_last_name_invalid():
    mock_form_data["last_name"] = "bardi,"
    driver = contact_us_form_submission(**mock_form_data)
    last_name_input = driver.find_element(By.NAME,"lastname")
    errors = last_name_input.find_element(By.XPATH,"./../..").find_elements(By.CLASS_NAME,"hs-error-msgs")
    driver.quit()
    assert len(errors) >=1 


def test_contact_us_form_last_name_valid():
    mock_form_data["last_name"] = "bardi"
    driver = contact_us_form_submission(**mock_form_data)
    last_name_input = driver.find_element(By.NAME,"lastname")
    errors = last_name_input.find_element(By.XPATH,"./../..").find_elements(By.CLASS_NAME,"hs-error-msgs")
    driver.quit()
    assert len(errors) == 0 

# Test Execution for phone number

def test_contact_us_form_phone_invalid():
    mock_form_data["phone"] = "658521970,"
    driver = contact_us_form_submission(**mock_form_data)
    phone_input = driver.find_element(By.NAME,"phone")
    errors = phone_input.find_element(By.XPATH,"./../..").find_elements(By.CLASS_NAME,"hs-error-msgs")
    driver.quit()
    assert len(errors) >=1 


def test_contact_us_form_phone_valid():
    mock_form_data["phone"] = "658521970"
    driver = contact_us_form_submission(**mock_form_data)
    phone_input = driver.find_element(By.NAME,"phone")
    errors = phone_input.find_element(By.XPATH,"./../..").find_elements(By.CLASS_NAME,"hs-error-msgs")
    driver.quit() 
    assert len(errors) == 0

# Test Execution for company name

def test_contact_us_form_company_invalid():
    mock_form_data["company"] = ""
    driver = contact_us_form_submission(**mock_form_data)
    company_input = driver.find_element(By.NAME,"company")
    errors = company_input.find_element(By.XPATH,"./../..").find_elements(By.CLASS_NAME,"hs-error-msgs")
    driver.quit()
    assert len(errors) >=1 


def test_contact_us_form_company_valid():
    mock_form_data["company"] = "john LTD"
    driver = contact_us_form_submission(**mock_form_data)
    company_input = driver.find_element(By.NAME,"company")
    errors = company_input.find_element(By.XPATH,"./../..").find_elements(By.CLASS_NAME,"hs-error-msgs")
    driver.quit()
    assert len(errors) == 0    


# Test Execution for email
def test_contact_us_form_syntax_email_invalid():
    mock_form_data["email"] = "john.com"
    driver = contact_us_form_submission(**mock_form_data)
    email_input = driver.find_element(By.NAME,"email")
    errors = email_input.find_element(By.XPATH,"./../..").find_elements(By.CLASS_NAME,"hs-error-msgs")
    driver.quit()
    assert len(errors) >=1 

def test_contact_us_form_email_invalid():
    mock_form_data["email"] = "johndow@yahoo.com"
    driver = contact_us_form_submission(**mock_form_data)
    email_input = driver.find_element(By.NAME,"email")
    errors = email_input.find_element(By.XPATH,"./../..").find_elements(By.CLASS_NAME,"hs-error-msgs")
    driver.quit()
    assert len(errors) > 0 

def test_contact_us_form_email_valid():
    mock_form_data["email"] = "johndow@toqio.com"
    driver = contact_us_form_submission(**mock_form_data)
    email_input = driver.find_element(By.NAME,"email")
    errors = email_input.find_element(By.XPATH,"./../..").find_elements(By.CLASS_NAME,"hs-error-msgs")
    driver.quit()
    assert len(errors) == 0 

