from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

tcb_user = ""
tcb_password = ""
service = Service(r"C:\Users\lior\Downloads\chromedriver.exe")
driver = webdriver.Chrome(service=service)

class LoginToTcb:
    def login_step1(self):
        driver.get("https://login.tcb.ac.il/nidp/saml2/sso?id=tcbloa2&sid=0&option=credential&sid=0")
        time.sleep(5)
        username = driver.find_element(By.ID , "Ecom_User_ID")
        username.send_keys(tcb_user)
        username.send_keys(Keys.ENTER)
        time.sleep(5)

    def login_step2(self):
        time.sleep(5)
        butten = driver.find_element(By.ID , "ldapPasswordCardClick")
        butten.click()
        time.sleep(5)

    def login_step3(self):
        time.sleep(5)
        another = driver.find_element(By.ID, "ldapPassword")
        another.send_keys(tcb_password)
        another.send_keys(Keys.ENTER)
        time.sleep(5)

# question 1 done
class Linkedinjobs:
    def login_linkin(self):
        driver.get("https://www.linkedin.com/checkpoint/lg/sign-in-another-account")
        time.sleep(5)
        username = driver.find_element(By.ID ,"username")
        password = driver.find_element(By.ID , "password")

        username.send_keys("")
        password.send_keys("")
        password.send_keys(Keys.ENTER)
        time.sleep(3)

        driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3664703142&distance=25&geoId=101620260&keywords=full%20stack%20developer&refresh=true")
        time.sleep(5)

        jobs = driver.find_elements(By.CSS_SELECTOR ,".job-card-list a")
        for n in range(len(jobs)):
            print(jobs[n].text)

        time.sleep(5)
        jobs = driver.find_element(By.CSS_SELECTOR , ".job-card-container")
        jobs.click()

        time.sleep(5)
        clickbuttun = driver.find_element(By.CSS_SELECTOR , ".jobs-apply-button")
        clickbuttun.click()
        driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3659015700&distance=25&geoId=101620260&keywords=full%20stack%20developer&refresh=true")






# question 2 done

class Random:
    def randomthings(self):
        driver.get("https://randomkeygen.com/")
        time.sleep(5)

        name = driver.find_elements(By.CSS_SELECTOR ,".input-wrap key")
        for n in range(len(name)):
            print(name[n].text)





what = Random()
what.randomthings()


# linkdin = Linkedinjobs()
# linkdin.login_linkin()

# tcb = LoginToTcb()
# tcb.login_step1()
# tcb.login_step2()
# tcb.login_step3()


