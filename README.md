
# Toqio-testcase

**QAE Case Study**

  

## Introduction

The technical test will be oriented to analyse https://toqio.co/, case selection, functional case writing and documentation, case automation, automatic case structure, also since it is a website we should test dead links, performance, security, and SEO.

  

## Phase I :

  
**Test cases**

 - Since we have a contact form and it is the only input in the website, we should make test cases for it
So we focus on the form (contact us) to make sure all the inputs will be securely implemented
You can find the implementation in this file.

>     test_toqio_contact_us.py

 - another test case, is to make sure all links are correct
 You can find the implementation in this file.

>  `test_toqio_links.py`

## Phase II

**Automated Test cases**

  

 1. making an automate to test the contact us form, using the automated 
    tools (Selenium) :

>     `(test_toqio_contact_us.py)`

 - First name test case
 - List item
 - Last name test case
 - email test case
 - phone test case
 - company test case
 - and so on

  

 2. Also tested all the links in the home page, using the automated tools   
    (Selenium)
   making an automate to Extracting and fetching all listed links in the home page, and   checking if they are accesible or not.

> `test_toqio_links.py):`

  

making an automate to Extracting and fetching all listed links in the home page, and checking if they are accesible or not.

  

 3. **Bonus task:**

Since it is a website, we should make some bonus tests to checks **Performance, SEO, and Security.**

 4. **Reports:**

you can find all the report attached to the project in the **bonus_reports** folder as follow : 

 1. `Test cases Report` (using **pytest-html**)
 2. `Performance Report` (using **lighthouse**)
 3. `SEO Report` (using **Seoptimer**, one of the best tools for SEO Auditing)
 4. `Security Report` (using **Acunetix**, a web application security scanner
    used by Fortune 500 companies  )

## Phase 3:

**Question :**

From your point of view and based on your experience, what should a company that wants to reduce the number of bugs in production do?
Explain at least one improvement strategy

**Response :**

From my experience, to reduce bugs in production, a company can opt for different improvement strategies : 

 - **Use automated testing in the continuous integration (CI) pipeline**
 
Integrate the automated testing practice into the CI pipeline to be sure that tests are executed automatically with each code commit.

 -  **Data-Driven Testing with Dynamic Test Data** 
 
 We opt for a testing approaches to cover a large range of input scenarios, ensuring the application behaves as expected under various conditions.
 Also we Implement dynamic test data to simulate realistic data scenarios, with that we have a more realistic test data before production.

 -  **Detailed documentation with every features deployment** 
 
We must have a detailed documentation for codebase, new features, and deployment procedures.

 -  **Other Strategies to keep in mind :** 
 
 Using Anit Bot system (like Akaimi)
 
 Using Anti DDOS attack (like cloudflare)
 
 Using good DNS for better indexation (around the world) 
 
 Since toqio.co is created by wordpress, it should be always up-to-date
 
 Reduce number of plugins (use the most popular/ up-to-date/ verified plugins)
 
 Always hide critical Links (wp-admin is already hidden)
 
